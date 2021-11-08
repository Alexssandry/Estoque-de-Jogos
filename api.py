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
    return 'Estou sendo executado de uma BluePrint'

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
