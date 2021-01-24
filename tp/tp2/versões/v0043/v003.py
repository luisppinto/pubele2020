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
@app.route('/cds/novocd')
def novo_cd_view():
    return render_template('add_cd_view.html')

@app.route('/api/cds/novocd', methods=['GET'])
def api_novo_cd():
	title = request.form.get('title')
	artist = request.form.get('artist')
	artwork = request.form.get('artwork')
	country = request.form.get('country')
	company = request.form.get('company')
	description = request.form.get('description')
	year = request.form.get('year')

	with shelve.open('cds.db', writeback=True) as s:
	# 3º Indicamos qual a posição de cada conteudo no shelve
		s[{'id'}].append({'title':title,'artist':artist,'artwork':artwork,'company':company,'description':description,'year':year})
		s.close()
	return render_template('add_cd_view.html')


@app.route('/cds/<cds>', methods=['GET'])
def get_cd_view(cd):
	res = requests.get('http://localhost:5000/api/cds/' + cd)
	p = json.dumps(res.content)

	return render_template('cd_view.html', p=p)
