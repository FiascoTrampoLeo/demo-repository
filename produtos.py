# Lista para armazenar os produtos em memória.
# Cada produto será um dicionário.
produtos = []

def encontrar_produto(codigo):
    """Busca um produto na lista pelo seu código."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

def cadastrar_produto():
    """Função para cadastrar um novo produto."""
    print("\n--- Cadastro de Novo Produto ---")
    
    while True:
        codigo = input("Digite o código do produto: ")
        if encontrar_produto(codigo):
            print("Erro: Já existe um produto com este código. Tente novamente.")
        else:
            break

    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria: ")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    while True:
        try:
            preco = float(input("Digite o preço do produto: R$ "))
            if preco < 0:
                 print("O preço não pode ser negativo.")
                 continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            
    descricao = input("Digite a descrição do produto: ")
    fornecedor = input("Digite o nome do fornecedor: ")

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "descricao": descricao,
        "fornecedor": fornecedor
    }
    
    produtos.append(novo_produto)
    print(f"\nProduto '{nome}' cadastrado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def listar_produtos():
    """Exibe todos os produtos cadastrados."""
    print("\n--- Lista de Produtos Cadastrados ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        input("\nPressione Enter para voltar ao menu...")
        return
        
    for produto in produtos:
        print("-" * 30)
        for chave, valor in produto.items():
            print(f"{chave.capitalize()}: {valor}")
    print("-" * 30)
    input("\nPressione Enter para voltar ao menu...")

