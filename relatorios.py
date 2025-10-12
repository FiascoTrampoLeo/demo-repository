from datetime import datetime

# Lista para armazenar o histórico de todas as movimentações de estoque
historico_movimentacoes = []

def registrar_movimentacao(produto, quantidade, tipo_movimentacao):
    """Registra uma movimentação de estoque no histórico"""
    movimentacao = {
        "data": datetime.now(),
        "produto_nome": produto["nome"],
        "produto_codigo": produto["codigo"],
        "tipo": tipo_movimentacao,
        "quantidade_movida": quantidade,
        "estoque_apos_mov": produto["quantidade"]
    }
    historico_movimentacoes.append(movimentacao)

def relatorio_vendas(lista_de_vendas):
    """Exibe um relatório detalhado de todas as vendas realizadas"""
    print("\n---=@ Relatório de Vendas @=---")
    if not lista_de_vendas:
        print("Nenhuma venda registrada até o momento.")
    else:
        faturamento_total = 0
        for i, venda in enumerate(lista_de_vendas, 1):
            print("\n" + "-"*40)
            print(f"VENDA #{i} | Data: {venda['data'].strftime('%d/%m/%Y %H:%M:%S')}")
            print("Itens Vendidos:")
            subtotal_venda = 0
            for item in venda['itens']:
                produto = item['produto']
                valor_item = item['quantidade'] * produto['preco']
                subtotal_venda += valor_item
                print(f"  - Produto: {produto['nome']} | Qtd: {item['quantidade']} | Valor: R$ {valor_item:.2f}")
            
            if venda['desconto'] > 0:
                print(f"Subtotal: R$ {subtotal_venda:.2f}")
                print(f"Desconto: {venda['desconto']}%")

            print(f"Valor Total da Venda: R$ {venda['valor_total']:.2f}")
            faturamento_total += venda['valor_total']
        
        print("\n" + "="*40)
        print(f"FATURAMENTO GERAL: R$ {faturamento_total:.2f}")
        print("="*40)

    input("\nPressione Enter para voltar ao menu...")
    
def relatorio_estoque(lista_de_produtos):
    """Mostra a quantidade atual de todos os produtos em formato de tabela"""
    print("\n---=@ Relatório de Estoque Atual @=---")
    if not lista_de_produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("-" * 60)
        print(f"{'CÓDIGO':<15} | {'NOME DO PRODUTO':<30} | {'QUANTIDADE':<10}")
        print("-" * 60)
        for produto in lista_de_produtos:
            print(f"{produto['codigo']:<15} | {produto['nome']:<30} | {produto['quantidade']:<10}")
        print("-" * 60)

    input("\nPressione Enter para voltar ao menu...")

def relatorio_historico_movimentacoes():
    """Exibe o histórico completo de movimentações de estoque"""
    print("\n---=@ Histórico de Movimentações de Estoque @=---")
    if not historico_movimentacoes:
        print("Nenhuma movimentação de estoque registrada.")
    else:
        print("-" * 120)
        print(f"{'DATA E HORA':<20} | {'CÓDIGO':<15} | {'PRODUTO':<30} | {'TIPO DE MOVIMENTAÇÃO':<20} | {'QUANTIDADE':<10} | {'ESTOQUE FINAL':<15}")
        print("-" * 120)
    
        for mov in reversed(historico_movimentacoes):
            data_str = mov['data'].strftime('%d/%m/%Y %H:%M')
            print(f"{data_str:<20} | {mov['produto_codigo']:<15} | {mov['produto_nome']:<30} | {mov['tipo']:<20} | {mov['quantidade_movida']:<10} | {mov['estoque_apos_mov']:<15}")
        print("-" * 120)

    input("\nPressione Enter para voltar ao menu...")
