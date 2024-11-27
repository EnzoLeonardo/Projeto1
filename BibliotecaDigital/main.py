from biblioteca import Biblioteca
from menu import Menu

def main():
    biblioteca = Biblioteca()

    while True:
        opcao = Menu.exibir()

        if opcao == '1':
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            biblioteca.adicionar_livro(titulo, autor, ano)
        elif opcao == '2':
            biblioteca.listar_livros()
        elif opcao == '3':
            termo = input("Termo de busca: ")
            biblioteca.buscar_livro(termo)
        elif opcao == '4':
            id = int(input("ID do livro a atualizar: "))
            novo_titulo = input("Novo título (deixe vazio para manter o atual): ") or None
            novo_autor = input("Novo autor (deixe vazio para manter o atual): ") or None
            novo_ano = input("Novo ano (deixe vazio para manter o atual): ") or None
            biblioteca.atualizar_livro(id, novo_titulo, novo_autor, novo_ano)
        elif opcao == '5':
            id = int(input("ID do livro a remover: "))
            biblioteca.remover_livro(id)
        elif opcao == '6':
            id = int(input("ID do livro para emprestar: "))
            biblioteca.emprestar_livro(id)
        elif opcao == '7':
            id = int(input("ID do livro para devolver: "))
            biblioteca.devolver_livro(id)
        elif opcao == '0':
            print("Encerrando o sistema de biblioteca...")
            break
        else:
            print("Opção inválida. Tente Novamente.")

if __name__ == "__main__":
    main()
    