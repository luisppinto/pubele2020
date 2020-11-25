'''GRUPO 8 - TRABALHO PRÁTICO 1 - PUBLICAÇÃO ELETRÓNICA
AUTORES:
BRUNO REBELO LOPES A57768
MORGANA SACRAMENTO FERREIRA A93779
LUÍS PEDRO DA SILVA PINTO A83016'''

import re #Usado para o search
from re import *
import jinja2 as j2 # Usado em create_page() e index()
import lxml
from bs4 import BeautifulSoup as bs # Usado em get_cd()
import os # Usado em create_page() e index()
import webbrowser #Abrir diretamente index
import cgi #Usado em search()

cd=[] # Lista vazia (a preencher por get_cd()) de todos os cds e respetivos conteúdos
title=[]
artist=[]
cd_artista=[]

def get_codigo():
	with open('v6051.py', encoding='utf-8') as original, open('codigo.txt', "w", encoding='utf-8') as target:
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
		<link rel="stylesheet" href="stylesheet.css">
	</head>
	<body>
	<div class="header">
				<h1>Catálogo de CDs</h1>
		</div>
		<div class="nav">
			<table class="nav-tab">
				<tr>
						<th><a href="index.html"><div class="hed">Lista de Títulos</div></a></th>
						<th><a href="relatorio.html"><div class="hed">Relatório</div></a></th>
						<th><a href="codigo.txt" target="_blank"><div class="hed">Código</a></div></th>
				</tr>
						</table>
		</div>

		<div class="main_content">

			<h1>{{newdic.title}}</h1>
			<div class="art"><img src={{newdic.artwork}} alt="Album Artwork"></div>
			<h2>{{newdic.artist}}</h2>
			<p><b>Ano: </b>{{newdic.year}} <b>País: </b>{{newdic.country}} <img src="https://flagcdn.com/h20/{{newdic.country.lower()}}.png"> <b>Produtora: </b>{{newdic.company}} </p>
			<p>{{newdic.description}}</p>
			<a href="index.html">Voltar ao índice</a>
			</div>
	</body>
