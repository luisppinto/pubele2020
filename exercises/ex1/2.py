from re import *
import sys

def ex2(palavra):

    with open('dicionario_medico_formatado.txt') as f:

        content = f.readlines() #retorna lista com linhas do ficheiro
        num_oco = 0
        linhas = []
        for i,line in enumerate(content):
            matches = findall(palavra,line) #lista com todas as ocorrências da palavra na linhas

            line = line.rstrip()
            line = sub(palavra,r'@'*palavra,line) #marca a palavra com um @ para ser identificada

            if matches: #se houver match na linha
                num_oco += len(matches)
                linhas.append(line) #guarda a linha

        for l in line:
            print(l+'\n')
        print("Número total de ocorrências da palavra " + palavra +": ", num_oco)

def main():

    palavra = sys.argv[-1]
    ex2(palavra)

if __name__ == '__main__':
    main()
