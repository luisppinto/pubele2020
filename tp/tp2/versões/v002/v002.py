from flask import Flask, render_template, request, redirect
import json
import requests
# from re import *
# from povoamento import relatorios, pessoas
# import db
from db_proverbios import *  

app = Flask(__name__) # required

	# 1º temos a defenição inicial do conteudo de cada relatório 
	# é desenvolvido a partir de uma lista de dicionários
	# o dicionario é constituido por key e value 
	# No caso de proverbios 'key'= descricao,'value'= significado

proverbios = [ {'descricao': 'quem tudo quer tudo perde', 'significado':'nao sejas ambicioso demais'},
	{'descricao': 'Quem vai a guerra da e leva', 'significado':'As ações tem consequencias'}]

    # Key = e value = 
# relatório1 = [

	# {'titulo': 'TP1- Internet introduction and Satellite Communications'},
	# {'titulo': 'Introdução','text': 'A Internet é uma rede de redes de computadores que trocam informações entre si.Tanto a administração quanto a operação da Internet são descentralizadas, apenas alguns serviços tais como definição de padrões e pesquisas e ainda a distribuição dos endereços são administrados por instituições regulamentadoras. Uma das principais instituições é a Internet Engineering Task Force (IETF).A IETF é um grupo de pesquisadores responsáveis pelo desenvolvimento de padrões a serem divulgados através de Request For Comments (RFCs). A comunicação via satélite utiliza ondas de rádio, enviadas por satélites artificiais em órbita da Terra, como forma de transmitir dados.Este tipo de comunicação tem a vantagem de poder estabelecer contato com navios e aviões, algo impossível de ser feito por meio de cabos. Também mensagens enviadas por meio de satélites podem chegar até as regiões mais isoladas do planeta, mesmo que o local não tenha infra-estrutura de cabos. Relativamente à comunicação via satélite, esta tornou possível vários progressos, dentro dos quais a área das geociências, as telecomunicações e o transporte aéreo.  Isto melhorou consideravelmente a segurança e o desenvolvimento mundial.'},
	# {'titulo':'Part I : Internet, IETF and RFCS','subtitulo': '1. IETF', 'text': 'IETF permite um funcionamento melhor da Internet ao produzir documentos técnicos relevantes e de alta qualidade que influenciam a maneira como as pessoas projetam, usam e gerenciam a Internet. [1] O trabalho técnico do IETF divide-se por grupos de trabalho, que estão organizados por tópicos em diversas áreas (exemplos: routing, transporte, segurança, etc.), e são geridos pelos respetivos diretores, sendo estes membros do The Internet Engineering Steering Group (IESG). Muito do trabalho do IETF é realizado por mailing lists. Nas suas reuniões, o IETF encoraja à colaboração e desenvolvimento de utilidades, ideias, exemplos de códigos, e soluções que demonstrem implementações práticas dos standards do IETF. O IAB (Internet Architecture Board) e o IRTF (Internet Research Task Force) complementam o trabalho do IETF, fornecendo, respetivamente, uma direção técnica de longo alcance para o desenvolvimento da internet e promovendo pesquisa importante para a evolução da mesma.'}]

	# 2º é necessário a introdução destes dados na BD 
for proverbio in proverbios:
	insert(proverbio)

# for relatorio in relatorios:
   # db.insert(relatorio)

# for pessoa in pessoas:
   # db.insert_p(pessoa)

   # 3º Criação das rotas da app
   # Homepage 
@app.route('/')
def index_view(): 
	return render_template('index.html')

	# Homepage 
	# Conteudo do Homepage -> Barra de Navegação [Botões com links - (Lista de Relatórios | Procurar Relatório | Adicionar Relatório | Remover Relatório | Modificar Relatório | Informações Adicionais )] {html}
	# Esta página deve coincidir com o botão Lista de Relatórios {html}
	# Cada Relatório na página deve ser um link para (Ver Relatório){html}
# @app.route('/')
# def index():
#    ps = db.find_all()
#    pessoas = db.find_all_p()
#    h = []
#    for titulo in ps:
#        relatorio = db.find_one(titulo)
#        for tag in relatorio['hashtags']:
#            if tag not in h:
#                h.append(tag)
#    return render_template('index.html', titles=ps, hashtags=h, pessoas=pessoas)

	# 
@app.route('/proverbios', methods=['GET'])
def get_proverbios_view():

	res = requests.get('http://localhost:5000/api/proverbios')
	ps = json.loads(res.content)

	return render_template('proverbios_view.html', proverbios=ps)

