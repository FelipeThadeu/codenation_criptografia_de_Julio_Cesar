# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import json
import requests
import string

alfabeto = string.ascii_lowercase

resultado = ''
response_json = {"numero_casas": 4, "token": "006302976f90a5a0dc663f235e93a5e43bb73182", "cifrado": " 1.0 AMXLSYX viuymviqirxw sv hiwmkr, tvskveqqmrk mw xli evx sj ehhmrk fykw xs er iqtxc \"xibx\" jmpi. psymw wvckpic", "decifrado": "without requirements or design programming is the art of adding bugs to an empty text file louis srygley"}

numero_casas = response_json['numero_casas']
response_array = list(response_json['cifrado'].lower())

def fraseCifrada(arquivo):
    with open('answer-test.json', 'w') as write:
        json.dump(arquivo, write)

fraseCifrada(response_json)

for letra in response_array:
    if letra in string.whitespace:
        resultado = resultado + letra
    elif letra in string.digits:
        resultado = resultado + letra
    elif letra in string.punctuation:
        resultado = resultado + letra
    elif letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao - numero_casas) % 26
        resultado = resultado + alfabeto[posicao]

response_json['decifrado'] = resultado

def fraseDecifrada(arquivo):
    with open('frase_cifrada.json', 'w') as write:
        json.dump(arquivo, write)

fraseCifrada(response_json)