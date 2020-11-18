from re import *
import jinja2 as j2
import lxml
'''
def extract():

	with open("report.xml") as f:
		report=f.read()

	info = []

	for tag,miolo in findall(r'<(.*?)>(.*?)</\1>',report):
		info.append((tag,miolo))

	print(info)
'''
def refile(filename):

	with open(filename) as f:
		report=f.read()

	return report

def extract_dict(l,report): #devolve dicionario

	info = {}
	for elem in l:
		v=search(rf"<{elem}>((?:.|\n)*?)</{elem}>",report)
		if v:
			info[elem]=v[1]

	return info

def preenche(info):
	t = j2.Template("""
<html>
<head>
{% for elem in info %}
  <title> {{ elem.title }} </title>
 {% endfor %}
  <meta charset="UTF-8"/>
</head>
<body>
    {% for elem in info %}
 <h1>{{title}}</h1>
 <h2>{{artist}}</h2>
 <p><b>Ano: </b>{{year}} <b>País: </b>{{country}} <b>Produtora: </b>{{company}}</p>
 <h2> Descrição </h2>
 <p> {{description}} </p>
    {% endfor %}
</body>
</html>
""")
	print(t.render(info))

def indice(info):

    i = j2.Template("""
    <!DOCTYPE html>
    <html>
    <head>
    	<title>Catálogo de CDs</title>
    	<meta charset="utf-8"/>
    </head>
    	<body>
    	<h1>Índice</h1>
    	<hr>
    	<ol>
           {% for el in info %}
             <li><a href="{{ cd.url }}">{{ cd.title }}</a></li>
           {% endfor %}
            </ol><br>
    	</body>
    </html>
    """)
    print(i.render(info))

def main():

	f = refile('catalogotp1.xml')
	dic = extract_dict(['title','artist','year','description','country','company'],f)
	preenche(dic)

main()
