# coding: utf-8
import sqlite3

banco = 'EstoqueJogos.db'

def criaBanco():
    conexao = sqlite3.connect(banco)
    comando = '''
    CREATE TABLE Produtos (
    id integer primary key autoincrement,
    nome text,
    plataforma text,
    quantidade integer,
    preco decimal)'''
    try:
        conexao.execute(comando)
        comando = '''
        INSERT INTO Produtos (nome, plataforma, quantidade, preco)
        VALUES ('God of War','PS4', 200, 250.00)'''
        conexao.execute(comando)
        conexao.commit()
    except:
        pass
    conexao.close()

class Banco():

    # Método construtor da class Banco
    def __init__(self):
        criaBanco()
    
    # Método para listar o estoque
    def listaEstoque(self):
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()
        query = '''
        SELECT * FROM Produtos'''
        cursor.execute(query)
        registros = cursor.fetchall()
        cursor.close()
        conexao.close()
        lista_json = list()
        if len(registros) > 0:
            for registro in registros:
                lista_json.append({
                    'id' : registro[0],
                    'nome' : registro[1],
                    'plataforma' : registro[2],
                    'quantidade' : registro[3],
                    'preco' : registro[4]})
            return lista_json
        else:
            return False

    # Método para adicionar produto
    def addItem(self, dados_jogo):
        with sqlite3.connect(banco) as conexao:
            comando = '''
            INSERT INTO Produtos (nome, plataforma, quantidade, preco)
            VALUES (?,?,?,?)'''
            for dado in dados_jogo:
                valor1 = dado['nome']
                valor2 = dado['plataforma']
                valor3 = dado['quantidade']
                valor4 = dado['preco']
                #return list(valor1, valor2, valor3, valor4)
                conexao.execute(comando, (valor1,valor2,valor3,valor4,))
                conexao.commit()

    # Método para adicionar produto
    def getItem(self, id_jogo):
        with sqlite3.connect(banco) as conexao:
            query = '''
            SELECT * FROM Produtos WHERE id = ?'''
            cursor = conexao.cursor()
            cursor.execute(query, (str(id_jogo)))
            registro = cursor.fetchone()
            cursor.close()
            return {
                    "id": registro[0],
                    "nome": registro[1],
                    "plataforma": registro[2],
                    "quantidade": registro[3],
                    "preco": registro[4]}

    # Método para alterar um registro
    def putItem(self, dados_jogo):
        with sqlite3.connect(banco) as conexao:
            cursor = conexao.cursor()
            query = '''
            SELECT * FROM Produtos WHERE id = ?'''
            update = '''
            UPDATE Produtos SET nome = ?, plataforma = ?,
            quantidade = ?, preco = ? WHERE id = ?
            '''
            for dado in dados_jogo:
                cursor.execute(query, (str(dado['id'])))
                registro = cursor.fetchall()
                if len(registro) == 1:
                    v_id = dado['id']
                    v_nome = dado['nome']
                    v_plataforma = dado['plataforma']
                    v_quantidade = dado['quantidade']
                    v_preco = dado['preco']

                    cursor.execute(update, (v_nome, 
                        v_plataforma, v_quantidade,
                        v_preco, v_id,))
                    
                    conexao.commit()
                
            cursor.close()

    # Método para deletar um produto
    def deleteItem(self, dados_jogo):
        with sqlite3.connect(banco) as conexao:
            delete = '''
            DELETE FROM Produtos WHERE id = ? '''

            for dado in dados_jogo:
                v_id = dado['id']
                conexao.execute(delete, (v_id,))
