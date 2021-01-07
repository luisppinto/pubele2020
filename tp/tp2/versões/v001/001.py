from flask import Flask, render_template, request
import json
import requests
import random
import shelve
from bd import relatorios

app = Flask(__name__)

s = shelve.open('relatorios.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/relatorios')
def api_relatorios():
    ps = list(s.keys())
    return json.dumps(ps)

@app.route('/relatorios')
def relatorios_view():

    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)

    return render_template('relatorios_view.html', title='Proverbios', relatorios=ps)

@app.route('/relatorios/novo', methods=['POST'])
def processamento_ficheiro():
    

def relatorios_novo():

    title = request.form.get('title')
    signi = request.form.get('autores')

    s[title] = signi
    s.sync()
    ps = list(s.keys())

    return render_template('relatorios_view.html', title='Relatorios', relatorios=ps)



@app.route('/relatorios/proverbio/<id_>')
def proverbio_view(id_):
    significado = s[id_]
    return render_template('proverbio_view.html', p = {'title': id_, 'significado': significado})


@app.route('/relatorios/semana')
def semana():

    p = random.choice(s.keys())
    return render_template('proverbio_semana_view.html', proverbio=p)


@app.route('/pessoas')
def pessoas_view():
    return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)
