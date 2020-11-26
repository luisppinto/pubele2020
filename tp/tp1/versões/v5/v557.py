from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import os # Usado em create_page() e index()
import webbrowser #Abrir diretamente index

cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos
title=[]

def get_codigo():
	with open('v557.py', encoding='utf-8') as original, open('codigo.txt', "w", encoding='utf-8') as target:
		target.writelines(original.readlines())

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
			<h1>{{newdic.title}}</h1>
			<h2>{{newdic.artist}}</h2>
			<p><b>Ano: </b>{{newdic.year}} <b>País: </b>{{newdic.country}} <b>Produtora: </b>{{newdic.company}} </p>
			<h2> Descrição </h2>
			<p>{{newdic.description}}</p>
			<a href="index.html">Voltar ao índice</a>
	</body>
</html>
""")

	for i in cd:
		nomes=i.title.text
		newdic={}
		atitle = i.title
		aartist = i.artist
		ayear = i.year
		acountry = i.country
		acompany = i.company
		adescription = i.description

		if atitle != None:
			newdic['title']= i.title.text
		if aartist != None:
			newdic['artist']= i.artist.text
		if ayear != None:
			newdic['year']= i.year.text
		if acountry != None:
			newdic['country']= i.country.text
		if acompany != None:
			newdic['company']= i.company.text
		if adescription != None:
			newdic['description']= i.description.text
		f_output = open('{}.html'.format(nomes),'w')
		print(page.render(newdic=newdic), file=f_output)

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
				<li><a href="codigo.txt">Aceder ao código-fonte<a></li>
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
	get_codigo()
	get_cd()
	create_page(cd)
	index(cd)
	#print(cd) # Ver lista com cds e respetivos conteúdos
main()
