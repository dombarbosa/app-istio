from flask import Flask, redirect, jsonify
import os

app = Flask(__name__)

@app.route('/')
def mainroute(): 
    return jsonify({'Status': 'UP', 'Aviso': 'Utilize a rota /forward para teste'})

@app.route('/forward', methods=['GET'])
def access_forward():
    env_access_forward = os.environ.get('ENV_FORWARD')
    env_dst_request = os.environ.get('ENV_DST_REQUEST')
    env_my_context_path = os.environ.get('ENV_MY_CONTEXT_PATH')
    
    if env_my_context_path == "":
        return jsonify({"Message": "Sem context path"})
    if env_access_forward.lower() == "true":
        return redirect(env_dst_request)
    else:
        return jsonify({"Message": "Variável vazia ou não informada. Altere a variável para executar novos testes"}),200

