from flask import Flask, render_template, request, redirect
import shelve
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

@app.route('/api/novocd', methods=['POST'])
def api_cd_novo():

	data = dict(request.form)
	insert(data)
	return json.dumps(data)

def insert(cd):
	with shelve.open('cds.db', writeback=True) as s:
		s[cd['title']] = cd['title']
		s[cd['artist']] = cd['artist']
		s[cd['year']] = cd['year']
		s[cd['country']] = cd['country']
		s[cd['company']] = cd['company']
		s[cd['artwork']] = cd['artwork']
		s[cd['id']] = cd['id']
		return s
