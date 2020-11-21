from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_titulos() e get_cd()
import sys # Usado em index()
import os # Usado em create_page()

lista_cds=[] # Lista vazia (a preencher por get_titulos()) de todos os títulos dos cds
cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos

def get_titulos():
	# Faz uma lista com todos os títulos de cds presentes no catalogotp1.xml
	# para ser usado no index()
	with open('catalogotp1.xml') as f:
		d=f.read()
		ad = bs(d,"xml")
		for i in ad.find_all("CD"):
			lista_cds.append(i.title.text)

def get_cd():
	# Faz uma lista com todos os cds (e os respetivos conteúdos) presentes no catalogotp1.xml
	# para ser usado no create_page()
	with open('catalogotp1.xml') as f:
		d=f.read()
		ad = bs(d,"xml")
		for i in ad.find_all("title"):
			cd.append(i.parent.text)

def create_page(cd, lista_cds):

	page = j2.Template("""
<html>
	<head>
			{{title}}
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

	for title in lista_cds:
		for i in cd:
			f_output2 = open('{}.html'.format(title), 'w')
			sys.stdout = f_output2
			print(page.render({"cd":cd}), file=f_output2)

def index(lista_cds):
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
					{% for el in lista_cds %}
				<li><a href="{{el}}.html">{{el}}</a></li>
					{% endfor %}
				</ul>
		</body>
	</html>
	""")
		file = open('index.html', 'w') #Cria ficheiro index.html automaticamente
		sys.stdout = file
		print(a.render({"lista_cds":lista_cds}), file=file)

def main():
	get_titulos()
	get_cd()
	create_page(cd, lista_cds)
	#index(lista_cds)
	#print(lista_cds) # Ver lista com títulos dos cds
	#print(cd) # Ver lista com cds e respetivos conteúdos
main()
