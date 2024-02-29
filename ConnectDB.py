import re
import json
import sys
import requests
from pymongo import MongoClient

#CONEXÃO COM DB ---------------------------------------------------
client = MongoClient("mongodb+srv://desafio-3-maitha:desmaitha3@cluster0.ilamnpu.mongodb.net/")
banco_dados=client["maithatech"]
colecao=banco_dados["desafiocep"]
#CONEXÃO COM DB ---------------------------------------------------

#API CEP + INSERT PARA DB -----------------------------------------
try:
    cep=int(input("Digite seu CEP:"))

    infor= requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    infor= infor.json()


    filtro = { "CEP":infor["cep"] }
    resposta = colecao.find_one(filtro)

    if resposta:
        print("CEP JÁ CADASTRADO NO BANCO DE DADOS!")
        sys.exit()

    else:
        colecao.insert_one({
        "CEP":infor["cep"],
        "logradouro":infor["logradouro"],
        "complemento":infor["complemento"],
        "bairro":infor["bairro"],
        "localidade":infor["localidade"],
        "uf":infor["uf"],
        "ibge":infor["ibge"],
        "ddd":infor["ddd"],
        "siafic":infor["siafi"]
    })
    print("CEP CADASTRADO COM SUCESSO!")
except requests.RequestException as e:
    print("Erro ao tentar fazer cadastro:",e)
    sys.exit()









