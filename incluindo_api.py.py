import re
import json
import requests
import sys

cep=int(input("Digite seu CEP: "))

infor= requests.get(f"https://viacep.com.br/ws/{cep}/json/")
infor= infor.json()
print("cep: ",infor["cep"])
print("logradouro: ",infor["logradouro"])
print("complemento: ",infor["complemento"])
print("bairro: ",infor["bairro"])
print("localidade: ",infor["localidade"])
print("uf: ",infor["uf"])
print("ibge: ",infor["ibge"])
print("ddd: ",infor["ddd"])
print("siafi: ",infor["siafi"])