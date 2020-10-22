from re import *

with open("dicionario_medico.txt", "r") as f:

    content = f.read()
    new_content = sub('\x0c', '\n', content)

    with open("dicionario_medico_formatado.txt", "w") as o:
        o.write(new_content)
