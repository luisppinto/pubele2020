import shelve


def find_all():
    with shelve.open('relatorios.db') as s:
        return list(s.keys())


def find_one(relatorio):
    with shelve.open('relatorios.db') as s:
        return { 'relatorio': relatorio, 'significado': s[relatorio] }


def insert(relatorio_data):
    with shelve.open('relatorios.db', writeback=True) as s:
        s[relatorio_data['relatorio']] = relatorio_data['significado']
        return list(s.keys())