from produtos import cadastrar_produto, listar_produtos
from estoque import (
    adicionar_estoque, 
    remover_estoque, 
    atualizar_estoque, 
    verificar_estoque_baixo
)

def main():
    """Função principal que exibe o menu e gerencia as ações do usuário."""
    while True:
        print("\n===== GERENCIADOR DE LOJA =====")
        print("1. Cadastrar Produto")
        print("2. Adicionar ao Estoque")
        print("3. Remover do Estoque")
        print("4. Atualizar Estoque Manualmente")
        print("5. Alerta de Estoque Baixo")
        print("6. Listar Todos os Produtos")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            adicionar_estoque()
        elif opcao == '3':
            remover_estoque()
        elif opcao == '4':
            atualizar_estoque()
        elif opcao == '5':
            verificar_estoque_baixo()
        elif opcao == '6':
            listar_produtos()
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