</html>
""")

	for i in cd:
		nomes=i.title.text
		newdic={}
		atitle = i.title
		aartist = i.artist
		aartwork = i.artwork
		ayear = i.year
		acountry = i.country
		acompany = i.company
		adescription = i.description

		if atitle != None:
			newdic['title']= i.title.text
		if aartist != None:
			newdic['artist']= i.artist.text
		if aartwork != None:
			newdic['artwork']= i.artwork.text
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
			<link rel="stylesheet" href="stylesheet.css">
		</head>
		<body>
		<div class="header">
				<h1>Catálogo de CDs</h1>
		</div>
		<form style="text-align:center" name="search" action="search.py" method="get">
				<input type="text" name="searchbox">
				<input type="submit" value="Procurar">
		</form><br>
		<div class="nav">
			<table class="nav-tab">
				<tr>
						<th><a href="index.html"><div class="hed">Lista de Títulos</div></a></th>
						<th><a href="relatorio.html"><div class="hed">Relatório</div></a></th>
						<th><a href="codigo.txt" target="_blank"><div class="hed">Código</a></div></th>
				</tr>
						</table>
		</div>

		<div class="main_content">
			<table>
								{% for el in title %}
				<tr>
										<th><a href="{{el}}.html"><div class="hiper">{{el}}</div></a></th>

				</tr>
				{% endfor %}
			</table>
		</div>
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
			<link rel="stylesheet" href="stylesheet.css">
		</head>
		<body>
		<div class="header">
				<h1>Catálogo de CDs</h1>
		</div>

		<div class="nav">
			<table>
				<tr>
					<th><a href="index.html"><div class="hed">Lista de Títulos</div></a></th>
						<th><a href="relatorio.html"><div class="hed">Relatório</div></a></th>
										<th><a href="codigo.txt" target="_blank"><div class="hed">Código</a></div></th>
								</tr>
			</table>
		</div>
		<div class="main_content">
			<h1>Relatório</h1>
			<p>Autores:</p>
			<ul>
				<li>Bruno Rebelo Lopes a57768</li>
				<li>Morgana Sacramento Ferreira a93779</li>
				<li>Luís Pedro da Silva Pinto a83016</li>
			</ul>
			<h2> Ficheiro catalogotp1.xml </h2>
			 <p class="conteudo_relatorio">
				O ficheiro catalogotp1.xml contém um conjunto de dados relativos a CDs de Música.<br>
				Estes CDs contêm um título, de carácter obrigatório, contém ainda um artista, uma capa de álbum, um país, uma produtora, uma descrição e um ano.<br>
				Abaixo podemos ver um excerto de código em XML:
			</p>
			<p class="codigo">
				&ltCATALOG&gt<br>
				&nbsp&nbsp&nbsp  &ltCD&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lttitle&gtA Vida Que Eu Escolhi&lt/title&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartist&gtTony Carreira&lt/artist&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartwork&gthttps://img.discogs.com/ZrC2cjDjuh_mremQ6o5kXKlTFAQ=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-5263584-1389034439-9728.jpeg.jpg&lt/artwork&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcountry&gtPortugal&lt/country&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcompany&gtEspacial&lt/company&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltdescription&gtA Vida Que Eu Escolhi é o décimo segundo álbum de estúdio a solo do cantor português Tony Carreira. Foi lançado em 2006 pela editora Espacial. Contém 15 faixas, das quais se destacam "Mesmo Que Seja Mentira" e "É Melhor (Dizer Adeus)" (anteriormente editadas como extras no álbum Ao Vivo no Coliseu, também de 2006), bem como "O Que Vai Ser De Mim (Quando Fores Embora)" e "A Vida Que Eu Escolhi", 4 temas que fazem parte da compilação "20 Anos de Canções", lançada em 2008. Este trabalho esteve, ao todo, 64 semanas, no Top Oficial da AFP, a tabela semanal dos 30 álbuns mais vendidos em Portugal. Entrou na época de Natal de 2006 directamente para a 4ª posição, atingindo o 1º lugar à quarta semana, lugar que disputaria com André Sardet e Madonna e que ocuparia por mais 3 ocasiões mas que perderia definitivamente para José Afonso. &lt/description&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltyear&gt2006&lt/year&gt &lt/CD&gt<br>
				&nbsp&nbsp&nbsp  &ltCD&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &lttitle&gtHide Your Heart&lt/title&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartist&gtBonnie Tyler&lt/artist&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltartwork&gthttps://upload.wikimedia.org/wikipedia/en/2/23/Hide_Your_Heart_Front_Cover.jpg&lt/artwork&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcountry&gtReino Unido&lt/country&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltcompany&gtCBS Records&lt/company&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltdescription&gtHide Your Heart (released under the title Notes from America in the United States, Canada and Brazil), is the seventh studio album by Welsh singer Bonnie Tyler. The album features the song "Hide Your Heart" written by Paul Stanley, Desmond Child and Holly Knight. This song was later covered three times in 1989 Ace Frehley's Trouble Walkin', Robin Beck's Trouble Or Nothin', and Molly Hatchet's Lightning Strikes Twice. And performed in 1989 by Paul Stanley with Kiss on their Hot in the Shade album.&lt/description&gt<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &ltyear&gt1988&lt/year&gt &lt/CD&gt<br>
				...
			</p>
			<h2> g8.py </h2>
			<p class="conteudo_relatorio">
				O ficheiro que deu origem a todo o website começa pelo import das librarias necessárias na resolução de algoritmos.
			</p>
			<p class="codigo">
				&nbsp&nbsp&nbsp from re import *<br>
				&nbsp&nbsp&nbsp import jinja2 as j2<br>
				&nbsp&nbsp&nbsp import lxml<br>
				&nbsp&nbsp&nbsp from bs4 import BeautifulSoup as bs<br>
				&nbsp&nbsp&nbsp import sys<br>
				&nbsp&nbsp&nbsp import os<br>
				&nbsp&nbsp&nbsp import webbrowser
			</p>
			<p class="conteudo_relatorio">
				Seguiu-se a inicialização das variáveis globais:
			</p>
			<p class="codigo">
				&nbsp&nbsp&nbsp cd=[] <br>
				&nbsp&nbsp&nbsp title=[] <br>
			</p>
			<h3>Função get_cd()</h3>
			<p class="codigo">
				&nbsp&nbsp&nbsp def get_cd():<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp with open('catalogotp1.xml') as f:<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp d=f.read()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp ad=bs(d,"xml")<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp for i in ad.find_all("CD"):<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp cd.append(i)<br>
			</p>
			<p class="conteudo_relatorio">
				Esta função começa por abrir o ficheiro catalogotp1.xml sendo este atribuido à variável f, usando a função read() em f criamos uma <br>
				uma variável d que contém todo o conteúdo de catalogotp1.xml com o formato XML.<br>
				Usando a libraria bs4 criamos uma soup que contém o conteúdo em d no formato xml. Com o auxílio do ciclo for e da função find_all<br>
				encontramos todas as tags CD e guardamos o seu conteúdo na lista cd.<br>
			</p>
			<h3>Função create_page(cd)</h3>
			<p class="codigo">



			</p>
			<p class="conteudo_relatorio">
				Esta função consiste na criação individual de cada página de cd. Recebe como argumento o conteúdo dos CDs obtidos em get_cd().<br>
				Cria um template que vai dar origem ao ficheiro com o nome do título do cd + ".html".<br>
				De seguida, iniciou-se um loop que irá preencher o template com o conteúdo do cd.<br>
				Para isso, fomos buscar o conteúdo de cada cd como o artwork através do i.artwork.<br>
				Ainda se implementou um if para cada variável, pois pode haver casos onde não existe artwork ou year, que adiciona os valores num dicionário.</br>
				Por fim, foi feito o .render com o dicionário, obtendo-se o resultado pretendido.
			</p>
			<h3>Função index(cd)</h3>
			<p class="codigo">
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
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp """)<br>
				&nbsp&nbsp&nbsp for i in cd:<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp title.append(i.title.text)<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp f_output = open('index.html', 'w') <br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp print(a.render({'title':title}), file=f_output)<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp indice = 'file:///'+os.getcwd()+'/' + 'index.html'<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp webbrowser.open_new_tab(indice)
			</p>
			<p class="conteudo_relatorio">
				Esta função consiste em criar um índice de CDs. Recebe como argumento o conteúdo dos CDs obtidos em get_cd().<br>
				Cria um template que vai dar origem ao ficheiro index.html, em que para cada CD usamos o título do mesmo para criar as hiperligações necessárias.<br>
				Por fim implementámos uma função de abertura do index.html automática após correr o programa.
			</p>
			<h3>Função relatorio()</h3>
			<p class="codigo">



			</p>
			<p class="conteudo_relatorio">
				A função relatorio() foi usada para gerar o ficheiro onde nos encontramos agora.<br>
				Foi aplicado um template que só dá origem a um relatorio.html quando o ficheiro g8.py corre, diminuindo a quantidade de ficheiros iniciais.<br>
				Aproveitou-se esta função para se gerar um ficheiro css com o nome standart stylesheet.css, que irá ser utilizado para alegrar as páginas html deste trabalho.
			</p>
			<h3>Função main()</h3>
			<p class="codigo">
				&nbsp&nbsp&nbsp def main():<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  get_codigo()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	get_cd()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	create_page(cd)<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp	index(cd)<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  relatorio()<br>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  search()<br>
				&nbsp&nbsp&nbsp main()
			</p>
			<p class="conteudo_relatorio">
				Esta função basicamente corre todas as funções nele contidas.
			</p>
			<br>
			<a class="index" href="index.html">Voltar ao índice</a>

		</div>
		</body>
	</html>
