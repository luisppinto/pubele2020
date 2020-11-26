from re import *
import os
import jinja2 as j2
r="/home/luisppinto/Desktop/pubele2020/pubele-aulas/data-collections/etl/"

meta=j2.Template("""
id: {{id}}
type: carta
destinatário: Eurico Tomás de Lima #dicionário -> chave1: exemplo
remetente:
data:
local_o:
descrição: |

files:
{% for f in files %}  - {{f}}
{% endfor %}
""")

for dir, subdirs, files in os.walk(r):
    ccarta = sub(r'.*/','',dir)
    conteudo=meta.render({"id": ccarta, "files": files})
        print("===",dir,meta.render({"id": ccarta,"files": files}))
    f=open( f"{dir}/{ccarta}.yaml","w")
    f.write
