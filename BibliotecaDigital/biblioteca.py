from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.proximo_id = 1

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = Livro(self.proximo_id,titulo, autor, ano)
        self.livros.append(novo_livro)
        self.proximo_id += 1
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro no acervo.")
        else:
            for livro in self.livros:
                print(livro)

    def buscar_livro(self, termo):
        resultados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]
        if resultados:
            for livro in resultados:
                print(livro)
            else:
                print("Nenhum livro encontrado para o termo de busca.")

    def atualizar_livro(self, id, novo_titulo=None, novo_autor=None, novo_ano=None):
        for livro in self.livros:
            if livro.id == id:
                if novo_titulo:
                    livro.titulo = novo_titulo
                if novo_autor:
                    livro.autor = novo_autor
                if novo_ano:
                    livro.ano = novo_ano
                print("Livro atualizado com exito!")
                return
        print("Livro não encontrado.")

    def remover_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                print("Livro removido com sucesso")
                return
        print("Livro não encontrado")
    
    def emprestar_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                if livro.emprestar():
                    print(f"Livro '{livro.titulo}' emprestado com exito")
                else:
                    print("O livro mencionado ja foi emprestado.")
                return
        print("Livro não encontrado")

    def devolver_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                if livro.devolver():
                    print(f"Livro '{livro.titulo}' devolvido com exito")
                else: 
                    print("O livro já está disponivel")
                return
        print("Livro não encontrado")