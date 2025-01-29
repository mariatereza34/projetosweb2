from flask import *
import dao

app = Flask(__name__)

clientes = [['Tereza', '123'],['Clara','456'],['Renê','789']]

app.secret_key = 'Khggj3h424j23hg44$#'

@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('index.html')

@app.route('/')
def mostrar_pagina_principal():
    return render_template('index.html')

@app.route('/mostrar_pagina_cadastro')
def mostrar_pagina_cadastro():
    return render_template('paginacadastro.html')

@app.route('/menu')
def mostrar_menu():
    return render_template('menu.html')

@app.route('/macbook')
def mostrar_macs():
    return render_template('macbooks.html')

@app.route('/ipads')
def mostrar_ipads():
    return render_template('ipads.html')

@app.route('/iphone')
def mostrar_iphones():
    return render_template('iphones.html')

@app.route('/fazer_login', methods=['POST'])
def fazer_login():
    login_cliente = request.form.get('cliente')
    senha_cliente = request.form.get('senha')

    if dao.login(login_cliente, senha_cliente):
        session['login'] = login_cliente
        return render_template('menu.html')
    else:
        return render_template('index.html')


@app.route('/cadastrarusuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, login, senha):
        msg= 'Usuário inserido com sucesso'
        return render_template('index.html', texto=msg)
    else:
        msg = 'Erro ao inserir usuário'
        return render_template('index.html', texto=msg)

@app.route('/mostrar_avaliacoes')
def mostrar_avaliacao():
    return render_template('avaliacoes.html')

@app.route('/mostrar_comentarios')
def mostrar_comentario():
    return render_template('comentario.html')

@app.route('/listarprodutos')
def listar_produtos():
    if 'login' in session:

        produtos = dao.listar_produtos()
        return render_template('listarprodutos.html', lista=produtos)
    else:
        return render_template('index.html')

@app.route('/cadastroproduto')
def pag_cadas_prod():
    return render_template('/cadastrarprodutos.html')

@app.route('/cadastrarprodutos', methods=['POST','GET'])
def cadastrar_produto():
    tipo = request.form.get('tipo')
    cor = request.form.get('cor')
    gb = request.form.get('gb')
    print(tipo,cor,gb)
    if dao.inserir_produto(tipo,cor,gb):
        msg= 'Produto inserido com sucesso'
        return render_template('menu.html', textoo=msg)
    else:
        msg = 'Erro ao inserir produto'
        return render_template('menu.html', textoo=msg)



if __name__ == '__main__':
    app.run(debug=True)