''')
	f_out = open('relatorio.html', 'w', encoding='utf-8')
	print(k.render(), file=f_out)

	st = j2.Template('''    body {
										background-color:lightgrey;
										width:100%;
										max-width:1920px;}

								div.nav {width:75%;
					max-width: 1920px;
					align-self: center;
					padding-left: 12.5%;}

				table {width:100%}

								div.hiper {
										border: 1px solid black;
										background-color:grey;
										padding-top: 15px;
										padding-bottom: 15px;
										text-align:center;
										margin-top:5px;
										font-size: 20px;
										color: black;
										border-radius: 15px;
								}
							div.art {
							text-align:center;

							}
								th {
								width:33%;
								}
								div.hed {border: 1px solid black;
										background-color:grey;
										padding-top: 15px;
										padding-bottom: 15px;
										text-align:center;
										margin-top:5px;
										font-size: 20px;
										color: black;
										border-radius: 15px;
								}


				div.main_content {
					width:75%;
					max-width: 1920px;
					align-self: center;
					padding-left: 12.5%;}

				h1 {
					font-size: 40px;
					color: black;
					text-align:center;
					height:72px;
					padding-top:16px;
					width:100%;
					border-bottom: 1px solid black;}

				h2 {
					font-size: 30px;
					color: black;
					text-align:center;
					height:72px;
					padding-top:18px;
					width:100%;
					border-bottom: 1px solid black;}

				h3 {
					font-size: 24px;
					color: black;
					text-align:center;
					height:72px;
					padding-top:18px;
					width:100%;
					border-bottom: 1px solid black;}

				p.conteudo_relatorio {
					font-size: 18px;
					color:black;}

				p.codigo {
					font-size: 18px;
					color:grey;
					font-style: italic;}

				img {
					text-align:center;}

			''')
	f_out_stylesheet = open('stylesheet.css', 'w', encoding='utf-8')
	print(st.render(), file=f_out_stylesheet)

def search():

	with open('catalogotp1.xml') as f:
		d = f.read()
		ad = bs(d,"xml")
		intent = input("Pretende procurar algum CD? s/n")
		if intent == s:
			qual = input("Que CD prentende procurar?")
			results = ad.find_all(string=re.compile(qual))
			open = 'file:///'+os.getcwd()+'/'+results+'.html'
			webbrowser.open_new_tab(open)

def index_autores(cd):

	# Cria índice (com hiperligação) de todos os autores presentes no catalogotp1.xml

	a = j2.Template("""
	<!DOCTYPE html>
	<html>
		<head>
			<title>Índice de Autores</title>
			<meta charset="utf-8"/>
			<link rel="stylesheet" href="stylesheet.css">
		</head>
		<body>
		<div class="header">
				<h1>Índice de Autores</h1>	
		</div>	
		<div class="nav">
			<table class="nav-tab">
				<tr>
					<th><a href="index_autores.html">Lista de Artistas</a></th>
					<th><a href="relatorio.html">Relatório</a></th>
					<th><a href="codigo.txt">Código</a></th>
								</tr>
							</table>
		</div>
		
		<div class="main_content">
			<table>

						{% for el in artist %}
				<tr>
								<th><a href="{{el}}.html"><div class="hiper">{{el}}</div></a></th>
				
				</tr>
				
				{% endfor %}

			</table>
		</div>
		</body>
	</html>
	""")

	for i in cd:
		artist.append(i.artist.text)
		cd_artista.append(i.parent.title.text)
		#print(cd_artista)
		f_output = open('index_autores.html', 'w', encoding='utf-8') #Cria ficheiro index_autores.html automaticamente
		print(a.render({'artist':artist}), file=f_output)
	indice_autores = 'file:///'+os.getcwd()+'/' + 'index_autores.html'
	webbrowser.open_new_tab(indice_autores)

	#for j in cd:
		#cd_artista.append(j.title.text)
		#print(cd_artista)
		


def main():
	get_codigo()
	get_cd()
	create_page(cd)
	index(cd)
	relatorio()
	search()
	index_autores()
main()
