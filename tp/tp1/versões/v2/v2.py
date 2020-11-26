from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import sys # Usado em index()
import os # Usado em create_page()

cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos

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
			<title>{{cd.title}}</title
		<meta charset="UTF-8"/>
	</head>
	<body>
			<h1>{{cd.title}}</h1>
			<h2>{{cd.artist}}</h2>
			<p><b>Ano: </b>{{cd.year}} <b>País: </b>{{cd.country}} <b>Produtora: </b>{{cd.company}} </p>
			<h2> Descrição </h2>
			<p>{{cd.description}}</p>
			<a href="index.html">Voltar ao índice</a>
	</body>
</html>
""")
	for i in cd:
		print(page.render(cd))
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
					{% for el in cd %}
				<li><a href="{{el.title}}.html">{{el.title}}</a></li>
					{% endfor %}
				</ul>
		</body>
	</html>
	""")
		file = open('index.html', 'w') #Cria ficheiro index.html automaticamente
		sys.stdout = file
		print(a.render({"cd":cd}), file=file)

def main():
	get_cd()
	#create_page(cd)
	#index(cd)
	print(cd) # Ver lista com cds e respetivos conteúdos
main()
