from produtos import cadastrar_produto, listar_produtos, produtos
from estoque import adicionar_estoque, remover_estoque, atualizar_estoque, verificar_estoque_baixo
from vendas import registrar_venda, vendas
from relatorios import relatorio_vendas, relatorio_estoque, relatorio_historico_movimentacoes
import os

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clr()
    while True:
        print("\n===== GERENCIADOR DE LOJA =====")
        print("\n--- PRODUTOS E ESTOQUE ---")
        print("\n1. Cadastrar Produto")
        print("2. Adicionar ao Estoque (Entrada)")
        print("3. Remover do Estoque (Saída Manual)")
        print("4. Atualizar Estoque (Ajuste)")
        print("5. Listar Todos os Produtos")
        
        print("\n--- VENDAS ---")
        print("\n6. Registrar Venda")
        
        print("\n--- RELATÓRIOS ---")
        print("\n7. Relatório de Estoque Atual")
        print("8. Relatório de Vendas")
        print("9. Histórico de Movimentações de Estoque")
        print("10. Alerta de Estoque Baixo")
        
        print("\n--- SISTEMA ---")
        print("11. Sair\n")
        print("="*31)
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            clr()
            cadastrar_produto()
        elif opcao == '2':
            clr()
            adicionar_estoque()
        elif opcao == '3':
            clr()
            remover_estoque()
        elif opcao == '4':
            clr()
            atualizar_estoque()
        elif opcao == '5':
            clr()
            listar_produtos()
        elif opcao == '6':
            clr()
            registrar_venda()
        elif opcao == '7':
            clr()
            relatorio_estoque(produtos)
        elif opcao == '8':
            clr()
            relatorio_vendas(vendas)
        elif opcao == '9':
            clr()
            relatorio_historico_movimentacoes()
        elif opcao == '10':
            clr()
            verificar_estoque_baixo()
        elif opcao == '11':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
