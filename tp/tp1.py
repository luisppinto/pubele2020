from re import *
import jinja2 as j2
import lxml
from bs4 import BeautifulSoup as bs


'''Generalizar o conversor relatórios → html de modo a que

1) passe a permitir vários relatórios (presentemente
só aceita um relatório): no XML juntar uma nova raíz
por exemplo "portfolio" debaixo da qual fiquem os vários
"report".
Sugestão:
    * cada report gerar uma página html separada
    * construir um índice geral que permita aceder
à página de cada projecto.

2) permita a existência de um novo elemento com o link
para um ficheiro
(correspondente ao código do projecto)

3) Extras: se conseguir, faça os extras que se lembrar!

Sugestões:
  * arrange uma página com bom aspecto...
  * crie um índice de autores.
  * Permita que a description inclua "hashtags" (exemplo
"#história") e crie uma página índice (hastag → reports)

4) Faço um portfolio.xml exemplo (que seja convincente)
para demonstração.'''

def extract(): # extrai a informação do relatório em XML
	with open("report.xml") as f:
		report=f.read()
	info=[]
	labels = findall(r'<.*>',report)
	for label in labels:
		chave=search(r'</(.*)>',label)
		v=search(r'>(.*)<',label)
		if v:
			info.append((chave[1],v[1]))
	print(info)

def extract2():

	with open("report.xml") as f:
		report=f.read()

	info = []

	for tag,miolo in findall(r'<(.*?)>(.*?)</\1>',report):
		info.append((tag,miolo))


	print(info)
# recebe uma lista com title,date,team e description e devolve um dicionário com a info xml dessas tags

def refile(filename): # devolve texto

	with open(filename) as f:
		report=f.read()

	return report

def extract_dict(l,report): # devolve dicionário

	info = {}
	for elem in l:
		v=search(rf"<{elem}>((?:.|\n)*?)</{elem}>",report)
		if v:
			info[elem]=v[1]

	return info

def extrai_listaH(xml,tag):

	info = []

	for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
		info.append(miolo)

	return info

def preenche2(info):

	t = j2.Template( """
<html>
<head>
  <title> {{title}} </title>
  <meta charset="UTF-8"/>
</head>
<body>
 <h1> {{title}} </h1>
 <p> {{date}} </p>
 <h2>Autores</h2>
 <hr/>
 <ol>
    {% for el in team  %}
      <li> {{el['name']}} : {{el['email']}} </li>
    {% endfor %}
 </ol>
 <hr/>
 <h2> Descrição </h2>
 <p> {{description}} </p>
</body>
</html>

""")

	print(t.render(info))

def index():



    <!DOCTYPE html>
<html>
	<head>
		<title>Index</title>
		<meta charset="utf-8"/>
	</head>

	<body>
		<h1>Index</h1>
		<hr>
		<a href="page1.html">Page 1</a><br>
		<a href="page2.html" target="_blank">Page 2</a><br>
		<a href="page3.html" title="Go to Page 3">Page 3</a><br>
		<a href="page4.html" title="Go to Page 4" target="_blank">Page 4</a><br>
	</body>

</html>


def extractmulti():

    file="../pubele2020/tp/catalogotp.xml"
    with open(file) as f:
        d=f.read()

    ad = bs(d,"xml")

    for i in ad.find_all("titulo"):
        print("##",i.text)
        aux1=i.parent.resource
        if aux1:
            print(f'[Link]({aux1.text})')
        aux2=i.parent.description
        if aux2:
            print(aux2.text)




def main():

	#info = extract()
	f = refile('report.xml')
	dic = extract_dict(['title','team','date','description'],f)
	aux = extrai_listaH(dic['team'],'element')
	dic['team'] = [extract_dict(['name','email'],el) for el in aux]
	preenche2(dic)

main()
