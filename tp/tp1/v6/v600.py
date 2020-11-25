from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import os # Usado em create_page() e index()
import webbrowser #Abrir diretamente index

cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos
title=[]

def get_codigo():
	with open('v600.py', encoding='utf-8') as original, open('codigo.txt', "w", encoding='utf-8') as target:
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
		f_output = open('{}.html'.format(nomes),'w', encoding='utf-8')
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
				<li><a href="relatorio.html">Aceder ao relório<a></li>
		</body>
	</html>
	""")

	for i in cd:
		title.append(i.title.text)
		f_output = open('index.html', 'w', encoding='utf-8') #Cria ficheiro index.html automaticamente
		print(a.render({'title':title}), file=f_output)
	indice = 'file:///'+os.getcwd()+'/' + 'index.html'
	webbrowser.open_new_tab(indice)


def relatorio():
	k = j2.Template('''
<!DOCTYPE html>
	<html>
		<head>
			<meta charset="UTF-8">
			<title>Relatório</title>
		</head>
		<body>
			<h1>Relatório</h1>
			<h2> Ficheiro Catálogotp1.xml </h2>
			 <p>
			 	O ficheiro Catálogotp1.xml contém um conjunto de dados relativos a CDs de Música.<br>
				Estes CDs contém um titulo, de caracter obrigatório, contém ainda um artista, um país, uma produtora, uma descrição e um ano.<br>
				Abaixo podemos ver um excerto de código em XML:
			</p>
			<p>
				&ltCATALOG&gt<br>
				&nbsp&nbsp&nbsp  &ltCD&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lttitle&gtA Vida Que Eu Escolhi&lt/title&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartist&gtTony Carreira&lt/artist&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcountry&gtPortugal&lt/country&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcompany&gtEspacial&lt/company&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltdescription&gtA Vida Que Eu Escolhi é o décimo segundo álbum de estúdio a solo do cantor português Tony Carreira. Foi lançado em 2006 pela editora Espacial. &lt/description&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltyear&gt2006&lt/year&gt &lt/CD&gt<br>
				&nbsp&nbsp&nbsp  &ltCD&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lttitle&gtHide your heart&lt/title&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartist&gtBonnie Tyler&lt/artist&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcountry&gtReino Unido&lt/country&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcompany&gtCBS Records&lt/company&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltdescription&gtHide Your Heart (released under the title Notes from America in the United States, Canada and Brazil), is the seventh studio album by Welsh singer Bonnie Tyler.&lt/description&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltyear&gt1988&lt/year&gt &lt/CD&gt<br>
				...
			</p>
			<h2> Nome do Ficheiro.py </h2>
			<p>
				O ficheiro que deu origem a todo o website começa pelo import das librarias necessárias na resolução de algoritmos.
			</p>
			<p>
				&nbsp&nbsp&nbsp from re import * <br>
				&nbsp&nbsp&nbsp import jinja2 as j2<br>
				&nbsp&nbsp&nbsp import lxml<br>
				&nbsp&nbsp&nbsp from bs4 import BeautifulSoup as bs <br>
				&nbsp&nbsp&nbsp import sys<br>
				&nbsp&nbsp&nbsp import os<br>
				&nbsp&nbsp&nbsp import webbrowser
			</p>
			<p>
				Seguiu-se a inicialização das variáveis globais:
			</p>
			<p>
				&nbsp&nbsp&nbsp cd=[] <br>
				&nbsp&nbsp&nbsp title=[] <br>
			</p>
			<h3>Função get_cd()</h3>
			<p>
				&nbsp&nbsp&nbsp def get_cd():<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp with open('catalogotp1.xml') as f:<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp d=f.read()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp ad=bs(d,"xml")<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp for i in ad.find_all("CD"):<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp cd.append(i)<br>
			</p>
			<p>
				Esta função começa por abrir o ficheiro catalogotp1.xml sendo este atribuido á variável f, usando a função read() em f criamos uma <br>
				em f criamos uma variavel d que contém todo o conteúdo de catalogotp1.xml com o formato XML.<br>
				Usando a libraria bs4 criamos uma soup que contém o conteúdo em d no formato xml. Com o auxilio do ciclo for e da função find_all<br>
				encontramos todas as tags CD e guardamos o seu conteúdo na lista cd.<br>
			</p>
			<h3>Função index(cd)</h3>
			<p>
				&nbsp&nbsp&nbsp def index(cd):<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp a = j2.Template("""<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lt!DOCTYPE html&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lthtml&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lthead&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltmeta charset="UTF-8"&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lttitle&gtCatálogo de CDs&lt/title&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lt/head&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltbody&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	&lth1&gtÍndice&lt/h1&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp		&ltul&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp			{% for el in title %}<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp		&ltli&gt&lta href="{{el}}.html"&gt{{el}}&lt/a&gt&lt/li&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp			{% endfor %}<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	&lt/ul&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lt/body&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lt/html&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp """)
				&nbsp&nbsp&nbsp for i in cd:
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp title.append(i.title.text)
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp f_output = open('index.html', 'w')
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp print(a.render({'title':title}), file=f_output)
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp indice = 'file:///'+os.getcwd()+'/' + 'index.html'
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp webbrowser.open_new_tab(indice)
			</p>
			<p>
				Esta função consiste em criar um indice de CDs. Recebe como argumento o conteúdo dos CDs obtidos em get_cd().<br>
				Cria um template que vai dar origem ao ficheiro index.html, em que para cada CD usamos o titulo do mesmo para criar as hiperligações necessárias.<br>
				Por fim implementamos uma função de abertura do index.html automática após correr o programa.
			</p>
			<h3>Função main()</h3>
			<p>
				&nbsp&nbsp&nbsp def main():<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	get_cd()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	create_page(cd)<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	index(cd)<br>
				<br>
				&nbsp&nbsp&nbsp main()
			</p>
			<p>
				Esta função basicamente corre todos as funções nele contidas.
			</p>
			<br>
			<a href="index.html">Voltar ao índice</a>
		</body>
	</html>
''')
	f_out = open('relatorio.html', 'w', encoding='utf-8')
	print(k.render(), file=f_out)

def main():
	get_codigo()
	get_cd()
	create_page(cd)
	index(cd)
	relatorio()

	#print(cd) # Ver lista com cds e respetivos conteúdos
main()
