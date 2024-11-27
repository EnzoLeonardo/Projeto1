class Menu:
    @staticmethod
    def exibir():
        print("\n--- Biblioteca Digital ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Atualizar Livro")
        print("5. REmover Livro")
        print("6. Emprestar Livro")
        print("7. Devolver Livro")
        print("0. Sair")
        return input("Escolha uma opção: ")