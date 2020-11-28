'''table
    tbody
    tr
        td
        th'''

from bs4 import BeautifulSoup as bs
import csv

def extrai_tabelas(file_html): #vai extrair as tabelas do html

    arvore = bs(file_html,"html.parser") #Abre o html com o BeautifulSoup

    return arvore.find_all("table")

def table_to_csv(table):

    linhas = []

    for linha in table.find_all("tr"):
        uma_linha = []
        for coluna in table.find_all(["td","th"]):
            uma_linha.append(coluna.text.strip())
        linhas.append(uma_linha)

    with open(rf"out_tabela{i}.csv","w") as f:
        writer = csv.writer(f)
        writer.writerows(linhas)

'''with open("tabelas.html") as f:
    content = f.read()
    tabelas = extrai_tabelas(content)
    for i,tabela in enumerate(tabelas):
        table_to_csv(tabela,i)'''
