from re import *
info={
"Title":"Aula de Publicação Eletrónica",
"Date":"29/10/2020",
"Team":'''<li>Rui Costa<br>83813<br>ruicosta@slb.pt</li>
<li>Paulo Jorge<br>84480<br>paulojorge@sapo.pt</li>''',
"Description":"Descrição da aula de Publicação Eletrónica"}

def extract():
    with open("reportxml.xml") as f:
        report=f.read()
    info={}
    v=search(r'<title>(.*)</title>',report)
    if v:
        info["Title"]=v[1]
    v=search(r'<date>(.*)</date>',report)
    if v:
        info["Date"]=v[1]
    print(info)

def subst(file,d):
    with open(file) as f:
        template=f.read()
    for key,value in d.items():
        template=sub(rf'#{key}',rf'{value}',template)
    return(template)

def main():
    print(subst("template.html", info))
    extract()
main()
