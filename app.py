from  flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import json
import os 

app = Flask(__name__)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

pasta = 'files'
caminho_arquivo = os.path.join(pasta, 'usuarios.json')



@app.route('/usuario',methods=['GET'])
def obterUsuarios():
    return jsonify(lerArquivo())

@app.route('/usuario',methods=['POST'])
def criarUsuario():
    usuarios = lerArquivo()
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4) 
    return jsonify(novo_usuario)

def lerArquivo():
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    else:
        return []

app.run(port=5000,host='localhost')