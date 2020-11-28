
from re import *
import requests
from aula import *
import sys

argumento = sys.argv[1]

if match(r"(http|ftp)",argumento):
	res = requests.get(argumento)
	content = res.content
else:
	with open(argumento) as f:
		content = f.read()

gera_csv(content)
