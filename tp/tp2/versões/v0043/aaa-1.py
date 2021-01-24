# Lista CDs
cds = {'titulo1': {
        'id': '0',
        'artist': 'artista',
        'artwork': 'url.jpg',
        'country': 'PT',
        'company': 'Espacial',
        'description': 'blablbao.',
        'year': '2006'},
       'titulo2': {'id': '1',
        'artist': 'Bonnie Tyler',
        'artwork': 'url.jpggg',
        'country': 'GB',
        'company': 'CBS Records',
        'description': 'blalbalblbalb.',
        'year': '1988'}}

titulo = 'Aja'
novocd = {
        'id': '2',
        'artist': 'Steely Dan',
        'artwork': 'url.jpg',
        'country': 'US',
        'company': 'Harvest',
        'description': 'blalbalbal.',
        'year': '1973'}

# SHELVE -------------------------------------------------------------------------------
import shelve

# Adiciona uma lista de CDs ao SHELVE 
def adiciona_CDs_de_lista():
  with shelve.open('cds.db',writeback=True) as s:
    for cd in cds:
      s[cd]=cds[cd]
      # print (cd) # id cd
      # print (s['cd']) 
      # print (s['cd']['title'])
      # print (s['cd']['artist'])
    # print(list(s.keys()))
    s.close() 

# Adiciona um CD dicionao SHELVE 
def novo_CD(titulo,novocd):
  with shelve.open('cds.db', writeback=True) as s:
    s[titulo]=novocd

    s.close()
    
# Ver Keys da SHELVE
# ['cd']
def ver_keys():
  with shelve.open('cds.db') as s:
    print (list(s.keys()))
    s.close()
    
# Ver Values da SHELVE 
def ver_values():
  with shelve.open('cds.db') as s:
    print (list(s.values()))
    s.close()

# Ver Items da SHELVE 

def ver_items():
  with shelve.open('cds.db') as s:
    print (list(s.items()))
    s.close()

def sacar_info():
  with shelve.open('cds.db') as s:
    for key in s:
      print (key) # chave = titulo 
      print (s[key]) # value = restantes informaçoes do CD em BULK
      print (s[key]['year'])# para ir á propria tag ano nesse cd
      
titulo='Aja'
def apagar_info(titulo):
  with shelve.open('cds.db', writeback=True) as s:  
     del s[titulo]
      
# def main ():
  # adicionalista()
  # removecdlista()
  # adiciona_CDs_de_lista() # Fazer 1º
  # novo_CD(titulo,novocd)
  # ver_keys()
  # ver_values()
  # ver_items()
  # sacar_info()
  # apagar_info(titulo)
# main()
  
