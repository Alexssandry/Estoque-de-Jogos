# Estoque-de-Jogos
CRUD via HTTP

# Para iniciar utilize os comandos abaixo
# Version do python usada 3.8.2

source venv/bin/activate

python app.py


# Para interagir

Estoque de Jogos
Utilize nas rotas /get /add /put /del

/get : retorna um JSON com os dados do estoque
/get/"valor de ID" : procura um jogo pelo numero <br> de ID na url e retorna um JSON


/add
Rota para adicionar novo jogo recebido via (POST)
Modelo do JSON:
[
{
"nome" : "nome_jogo",
"plataforma" : "console",
"quantidade" : 100,
"preco" : 130.90
}
]


/put
Rota para alterar os dados de um jogo (PUT)
modelo para JSON
[
{
"id" : 1,
"nome" : "nome_jogo",
"plataforma" : "console",
"quantidade" : 100,
"preco" : 130.90
},
{
# outro produto
}
]


/del
Rota para remover um jogo via (DELETE)
Modelo do JSON:
[
{
"id" : 1
},
{
"id" : 2
}
] 
