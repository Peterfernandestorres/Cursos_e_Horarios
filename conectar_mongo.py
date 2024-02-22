from pymongo import MongoClient as mc
 
client = mc("mongodb://root:808@127.0.0.1:37452")
 
db = client.loja_db


# for us in db["usuario"].find():
    # print(us)

"""Estamos Obetendo Dados que estão cadastrados na tabela (coleção) do usuario, usando db[""]find()"""
#O comando Find Localiza os dados e retorna com todos eles para a variavel us.
"""Depois Fazemos a leitura de todas as linhas com o For e exibimos na tela"""

# usuario_id = db["usuario"].insert_one({"nomeusuario:","carlos","senha:","123","nivel:","usuario"}).inserted_id
# print (usuario_id)

#rs = db["usuario"].find_one ({"nivel":"usuario"})
#print (rs)

#for rs in db["usuario"].find_one({"nivel":"usuario"}):
#    print (rs)

for rs in db["usuario"].find({"nivel":"usuario"}):
        print (rs)