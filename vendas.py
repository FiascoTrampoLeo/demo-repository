from datetime import datetime
from produtos import encontrar_produto
from relatorios import registrar_movimentacao

# Lista para armazenar o histórico de vendas
vendas = []

def aplicar_desconto(preco, percentual):
    """Aplica um desconto percentual ao preço"""
    if 0 < percentual <= 100:
        return preco * (1 - percentual / 100)
    print("Percentual de desconto errado. Nenhum desconto foi aplicado.")
    return preco

def gerar_recibo(venda_atual):
    """gera um recibo simples para a venda na tela"""
    print("\n" + "="*35)
    print("---=@ RECIBO DA VENDA @=---")
    print(f"Data: {venda_atual['data'].strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 35)
    
    subtotal_geral = 0
    for item in venda_atual['itens']:
        produto = item['produto']
        subtotal_item = item['quantidade'] * produto['preco']
        subtotal_geral += subtotal_item
        print(f"Produto: {produto['nome']} (Cód: {produto['codigo']})")
        print(f"  {item['quantidade']} x R$ {produto['preco']:.2f} = R$ {subtotal_item:.2f}")
    
    print("-" * 35)
    if venda_atual['desconto'] > 0:
        print(f"Subtotal: R$ {subtotal_geral:.2f}")
        desconto_valor = subtotal_geral * (venda_atual['desconto'] / 100)
        print(f"Desconto ({venda_atual['desconto']}%): - R$ {desconto_valor:.2f}")
    
    print(f"VALOR TOTAL: R$ {venda_atual['valor_total']:.2f}")
    print("---=@ OBRIGADO PELA PREFERÊNCIA! @=---")
    print("="*35)


def registrar_venda():
    """Registra a venda de um ou mais produtos, atualiza o estoque e gera recibo"""
    print("\n---=@ Registrar Nova Venda @=---")
    
    itens_venda = []
    valor_sem_desconto = 0
    
    while True:
        codigo = input("Digite o código do produto (ou 'fim' para finalizar): ")
        if codigo.lower() == 'fim':
            break

        produto = encontrar_produto(codigo)
        if not produto:
            print("Produto não encontrado.")
            continue
            
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade para '{produto['nome']}': "))
                if quantidade <= 0:
                    print("A quantidade tem que ser um número positivo.")
                elif quantidade > produto['quantidade']:
                    print(f"Sem estoque. Disponível: {produto['quantidade']}")
                else:
                    break
            except ValueError:
                print("Entrada errada. Por favor, digite um número inteiro.")

        itens_venda.append({"produto": produto, "quantidade": quantidade})
        valor_sem_desconto += produto['preco'] * quantidade
        print(f"Produto '{produto['nome']}' adicionado à venda.")

    if not itens_venda:
        print("Nenhum produto adicionado. Venda cancelada.")
        input("\nPressione Enter para voltar ao menu...")
        return
        
    print(f"\nSubtotal da venda: R$ {valor_sem_desconto:.2f}")
    valor_final = valor_sem_desconto
    desconto_percentual = 0

    aplicar = input("Deseja aplicar algum desconto? (s/n): ").lower()
    if aplicar == 's':
        while True:
            try:
                desconto_percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
                if 0 < desconto_percentual <= 100:
                    valor_final = aplicar_desconto(valor_sem_desconto, desconto_percentual)
                    break
                else:
                    print("O percentual de desconto deve ser um número entre 1 e 100.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    
    print(f"Valor total final: R$ {valor_final:.2f}")
    confirmar = input("Confirmar venda? (s/n): ").lower()

    if confirmar == 's':
        nova_venda = {
            "data": datetime.now(),
            "itens": itens_venda,
            "desconto": desconto_percentual,
            "valor_total": valor_final
        }
        vendas.append(nova_venda)
        
        # Atualiza o estoque e registra a movimentação para cada item
        for item in itens_venda:
            produto_vendido = item['produto']
            quantidade_vendida = item['quantidade']
            # Atualiza estoque
            produto_vendido['quantidade'] -= quantidade_vendida
            # Registra no histórico
            registrar_movimentacao(produto_vendido, quantidade_vendida, "Saída por Venda")
        
        print("\nVenda registrada com sucesso!")
        gerar_recibo(nova_venda)

    else:
        print("Venda cancelada.")
        
    input("\nPressione Enter para voltar ao menu...")
