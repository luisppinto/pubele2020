from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import sys # Usado em index()
import os # Usado em create_page()

cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos
title=[]

def get_cd():
	with open('catalogotp1.xml') as f:
		d=f.read()
		ad=bs(d,"xml")
		for i in ad.find_all("CD"):
			cd.append(i)

def create_page(cd):

	page = j2.Template("""
<html>
	<head>
			<title>{{title}}</title
		<meta charset="UTF-8"/>
	</head>
	<body>
			<h1>{{title}}</h1>
			<h2>{{artist}}</h2>
			<p><b>Ano: </b>{{year}} <b>País: </b>{{country}} <b>Produtora: </b>{{company}} </p>
			<h2> Descrição </h2>
			<p>{{description}}</p>
			<a href="index.html">Voltar ao índice</a>
	</body>
</html>
""")
	for i in cd:
		nomes= i.title.text
		#print (nomes)
		f_output = open('{}.html'.format(nomes),'w')
		#artistas = i.artist.text
		#print(artistas)
		print(page.render({'title':i.title.text, 'artist':i.artist.text, 'year': i.year.text, 'country':i.country.text, 'company':i.company.text, 'description':i.description.text}), file=f_output)
'''
	for i in cd:
		title.append(i.title.text)
		f_output = open('{}.html'.format(title), 'w')
		sys.stdout = f_output
		print(page.render({"title":title,"artist":artist}), file=f_output)
'''
def index(cd):
	# Cria índice (com hiperligação) de todos os cds presentes no catalogotp1.xml
	a = j2.Template("""
	<!DOCTYPE html>
	<html>
		<head>
			<title>Catálogo de CDs</title>
			<meta charset="utf-8"/>
		</head>
		<body>
			<h1>Índice</h1>
				<ul>
					{% for el in title %}
				<li><a href="{{el}}.html">{{el}}</a></li>
					{% endfor %}
				</ul>
		</body>
	</html>
	""")
		
	for i in cd:
		title.append(i.title.text)
		f_output = open('index.html', 'w') #Cria ficheiro index.html automaticamente
		# sys.stdout = f_output
		print(a.render({'title':title}), file=f_output)
	
		
def main():
	get_cd()
	create_page(cd)
	index(cd)
	# print(cd) # Ver lista com cds e respetivos conteúdos
main()
