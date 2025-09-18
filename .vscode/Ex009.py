from flask import Flask, request, jsonify

import json

app = Flask(__name__)

#Rota GET

#cria uma rota mensagem que responde as requisições de GET

@app.route('/mensagem', methods=['GET'])
def mensagem():
    return jsonify({"mensagem": "Olá, mundo!"})

#Rota POST

#cria uma rota soma que responde as requisições de POST

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()  # Espera um JSON no corpo da requisição
    a = dados.get('a', 0)
    b = dados.get('b', 0)
    resultado = a + b
    return jsonify({"resultado": resultado})

bancodedados = r"C:\Users\mahta\Desktop\Prog\.vscode\bancodedados.json"

@app.route('/cadastro', methods=['POST'])
def cadastro():
     dados = request.get_json() 
     nome = dados.get("nome")
     email = dados.get("email")
     novocadastro = {"nome": nome, "email": email}
     with open(bancodedados, 'r') as arquivo:
                dados_existentes = json.load(arquivo)
     dados_existentes.append(novocadastro)
     with open(bancodedados, 'w') as arquivo:
            json.dump(dados_existentes, arquivo, indent=4)
     return jsonify({"resultado": "cadastro criado"}),201
     

if __name__ == "__main__":
    app.run()



#/mensagem (GET): retorna uma mensagem fixa.
#/soma (POST): recebe dois números em JSON, soma e retorna o resultado.