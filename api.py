# coding: utf-8
from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import request
from banco import Banco

BlueP_API = Blueprint('api', __name__)
banco = Banco()

@BlueP_API.route('/')
def principal():
    return '''
    Estoque de Jogos
<br>
Utilize nas rotas /get /add /put /del
<br><br>
/get : retorna um JSON com os dados do estoque <br>
/get/"valor de ID" : procura um jogo pelo numero de ID na url e retorna um JSON<br>
<br><br>

/add <br>
Rota para adicionar novo jogo recebido via (POST) <br>
Modelo do JSON: <br>
[ <br>
{ <br>
    "nome" : "nome_jogo", <br>
    "plataforma" : "console", <br>
    "quantidade" : 100, <br>
    "preco" : 130.90 <br>
} <br>
] <br>

<br><br>
/put <br>
Rota para alterar os dados de um jogo (PUT) <br>
modelo para JSON <br>
[ <br>
{ <br>
    "id" : 1, <br>
    "nome" : "nome_jogo", <br>
    "plataforma" : "console", <br>
    "quantidade" : 100, <br>
    "preco" : 130.90 <br>
}, <br>
{ <br>
    # outro produto <br>
} <br>
] <br>
<br><br>

/del <br>
Rota para remover um jogo via (DELETE) <br>
Modelo do JSON: <br>
[ <br>
{ <br>

    "id" : 1 <br>
}, <br>
{ <br>

    "id" : 2 <br>
} <br>
] <br>

<br><br>

'''

@BlueP_API.route('/get', methods=['GET'])
def exibeEstoque():
    retorno = banco.listaEstoque()
    if retorno:
        return jsonify({'Estoque' : retorno})
    return make_response(jsonify({'Estoque' : 'Vazio!'}))

@BlueP_API.route('/add', methods=['POST'])
def addItemEstoque():
    if request.method == 'POST':
        if request.json:
            banco.addItem(request.json)
            return make_response(jsonify({'Estoque' : 'Sucesso!'}))
        else:
            return make_response(jsonify({'Estoque' : 'Falhou!'}))

@BlueP_API.route('/get/<int:id_jogo>', methods=['GET'])
def getItemEstoque(id_jogo = None):
    if id_jogo != None:
        item = banco.getItem(id_jogo)
        return jsonify({'Produto': item})

@BlueP_API.route('/put', methods=['PUT'])
def putItemEstoque():
    if request.method == 'PUT':
        if request.json:
            banco.putItem(request.json)
            return make_response(jsonify({'Estoque':'Sucesso!'}))
        else:
            return make_response(jsonify({'Estoque':'Falhou!'}))

@BlueP_API.route('/del', methods=['DELETE'])
def deleteItemEstoque():
    if request.method == 'DELETE':
        if request.json:
            banco.deleteItem(request.json)
            return make_response(jsonify({'Estoque':'Sucesso!'}))
        else:
            return make_response(jsonify({'Estoque':'Falho!'}))
