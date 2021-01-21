from flask import Flask, render_template, request, redirect
import json
import requests
from re import *
from povoamento import relatorios, pessoas
import db

app = Flask(__name__)

for relatorio in relatorios:
    db.insert(relatorio)

for pessoa in pessoas:
    db.insert_p(pessoa)

@app.route('/')
def index():
    ps = db.find_all()
    pessoas = db.find_all_p()
    h = []
    for titulo in ps:
        relatorio = db.find_one(titulo)
        for tag in relatorio['hashtags']:
            if tag not in h:
                h.append(tag)
    return render_template('index.html', titles=ps, hashtags=h, pessoas=pessoas)

@app.route('/relatorios', methods=['GET'])
def get_relatorios():
    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)
    return render_template('relatorios_view.html', title='Relatórios', relatorios=ps)

@app.route('/relatorios', methods=['POST'])
def post_relatorio():
    data = dict(request.form)
    requests.post('http://localhost:5000/api/relatorios', data=data)
    return redirect('http://localhost:5000/relatorios')

@app.route('/relatorios/<titulo>', methods=['GET'])
def get_relatorio(titulo):
    res = requests.get('http://localhost:5000/api/relatorios/' + titulo)
    p = json.loads(res.content)

    return render_template('relatorio_view.html', p=p)

@app.route('/relatorios/procura')
def procura_view():
    return render_template('procura_view.html')

@app.route('/pessoas/<nome>', methods=['GET'])
def get_pessoa(nome):
    res = requests.get('http://localhost:5000/api/pessoas/' + nome)
    p = json.loads(res.content)
    return render_template('pessoa_view.html', p=p)

@app.route('/relatorios/resultado', methods=['POST'])
def relatorios_resultado():
    pesquisa = request.form.get('procura').replace('#','')
    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)

    l = []
    t = []
    for titulo in ps:
        relatorio = db.find_one(titulo)
        text = relatorio['description']
        res = findall(rf"(?i)\b{pesquisa}\b",str(text))
        if res:
            if titulo not in l:
                l.append(titulo)
                pos = text.index(res[0])
                if (len(text) >= 500):
                    t.append(text[pos:pos+len(res[0])+500].replace(res[0],'*'+res[0]+'*'))
                else:
                    t.append(text.replace(res[0],'*'+res[0]+'*'))
    return render_template('resultados_pesquisa_view.html', title=rf'Relatórios que contêm o padrão"{pesquisa}"', relatorios=l, i=)

# api para relatorios

@app.route('/api/relatorios', methods=['GET'])
def api_get_relatorios():
    ps = db.find_all()
    return json.dumps(ps)

@app.route('/api/relatorios', methods=['POST'])
def api_post_relatorio():
    data = dict(request.form)

    h = data['hashtags'].split(' ')
    l = data['references'].split(' ')

    data['references'] = l
    data['hashtags'] = h
    data['authors'] = [{'name': 'Bruno Rebelo Lopes', 'number': '57768'},{'name':'Morgana Sacramento Ferreira','number':'93779'},{'name':'Luís Pedro da Silva Pinto','number':'83016'}]

    db.insert(data)

    return json.dumps(db.find_all())

@app.route('/api/relatorios/<titulo>', methods=['GET'])
def api_get_relatorio(titulo):
    p = db.find_one(titulo)
    return json.dumps(p)

# api para autores
@app.route('/api/pessoas', methods=['GET'])
def api_get_pessoas():
    ps = db.find_all_p()
    return json.dumps(ps)
@app.route('/api/pessoas/<nome>', methods=['GET'])
def api_get_pessoas(nome):
    p = db.find_one_p(nome)
    return json.dumps(p)
