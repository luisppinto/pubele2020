'''table
	tbody
	tr
	td
	th'''

from bs4 import BeautifulSoup as bs
import csv


def extrai_tabelas(file_html):

	arvore = bs(file_html,"html.parser")

	return arvore.find_all("table")



def table_to_csv(table,i):

	linhas = []

	for linha in table.find_all("tr"):
		uma_linha = []
		for coluna in linha.find_all(["td","th"]):
			uma_linha.append(coluna.text.strip())
		linhas.append(uma_linha)

	with open(rf"out_tabela{i}.csv",'w') as f:
		writer = csv.writer(f)
		writer.writerows(linhas)



def gera_csv(content):
	tabelas = extrai_tabelas(content)
	for i,tabela in enumerate(tabelas):
		table_to_csv(tabela,i)





