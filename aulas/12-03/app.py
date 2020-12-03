from flask import Flask, render_template
import jinja2 as j2

import random

app = Flask(__name__)

proverbios = [
'Mais vale tarde do que nunca.',
'Mês de abril, arroz de caril.',
'Quem vai à guerra dá e leva.'
]

proverbios = [
{
'id':0,
'texto':'Mais vale tarde do que nunca.',
'significado':'Atrasei-me, mas ao menos cheguei.'
},
{
'id':1,
'texto':'Mês de abril, arroz de caril.',
'significado':'Arroz de caril é bom em abril.'
},
{
'id':2,
'texto':'Quem vai à guerra dá e leva.',
'significado':'...'
}
]

pessoas = [
'Pedro',
'Beatriz',
'Paulo'
]

# OS TEMPLATES QUE AQUI ESTAVAM PASSARAM PARA A PASTA TEMPLATES

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/proverbios')
def proverbios_view():
	return render_template('proverbios_view.html', title='Provérbios', proverbios=proverbios)

@app.route('/proverbios/proverbio/<id>')
def proverbio_view(id):
	return render_template('proverbio_view.html', p = proverbios[int(id)])

@app.route('/proverbios/semana')
def semana():
	p = random.choice(proverbios)
	return render_template('proverbio_semana.html', title='Provérbio da semana', proverbio=p)

@app.route('/pessoas')
def pessoas():
	return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)
