from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_titulos() e get_cd()
import sys # Usado em index()

lista_cds=[]
cd=[]

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
		for i in ad.find_all("title"): # !!! ESTÁ A DEVOLVER O title COM AS TAGS !!! NÃO PODE !!!
			cd.append(i.parent)

def create_page(cd):
	count=0
	for i in cd: # Permite o output de um ficheiro por cada elemento da lista
		count += 1
		filename = '{}.html'.format(count) # !!! FALTA MUDAR O NOME PARA O NOME DE CADA title !!!
		with open(filename, 'w') as f_out:
			f_out.write('{}\n'.format(i))

		# !!! FALTA IMPLEMENTAR O TEMPLATE A SEGUIR !!!
		'''t = j2.Template("""
	<html>
		<head>
			{% for el in cd %}
				{{el.title}}
			{% endfor %}
			<meta charset="UTF-8"/>
		</head>
		<body>
			{% for el in cd %}
				<h1>{{el.title}}</h1>
				<h2>{{el.artist}}</h2>
				<p><b>Ano: </b>{{el.year}}<b>País: </b>{{el.country}}<b>Produtora: </b>{{el.company}}</p>
				<h2> Descrição </h2>
				<p>{{el.description}}</p>
			{% endfor %}
		</body>
	</html>
	""")
	print(a.render({"cd":cd}))'''

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
	create_page(cd)
	index(lista_cds)
	#print(lista_cds) # Ver lista com títulos dos cds
	#print(cd) # Ver lista com cds e respetivos conteúdos
main()
