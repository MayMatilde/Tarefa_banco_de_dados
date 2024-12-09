from livroDAO.livro_autor import AutorDAO
from livroModel.model import *

class AutoresRepository:
    def __init__(self, dao: AutorDAO ):
        self.dao = dao

    def adicionar_Autores(self, nome, data_nascimento, nacionalidade):
        Autor = Autores(self, nome=nome, data_nascimento=data_nascimento, nacionalidade=nacionalidade)
        return self.dao.adicionar(Autor)

    def listar_Autores(self):
        return self.dao.listar()

    def deletar_Autores(self, id):
        return self.dao.deletar(id)

    def atualizar_Autores(self, Autor):
        return self.dao.atualizar(Autor)
