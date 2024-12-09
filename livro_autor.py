from sqlalchemy.orm import Session
from livroModel.model import Autores

class AutorDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar(self, autor: Autores):
        self.db_session.add(autor)
        self.db_session.commit()

    def buscar_nome(self, nome: str):
        return self.db_session.query(Autores).filter_by(nome=nome).first()
    

    def listar_autores(self):
        return self.db_session.query(Autores).all
