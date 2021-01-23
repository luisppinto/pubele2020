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

