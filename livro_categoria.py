from sqlalchemy.orm import Session
from livroModel.model import Categorias

class CategoriaDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar(self, categoria: Categorias):
        self.db_session.add(categoria)
        self.db_session.commit()

    def buscar_nome(self, nome: str):
        return self.db_session.query(Categorias).filter_by(nome=nome).first()
    

    def listar_autores(self):
        return self.db_session.query(Categorias).all
