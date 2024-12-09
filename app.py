from flask import Flask
from livroController.controller import books
from Repository_Pattern.database import db
from Repository_Pattern.cadastro import *
from Repository_Pattern.autor import *
from Repository_Pattern.livro import *
from livroModel.model import *
from livroDAO.livro_autor import AutorDAO
from livroDAO.livro_dao import LivroDAO
from livroDAO.livro_categoria import CategoriaDAO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(books)

livro_dao = LivroDAO(db.session)
livro_autor = AutorDAO(db.session)
livro_categoria = CategoriaDAO(db.session)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
