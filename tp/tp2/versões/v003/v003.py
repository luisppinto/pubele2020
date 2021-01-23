from flask import Flask, render_template, request, redirect
import json
import requests
from db_cds import *  

app = Flask(__name__) # required

	# INDEX 
	# Lista de CDs
		# FRONT END 
@app.route('/', methods=['GET'])
def index_view():
	res = requests.get('http://localhost:5000/api/cds')
	ps = json.loads(res.content)
	return render_template('index.html', cds=ps)


		# BACKEND
@app.route('/api/cds', methods=['GET'])
def api_get_cds():
	ps = cds
	return json.dumps(ps)

	# Informações adicionais
	# Lista autores 
		# FRONT END
@app.route('/autores', methods=['GET'])
def info_ad_view():
	res = requests.get('http://localhost:5000/api/autores')
	ss = json.loads(res.content)
	return render_template('info_ad_view.html', autores=ss)
	
		# BACKEND
@app.route('/api/autores', methods=['GET'])
def api_get_autores():
	ss = autores
	return json.dumps(ss)

	# Ver CD

@app.route('/cds/<cd>', methods=['GET'])
def get_cd_view(cd):

	res = requests.get('http://localhost:5000/api/cds/'+ cd['title'])
	p = json.loads(res.content)

	return render_template('cd_view.html', p=p)

@app.route('/api/cds/<cd>', methods=['GET'])
def api_get_cd(cd):

	p = find_one(cd)
	return json.dumps(p)

@app.route('/api/cds/novocd', methods=['POST'])
def api_cd_novo():
	# 1º abrimos o shelve
	with shelve.open('cds.db', writeback=True) as s:
	# 2º passamos do html para variavel
		id = request.form.get('id')
		title = request.form.get('title')
		artist = request.form.get('artist')
		artwork = request.form.get('artwork')
		country = request.form.get('country')
		company = request.form.get('company')
		description = request.form.get('description')
		year = request.form.get('year')

	# 3º Indicamos qual a posição de cada conteudo no shelve
		s[cd['id']] = id
		s[cd['title']] = title
		s[cd['artist']] = artist
		s[cd['artwork']] = artwork
		s[cd['country']] = country
		s[cd['company']] = company
		s[cd['description']] = description
		s[cd['year']] = year

	# 4º Atualizamos o conteudo do shelve
		s.sync()
		ps = list(s.keys())

	return render_template('add_cd_view.html', title='CDs', cds=ps)

@app.route('/cds/novocd')
def novo_cd():
	return render_template('add_cd_view.html')