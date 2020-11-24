from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import os # Usado em create_page() e index()
import webbrowser #Abrir diretamente index

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
		context="{"
		title = i.title
		artist = i.artist
		year = i.year
		country = i.country
		company = i.company
		description = i.description

		if title != None:
			title =i.title.text
			context = context + "'title':title, "
		if artist != None:
			artist = i.artist.text
			context = context + "'artist':artist, "
		if year != None:
			year = i.year.text
			context = context + "'year':year, "
		if country != None:
			country = i.country.text
			context = context + "'country':country, "
		if company != None:
			company = i.company.text
			context = context + "'company':company, "
		if description != None:
			description = i.description.text
			context = context + "'description':description}"

		print(context)
		f_output = open('{}.html'.format(title),'w')
		print(page.render(context=context), file=f_output)

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
		print(a.render({'title':title}), file=f_output)
	indice = 'file:///'+os.getcwd()+'/' + 'index.html'
	webbrowser.open_new_tab(indice)

def main():
	get_cd()
	create_page(cd)
	index(cd)
	#print(cd) # Ver lista com cds e respetivos conteúdos
main()
