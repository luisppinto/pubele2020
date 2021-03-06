import shelve

proverbios = [
    {
        'id': 0,
        'title': 'Mais vale tarde do que nunca.',
        'significado': 'Atrasei-me, mas ao menos cheguei.'
    },
    {
        'id': 1,
        'title': 'Mês de abril, arroz de caril.',
        'significado': 'É bom comer arroz de caril em abril.'
    },
    {
        'id': 2,
        'title': 'Quem vai à guerra dá e leva',
        'significado': 'Não esperes que as tuas ações não tenham consequências.'
    },
    {
        'id': 3,
        'title': 'Em tempo de guerra, qualquer buraco é trincheira',
        'significado': 'Nunca rejeites ajuda.'
    }
]

with shelve.open('proverbios.bd') as s:
    s['p0'] = {
        'id': 0,
        'title': 'Mais vale tarde do que nunca.',
        'significado': 'Atrasei-me, mas ao menos cheguei.'
    }

pessoas = [
    'Pedro',
    'Beatriz',
    'Paulo'
]
