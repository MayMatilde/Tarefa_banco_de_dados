from Repository_Pattern.database import db


class Livros(db.Model):
    __tablename__ = 'Tabela_de_livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(40), nullable=False)
    isbn = db.Column(db.Integer, nullable=False, unique=True)
    data_publi = db.Column(db.Date(), nullable=False)
    numero_paginas = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categorias.id'))

    autor = db.relationship('Autores', back_populates='livros')
    categorias = db.relationship('Categorias', back_populates='livros')

class Autores(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    data_nascimento = db.Column(db.Date())
    nacionalidade = db.Column(db.String(40), nullable=False)

    livros = db.relationship('Livros', back_populates='autor')

class Categorias(db.Model):
    __tablename__ = 'Categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)

    livros = db.relationship('Livros', back_populates='categorias')
