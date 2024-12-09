from sqlalchemy.orm import Session
from livroModel.model import Livros
from livroController.controller import *

class LivroDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def adicionar(self, livro: Livros):
        self.db_session.add(livro)
        self.db_session.commit()
        return livro

    def buscar_id(self, id: int):
        return self.db_session.query(Livros).filter_by(id=id).first()

    def listar(self):
        return self.db_session.query(Livros).all()
    
    
    def deletar(self, id: int):
        livro = self.buscar_id(id)
        if livro:
            self.db_session.delete(livro)
            self.db_session.commit()        
            return True
        return False  
            
    def atualizar(self, livro: Livros):
        self.db_session.merge(livro)
        self.db_session.commit()

 