# @app.route('/relatorios', methods=['GET'])
# def get_relatorios():
#    res = requests.get('http://localhost:5000/api/relatorios')
#    ps = json.loads(res.content)
#    return render_template('relatorios_view.html', title='Relatórios', relatorios=ps)

@app.route('/proverbios', methods=['POST'])
def post_proverbio_view():

	data = dict(request.form)
	requests.post('http://localhost:5000/api/proverbios', data=data)

	return redirect('http://localhost:5000/proverbios')

# @app.route('/relatorios', methods=['POST'])
# def post_relatorio():
#    data = dict(request.form)
#    requests.post('http://localhost:5000/api/relatorios', data=data)
#    return redirect('http://localhost:5000/relatorios')

@app.route('/proverbios/<proverbio>', methods=['GET'])
def get_proverbio_view(proverbio):

	res = requests.get('http://localhost:5000/api/proverbios/'+proverbio)
	p = json.loads(res.content)
    
	return render_template('proverbio_view.html', p=p)

# @app.route('/relatorios/<titulo>', methods=['GET'])
# def get_relatorio(titulo):
#    res = requests.get('http://localhost:5000/api/relatorios/' + titulo)
#    p = json.loads(res.content)

#    return render_template('relatorio_view.html', p=p)

# @app.route('/relatorios/procura')
# def procura_view():
#    return render_template('procura_view.html')

# @app.route('/pessoas/<nome>', methods=['GET'])
# def get_pessoa(nome):
#    res = requests.get('http://localhost:5000/api/pessoas/' + nome)
#    p = json.loads(res.content)
#    return render_template('pessoa_view.html', p=p)

# @app.route('/relatorios/resultado', methods=['POST'])
# def relatorios_resultado():
#    pesquisa = request.form.get('procura').replace('#','')
#    res = requests.get('http://localhost:5000/api/relatorios')
#    ps = json.loads(res.content)

#    l = []
#    t = []
#    for titulo in ps:
#        relatorio = db.find_one(titulo)
#        text = relatorio['description']
#        res = findall(rf"(?i)\b{pesquisa}\b",str(text))
#        if res:
#            if titulo not in l:
#                l.append(titulo)
#                pos = text.index(res[0])
#               if (len(text) >= 500):
#                    t.append(text[pos:pos+len(res[0])+500].replace(res[0],'*'+res[0]+'*'))
#                else:
#                    t.append(text.replace(res[0],'*'+res[0]+'*'))
#    return render_template('resultados_pesquisa_view.html', title=rf'Relatórios que contêm o padrão"{pesquisa}"', relatorios=l)


@app.route('/api/proverbios', methods=['GET'])
def api_get_proverbios():

	ps = find_all()
	return json.dumps(ps)

# api para relatorios

# @app.route('/api/relatorios', methods=['GET'])
# def api_get_relatorios():
#    ps = db.find_all()
#    return json.dumps(ps)

@app.route('/api/proverbios', methods=['POST'])
def api_post_proverbio():
    
	data = dict(request.form)
	insert(data)
	return json.dumps(data)

#@app.route('/api/relatorios', methods=['POST'])
# def api_post_relatorio():
#    data = dict(request.form)

#    h = data['hashtags'].split(' ')
#    l = data['references'].split(' ')

#    data['references'] = l
#    data['hashtags'] = h
#    data['authors'] = [{'name': 'Bruno Rebelo Lopes', 'number': '57768'},{'name':'Morgana Sacramento Ferreira','number':'93779'},{'name':'Luís Pedro da Silva Pinto','number':'83016'}]

#    db.insert(data)

#    return json.dumps(db.find_all())

@app.route('/api/proverbios/<proverbio>', methods=['GET'])
def api_get_proverbio(proverbio):

	p = find_one(proverbio)
	return json.dumps(p)

# @app.route('/api/relatorios/<titulo>', methods=['GET'])
# def api_get_relatorio(titulo):
#    p = db.find_one(titulo)
#    return json.dumps(p)

# api para autores
# @app.route('/api/pessoas', methods=['GET'])
# def api_get_pessoas():
#    ps = db.find_all_p()
#    return json.dumps(ps)
# @app.route('/api/pessoas/<nome>', methods=['GET'])
# def api_get_pessoas(nome):
#     p = db.find_one_p(nome)
#   return json.dumps(p)