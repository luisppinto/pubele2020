from re import *
import jinja2 as j2

with open("catalogotp1.xml") as f:
    report=f.read()
cds = []
for tag,miolo in findall(r'<(.*?)>(.*?)</\1>',report):
	cds.append((tag,miolo))
#print(cds)

info = []
for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
	info.append(miolo)
print(info)

index=j2.Template("""
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
       {% for el in cds %}
         <li>{{title}}</li>
       {% endfor %}
        </ol><br>
	</body>
</html>
""")
print(index.render(cds))
