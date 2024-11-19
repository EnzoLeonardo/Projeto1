class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestados"
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano} | Status {status}"

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False