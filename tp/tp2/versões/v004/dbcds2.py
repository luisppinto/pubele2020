import shelve

def find_all():
    with shelve.open('cds.db') as s:
        return list(s.keys())

def find_one(title):
    with shelve.open('cds.db') as s:
        return {'title':title}

def insert(cd):
    with shelve.open('cds.db', writeback=True) as s:
        s[cd['title']] = cd['artist']
        return s
