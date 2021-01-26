import shelve

def find_all():
    with shelve.open('cds.db') as s:
        return list(s.keys())

def find_one(title):
    with shelve.open('cds.db') as s:
        return s[title]

def insert(cd):
    with shelve.open('cds.db', writeback=True) as s:
        s[cd['title']] = cd
        return s

def delete(title):
	with shelve.open('cds.db', writeback=True) as s:
		del s[title]
		return list(s.keys())