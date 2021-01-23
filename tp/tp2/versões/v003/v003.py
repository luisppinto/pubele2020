from flask import Flask, render_template, request, redirect
import json
import requests
from db_cds import *

app = Flask(__name__) # required

s = shelve.open('cds.db')

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

	# ADICIONA UM NOVO CD
@app.route('/cds/novo', methods=['POST'])
def cds_novo():

	title = request.form.get('title')
	artist = request.form.get('artist')
	artwork = request.form.get('artwork')
	country = request.form.get('country')
	company = request.form.get('company')
	description = request.form.get('description')
	year = request.form.get('year')

	s[title] = artist, artwork, country, company, description, year
	s.sync()
	ps = list(s.keys())

	return render_template('index.html', title='CDs', cds=ps)
