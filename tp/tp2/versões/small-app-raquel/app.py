from flask import Flask, render_template, request, redirect
import requests
import json

import db_relatorios

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/relatorios', methods=['GET'])
def get_relatorios():
    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)
    print(ps)

    return render_template('relatorios_view.html', relatorios=ps)



@app.route('/relatorios', methods=['POST'])
def post_relatorio():
    data = dict(request.form)
    print(data)
    requests.post('http://localhost:5000/api/relatorios', data=data)


    return redirect('http://localhost:5000/relatorios')



@app.route('/relatorios/<relatorio>', methods=['GET'])
def get_relatorio(relatorio):
    res = requests.get('http://localhost:5000/api/relatorios/' + relatorio)

    p = json.loads(res.content)
    return render_template('relatorio_view.html', p=p)




# API
@app.route('/api/relatorios', methods=['GET'])
def api_get_relatorios():
    ps = db_relatorios.find_all()
    return json.dumps(ps)


@app.route('/api/relatorios', methods=['POST'])
def api_post_relatorio():
    
    data = dict(request.form)
    db_relatorios.insert(data)

    return json.dumps(db_relatorios.find_all())


@app.route('/api/relatorios/<relatorio>', methods=['GET'])
def api_get_relatorio(relatorio):
    p = db_relatorios.find_one(relatorio)
    return json.dumps(p)

# Pessoas
@app.route('/pessoas', methods=['GET'])
def get_pessoas():

    res = requests.get('http://localhost:5000/api/pessoas')
    ps = json.loads(res.content)
    return render_template('pessoas_view.html', title='Pessoas', pessoas=ps)


@app.route('/pessoas/<numero>', methods=['GET'])
def get_pessoa(numero):

    res = requests.get('http://localhost:5000/api/pessoas/%s' % numero)
    p = json.loads(res.content)
    return render_template('pessoa_view.html', pessoa=p)



import db_pessoas

# API
@app.route('/api/pessoas', methods=['GET'])
def api_get_pessoas():

    ps = db_pessoas.find_all()

    return json.dumps(ps)



@app.route('/api/pessoas/<numero>', methods=['GET'])
def api_get_pessoa(numero):

    d = pessoas[numero]
    d['numero'] = numero
    
    return json.dumps(d)


@app.route('/api/pessoas', methods=['POST'])
def api_post_pessoa():

    data = dict(request.form)
    db_pessoas.insert(data)

    return data








