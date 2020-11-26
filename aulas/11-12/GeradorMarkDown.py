import lxml
from bs4 import BeautifulSoup as bs

file="/home/luisppinto/Desktop/pubele2020/pubele-aulas/aulas/11-09/catalogo.xml"
with open(file) as f:
    d=f.read()

ad = bs(d,"xml")

for i in ad.find_all("title"):
    print("##",i.text)
    aux1=i.parent.resource
    if aux1:
        print(f'[Link]({aux1.text})')
    aux2=i.parent.description
    if aux2:
        print(aux2.text)
