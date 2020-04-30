# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import json
import requests
import string
import hashlib

api_url_base = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=TOKEN'
alfabeto = string.ascii_lowercase
resultado = ''
response = requests.get(api_url_base)
response_json = response.json()

numero_casas = response_json['numero_casas']
response_array = list(response_json['cifrado'].lower())

def fraseCifrada(arquivo):                      #Função que cria o arquivo Json
    with open('answer.json', 'w') as write:
        json.dump(arquivo, write)

fraseCifrada(response_json)

for letra in response_array:
    if letra in string.whitespace: #Verifica se há espaços em branco e inclui sem modificação
        resultado = resultado + letra
    elif letra in string.digits:   #Verifica se há dígitos e inclui sem modificação
        resultado = resultado + letra
    elif letra in string.punctuation: #Verifica se há pontuação e inclui sem modificação
        resultado = resultado + letra
    elif letra in alfabeto:             #faz a decriptografia
        posicao = alfabeto.find(letra)
        posicao = (posicao - numero_casas) % 26
        resultado = resultado + alfabeto[posicao]

response_json['decifrado'] = resultado
response_json['resumo_criptografico'] = hashlib.sha1(resultado.encode('utf-8')).hexdigest()

def fraseDecifrada(arquivo):                      #Função que cria o arquivo Json
    with open('answer.json', 'w') as write:
        json.dump(arquivo, write)

fraseDecifrada(response_json)

r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=TOKEN', files={"answer": open("answer.json", "rb")})
