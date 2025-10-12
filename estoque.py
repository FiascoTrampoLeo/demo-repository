from produtos import encontrar_produto, produtos
from relatorios import registrar_movimentacao

NIVEL_MINIMO_ESTOQUE = 10

def adicionar_estoque():
    """Adiciona uma quantidade ao estoque de um produto existente e registra a movimentação."""
    print("\n---=@ Adicionar ao Estoque @=---")
    codigo = input("Digite o código do produto para adicionar ao estoque: ")
    
    produto = encontrar_produto(codigo)
    
    if produto:
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade a ser adicionada ao estoque do produto '{produto['nome']}': "))
                if quantidade > 0:
                    produto["quantidade"] += quantidade
                    # Registra a movimentação de entrada
                    registrar_movimentacao(produto, quantidade, "Entrada Manual")
                    print(f"\n{quantidade} unidades adicionadas. Novo estoque: {produto['quantidade']}.")
                    break
                else:
                    print("A quantidade deve ser um número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        print("Produto não encontrado.")
    input("\nPressione Enter para voltar ao menu...")

def remover_estoque():
    """Remove uma quantidade do estoque de um produto (ajuste manual) e registra a movimentação."""
    print("\n---=@ Remover do Estoque (Ajuste Manual) @=---")
    codigo = input("Digite o código do produto para remover do estoque: ")
    
    produto = encontrar_produto(codigo)

    if produto:
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade a ser removida do estoque de '{produto['nome']}': "))
                if quantidade <= 0:
                    print("A quantidade deve ser um número positivo.")
                elif quantidade > produto["quantidade"]:
                    print(f"Erro: Quantidade a ser removida ({quantidade}) é maior que o estoque atual ({produto['quantidade']}).")
                else:
                    produto["quantidade"] -= quantidade
                    # Registra a movimentação de saída
                    registrar_movimentacao(produto, quantidade, "Saída Manual")
                    print(f"\n{quantidade} unidades removidas. Novo estoque: {produto['quantidade']}.")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        print("Produto não encontrado.")
    input("\nPressione Enter para voltar ao menu...")


def atualizar_estoque():
    """Permite ajustar manualmente a quantidade total de produtos (inventário) e registra a movimentação"""
    print("\n--- Atualização Manual de Estoque (Ajuste de Inventário) ---")
    codigo = input("Digite o código do produto para atualizar o estoque: ")

    produto = encontrar_produto(codigo)
    
    if produto:
        quantidade_antiga = produto["quantidade"]
        while True:
            try:
                nova_quantidade = int(input(f"Digite a nova quantidade total para o produto '{produto['nome']}': "))
                if nova_quantidade >= 0:
                    produto["quantidade"] = nova_quantidade
                    
                    # Calcula a diferença para registrar a movimentação correspondente
                    diferenca = nova_quantidade - quantidade_antiga
                    if diferenca != 0:
                        # Define o tipo de movimentação com base na diferença
                        tipo_mov = "Ajuste de Entrada" if diferenca > 0 else "Ajuste de Saída"
                        registrar_movimentacao(produto, abs(diferenca), tipo_mov)

                    print(f"\nEstoque atualizado com sucesso. Nova quantidade: {produto['quantidade']}.")
                    break
                else:
                    print("A quantidade não pode ser um número negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        print("Produto não encontrado.")
    input("\nPressione Enter para voltar ao menu...")

def verificar_estoque_baixo():
    """Verifica e exibe produtos com estoque abaixo do nível mínimo definido."""
    print("\n--- Alerta de Estoque Baixo ---")
    print(f"(Nível mínimo definido: {NIVEL_MINIMO_ESTOQUE} unidades)")
    
    encontrou_produto = False
    for produto in produtos:
        if produto["quantidade"] < NIVEL_MINIMO_ESTOQUE:
            print(f"ALERTA: O produto '{produto['nome']}' (Cód: {produto['codigo']}) está com estoque baixo: {produto['quantidade']} unidades.")
            encontrou_produto = True
            
    if not encontrou_produto:
        print("Nenhum produto com estoque baixo encontrado.")
    input("\nPressione Enter para voltar ao menu...")
