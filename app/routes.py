from app import app
from flask import render_template
from flask import request
import json
import requests
link = "https://flasktintpedroa-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="pagina inical")


@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="contatos")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="cadastros")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data= json.dumps(dados))
        return 'cadastrado com sucesso!'

    except Exception as e:
        return f'ocorreu um erro\n +{e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'algo deu errado \n {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave  == '123123':
               idCadastro = codigo
               return idCadastro
    except Exception as e:
        return f'algo deu errado \n {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"joão"}
        requisição = requests.patch(f'{link}/cadastro/-O8mjWhT1RuyBD9C0-gZ/.json', data=json.dumps(dados))
        return f'atualizado com sucesso!'
    except Exception as e:
        return f'algo deu errado'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8mjWhT1RuyBD9C0-gZ/.json')
        return f'excluido com sucesso!'

    except Exception as e:
        return f'algo deu errado'