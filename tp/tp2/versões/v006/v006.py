# Imports
from flask import Flask, render_template, request, redirect
import json
import requests
from db_cd import *
import re

# Lista Inicial de CDs - Catálogo
cds = [
    {
        'id': 0,
        'title': 'A Vida Que Eu Escolhi',
        'artist': 'Tony Carreira',
        'artwork': 'https://img.discogs.com/ZrC2cjDjuh_mremQ6o5kXKlTFAQ=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-5263584-1389034439-9728.jpeg.jpg',
        'country': 'PT',
        'company': 'Espacial',
        'description': 'A Vida Que Eu Escolhi é o décimo segundo álbum de estúdio a solo do cantor português Tony Carreira. Foi lançado em 2006 pela editora Espacial. Este trabalho esteve, ao todo, 64 semanas, no Top Oficial da AFP, a tabela semanal dos 30 álbuns mais vendidos em Portugal. Entrou na época de Natal de 2006 directamente para a 4ª posição, atingindo o 1º lugar à quarta semana, lugar que disputaria com André Sardet e Madonna e que ocuparia por mais 3 ocasiões mas que perderia definitivamente para José Afonso.',
        'year': '2006'
    },
    {
        'id': 1,
        'title': 'Hide Your Heart',
        'artist': 'Bonnie Tyler',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/2/23/Hide_Your_Heart_Front_Cover.jpg',
        'country': 'GB',
        'company': 'CBS Records',
        'description': 'Hide Your Heart (released under the title Notes from America in the United States, Canada and Brazil), is the seventh studio album by Welsh singer Bonnie Tyler. The album features the song "Hide Your Heart" written by Paul Stanley, Desmond Child and Holly Knight.',
        'year': '1988'
    },
    {
        'id': 2,
        'title': 'Aja',
        'artist': 'Steely Dan',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/4/49/Aja_album_cover.jpg',
        'country': 'US',
        'company': 'Harvest',
        'description': 'Aja (/ˈeɪʒə/, pronounced like Asia) is the sixth studio album by the American jazz rock band Steely Dan. It was released in September 1977 by ABC Records. Recording alongside nearly 40 musicians, band leaders Donald Fagen and Walter Becker pushed Steely Dan further into experimenting with different combinations of session players while pursuing longer, more sophisticated compositions for the album.',
        'year': '1973'
    },
    {
        'id': 3,
        'title': 'The Dark Side of The Moon',
        'artist': 'Pink Floyd',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png',
        'country': 'GB',
        'company': 'Harvest',
        'description': 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd, released on 1 March 1973 by Harvest Records. Primarily developed during live performances, the band premiered an early version of the record several months before recording began. The record was conceived as an album that focused on the pressures faced by the band during their arduous lifestyle, and dealing with the apparent mental health problems suffered by former band member Syd Barrett, who departed the group in 1968. New material was recorded in two sessions in 1972 and 1973 at Abbey Road Studios in London.',
        'year': '1973'
    },
    {
        'id': 4,
        'title': 'Return to the 36 Chambers',
        'artist': 'Ol Dirty Bastard',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/b/bf/Odb_welfare.jpg',
        'country': 'US',
        'company': 'Elektra',
        'description': 'Return to the 36 Chambers is the solo debut album of American rapper and Wu-Tang Clan member Ol Dirty Bastard, released March 28, 1995 on Elektra Records in the United States. It was the second solo album, after Method Mans Tical, to be released from the nine-member Wu-Tang clan, following the release of their debut album. Return to the 36 Chambers was primarily produced by RZA, with additional production from Ol Dirty Bastard, and affiliates True Master and 4th Disciple. The album features guest appearances from Wu-Tang members GZA, RZA, Method Man, Raekwon, Ghostface Killah and Masta Killa, as well as several Wu-Tang affiliates and Brooklyn Zu.',
        'year': '1995'
    },
    {
        'id': 5,
        'title': 'Unchain My Heart',
        'artist': 'Joe Cocker',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/8/8e/Joe_Cocker-Unchain_My_Heart_%28album_cover%29.jpg',
        'country': 'US',
        'company': 'EMI',
        'description': 'Unchain My Heart is the eleventh studio album by Joe Cocker, released in 1987.',
        'year': '1987'
    },
    {
        'id': 6,
        'title': 'Picture Book',
        'artist': 'Simply Red',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/e/e5/PictureBookSimplyRedalbumcover.png',
        'country': 'GB',
        'company': 'Elektra',
        'description': 'Picture Book is the debut album by British pop and soul group Simply Red, released in October 1985.',
        'year': '1985'
    }]
# Lista de Autores
autores = [
    {'name': 'Bruno Rebelo Lopes', 'number': '57768'},
			{'name':'Morgana Sacramento Ferreira','number':'93779'},
			{'name':'Luís Pedro da Silva Pinto','number':'83016'}]

