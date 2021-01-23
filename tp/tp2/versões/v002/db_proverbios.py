# Shelve

import shelve

def find_all():
	with shelve.open('proverbios.db') as s:
		return list(s.keys())

def find_one(descricao):
	with shelve.open('proverbios.db') as s:
		return {'descricao':descricao, 'significado':s[descricao]}

def insert(proverbio):
	with shelve.open('proverbios.db', writeback=True) as s:
		s[proverbio['descricao']] = proverbio['significado']
	return s 