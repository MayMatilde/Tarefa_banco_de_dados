from livroDAO.livro_dao import LivroDAO
from livroModel.model import *

class LivrosRepository:
    def __init__(self, dao: LivroDAO):
        self.dao = dao

    def adicionar_Livros(self, titulo, isbn, data_publicacao, numero_paginas, autor_id, categoria_id):
        Livros = Livros(titulo=titulo, isbn=isbn, data_publicacao=data_publicacao, numero_paginas=numero_paginas, autor_id=autor_id, categoria_id=categoria_id)
        return self.dao.adicionar(Livros)

    def listar_Livros(self):
        return self.dao.listar()

    def deletar_Livros(self, id):
        return self.dao.deletar(id)

    def atualizar_Livros(self, Livros):
        return self.dao.atualizar(Livros)
