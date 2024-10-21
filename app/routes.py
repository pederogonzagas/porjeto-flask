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
        dados = {"cpf": cpf, "nome": nome, "telefone": telefone, "endereco": endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data=json.dumps(dados))
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
            if chave == 'dadsd':
                idCadastro = codigo
                return idCadastro
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'




@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8mjWhT1RuyBD9C0-gZ/.json')
        return f'excluido com sucesso!'

    except Exception as e:
        return f'algo deu errado'

@app.route('/atualizar', methods = ['GET', 'POST'])
def atualizar():
    if request.method == 'GET':
        return render_template('atualizar.html', titulo="Atualizar Usuário")

    if request.method == 'POST':
        try:
            cpf = request.form.get("cpf")
            novo_nome = request.form.get("nome")
            novo_telefone = request.form.get("telefone")
            novo_endereco = request.form.get("endereco")

            requisicao = requests.get(f'{link}/cadastro/.json')
            dicionario = requisicao.json()

            idCadastro = None
            for codigo in dicionario:
                    if dicionario[codigo]['cpf'] == cpf:
                        idCadastro = codigo
                        break
            if not idCadastro:
                return f" CPF {cpf} não encontrado.",

            dados_atualizados = {
                "nome": novo_nome,
                 "telefone": novo_telefone,
                 "endereco": novo_endereco
            }
            requisicao_atualizacao = requests.patch(f'{link}/cadastro/{idCadastro}.json', data=json.dumps(dados_atualizados))

            if requisicao_atualizacao.status_code == 0:
                return"Atualizado com sucesso!"
            else:
                return f"Erro ao atualizar: {requisicao_atualizacao.text}"

        except Exception as e:
            return f"Algo deu errado: {e}"



