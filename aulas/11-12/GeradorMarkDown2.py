import lxml
from bs4 import BeautifulSoup as bs

file="/home/luisppinto/Desktop/pubele2020/pubele-aulas/aulas/11-09/catalogo.xml"
with open(file) as f:
    d=f.read()

ad = bs(d,"xml")

for i in ad.find_all("relations"):
    i.name="ul"
    for j in i.find_all("rel"):
        j.name = "li"
        j.contents.append("batatas")
print(ad)