app = Flask(__name__) # required

# Ciclo Auxiliar para inserir a lista inicial de CDs
for cd in cds:
    insert(cd)


# --------------------------- Home Page - Index - Lista de CDs -----------------------------
# ----------------------------------------------------FRONTEND
@app.route('/', methods=['GET'])
def index_view():
    res = requests.get('http://localhost:5000/api/cds')
    ps = json.loads(res.content)
    return render_template('index.html', cds=ps)

# ----------------------------------------------------BACKEND
@app.route('/api/cds', methods=['GET'])
def api_get_cds():
    ps = find_all()
    return json.dumps(ps)

# ------------------ Lista de Autores - Informações Adicionais -----------------------------
# ----------------------------------------------------FRONTEND
@app.route('/autores', methods=['GET'])
def info_ad_view():
	res = requests.get('http://localhost:5000/api/autores')
	ss = json.loads(res.content)
	return render_template('info_ad_view.html', autores=ss)

# ----------------------------------------------------BACKEND
@app.route('/api/autores', methods=['GET'])
def api_get_autores():
    ss = autores
    return json.dumps(ss)

# ---------------------------------------------------- View CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/cds/<title>', methods=['GET'])
def get_cd_view(title):
    res = requests.get('http://localhost:5000/api/cds/' + title)
    cd = json.loads(res.content)
    return render_template('cd_view.html', p=cd)

# ----------------------------------------------------BACKEND
@app.route('/api/cds/<title>', methods=['GET'])
def api_get_cd(title):
    p = find_one(title)
    return json.dumps(p)

# ------------------------------------------------- Add New CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/cds/novocd')
def new_cd_view():
    return render_template('add_cd_view.html')

@app.route('/cds/novocd',methods=['POST'])
def post_cd():
    data = dict(request.form)
    requests.post('http://localhost:5000/api/cds/novocd', data=data)
    return redirect('http://localhost:5000/')
# ----------------------------------------------------BACKEND

@app.route('/api/cds/novocd',methods=['POST'])
def api_post_cd():
    data = dict(request.form)
    insert(data)
    return json.dumps(find_all())

# -------------------------------------------------  Apagar CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/delete/<title>', methods=['POST'])
def delete_cd(title):
    requests.post('http://localhost:5000/api/cds/'+ title)
    return redirect('http://localhost:5000/')

# ----------------------------------------------------BACKEND
@app.route('/api/cds/<title>', methods=['POST'])
def api_delete_cd(title):
    p = delete(title)
    return json.dumps(p)

# ----------------------------------------------- Atualizar CD --------------------------------
# ----------------------------------------------- FRONTEND -------------------------
@app.route('/update/<title>', methods=['POST'])
def update_cd(title):
    data = dict(request.form)
    requests.post('http://localhost:5000/api/cds/'+ title, data=data)
    return redirect('http://localhost:5000/cds/'+ title)

# ----------------------------------------------- BACKEND -----------------------
@app.route('/api/cds/<title>', methods=['POST'])
def api_update_cd(title):
    data = dict(request.form)
    insert(data)
    return json.dumps(find_all())

# ----------------------------------------------- Procurar CD ---------------------------------
@app.route('/', methods=['POST'])
def procura_cd():
    userinput = request.form.get('userinput')                       # Retorna o que o user põe no editbox
    res = requests.get('http://localhost:5000/api/cds')             # Faz o request á API dos cds
    ps = json.loads(res.content)                                    # conjunto de cds existentes
    lista_cds_encontrados=[]

    for title in ps:                                                # Por cada CD encontrado
        cd=find_one(title)
        res = requests.get('http://localhost:5000/api/cds/'+ title)
        cd = json.loads(res.content)                                 # Encontra o cd por titulo
        conteudo=cd                                                  # Vai buscar o conteudo do cd
        res1=re.findall(rf"(?i)\b{userinput}\b",str(conteudo))          # Percorre á procura do userinput no conteudo
        if res1:                                                     # Se for possivel correr o res
            if title not in lista_cds_encontrados:                   # Se o titulo nao estiver na lista que foi armazenando os encontrados
                lista_cds_encontrados.append(title)                  # Adiciona o titulo á lista
    print(lista_cds_encontrados)

    if (len(lista_cds_encontrados) == 1):
        res2 = requests.get('http://localhost:5000/api/cds/' + lista_cds_encontrados[0])
        cd = json.loads(res2.content)
        print (cd)
        return render_template('cd_view.html', p=cd) # com o cd

    else if (len(lista_cds_encontrados)>1):
        res3 = requests.get('http://localhost:500/api/resultados')
        cds= json.loads(res3.content)
        print(cds)
        return render_template('search_resultas.html', p=cds ) # Lista de encontrados ( titulo com link )

    if not lista_cds_encontrados:
        flash ('No results found!')
        return redirect ('/') # Não encontrado