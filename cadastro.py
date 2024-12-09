from livroDAO.livro_categoria import CategoriaDAO
from livroModel.model import *

class CategoriaRepository:
    def __init__(self, dao: CategoriaDAO ):
        self.dao = dao

    def adicionar_Cadastro(self, nome, data_nascimento, nacionalidade):
        categoria = Categorias(self, nome=nome, data_nascimento=data_nascimento, nacionalidade=nacionalidade)
        return self.dao.adicionar(categoria)

    def listar_Cadastro(self):
        return self.dao.listar()

    def deletar_Cadastro(self, id):
        return self.dao.deletar(id)

    def atualizar_Cadastro(self, cadastro):
        return self.dao.atualizar(cadastro)
