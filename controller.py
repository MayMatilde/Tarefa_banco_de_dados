from flask import render_template, request, Blueprint, redirect, url_for
from datetime import datetime
from Repository_Pattern.database import db
from livroModel.model import Livros, Autores, Categorias
from livroDAO.livro_dao import LivroDAO
from livroDAO.livro_autor import AutorDAO
from livroDAO.livro_categoria import CategoriaDAO
from Repository_Pattern.autor import AutoresRepository
from Repository_Pattern.cadastro import CategoriaRepository
from Repository_Pattern.livro import LivrosRepository  

livro_dao = LivroDAO(db.session)
livro_autor_dao = AutorDAO(db.session)
livro_categoria_dao = CategoriaDAO(db.session)


livro = LivrosRepository(db.session)
autor = AutoresRepository(db.session)
cadastro = CategoriaRepository(db.session)

books = Blueprint('books', __name__)

@books.route('/')
def index():
    return render_template('index.html')

@books.route('/acessoAutor', methods=['GET', 'POST'])
def acessoAutor():
    if request.method == 'GET':
        return render_template('acessoAutor.html')
    
    elif request.method == 'POST':
        nome_autor = request.form['nome_autor']
        data_nascimento = datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d').date() #verifica a data certinho
        nacionalidade = request.form['nacionalidade']  

        
        autor = AutorDAO.buscar_nome(nome_autor)
        if not autor:
            autor = Autores(
                nome=nome_autor,
                data_nascimento=data_nascimento,
                nacionalidade=nacionalidade
            )
            AutoresRepository.adicionar_Autores(autor)

        return redirect(url_for('books.acesso')) 

@books.route('/acesso', methods=['GET', 'POST'])
def acesso():
    if request.method == 'GET':
        return render_template('acesso.html')
    
    elif request.method == 'POST':
        titulo = request.form['titulo']
        isbn = request.form['isbn']
        data_publi = datetime.strptime(request.form['data_publi'], '%Y-%m-%d').date()
        numero_paginas = request.form['numero_paginas']
        autor_nome = request.form['autor']
        nome_categorias = request.form['categoria']

        #limpa as categorias e as transforma em uma lista
        nome_categorias = [c.strip() for c in nome_categorias.split(',')]

        autor = AutorDAO.buscar_nome(autor_nome)
        if not autor:
            autor = Autores(nome=autor_nome)
            AutoresRepository.adicionar_Autores(autor)

        categorias = []
        for nome in nome_categorias:
            categoria = AutoresRepository.buscar_nome(nome)
            if not categoria:
                categoria = Categorias(nome=nome.strip())
                AutoresRepository.adicionar_Autores(categoria)
            categorias.append(categoria)

        livro = Livros(
            titulo=titulo, 
            isbn=isbn,
            data_publi=data_publi,
            numero_paginas=numero_paginas,
            autor=autor
        )

        livro.categorias = categorias  
        LivrosRepository.adicionar_Livro(livro)  

        return redirect(url_for('books.lista'))  

@books.route('/lista')
def lista():
    info = LivrosRepository.listar()  
    return render_template('lista.html', info=info)

@books.route('/deletar/<int:id>')
def deletar(id):
    LivrosRepository.deletar_Livros(id)  
    return redirect(url_for('books.lista'))  
