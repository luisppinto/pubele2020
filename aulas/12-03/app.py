from flask import Flask, render_template, request

import random

import shelve

from bd import proverbios, pessoas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/proverbios')
def proverbios_view():
    return render_template('proverbios_view.html', title='Proverbios', proverbios=proverbios)

@app.route('/proverbios/novo', methods=['POST'])
def proverbios_novo():
    title = request.form.get('title')
    signi = request.form.get('significado')
    return render_template('proverbio_view.html', p = {'title': title, 'significado': signi})

@app.route('/proverbios/proverbio/<id_>')
def proverbio_view(id_):
    return render_template('proverbio_view.html', p = proverbios[int(id_)])


@app.route('/proverbios/semana')
def semana():
    p = random.choice(proverbios)
    return render_template('proverbio_semana_view.html', proverbio=p)


@app.route('/pessoas')
def pessoas_view():
    return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)
