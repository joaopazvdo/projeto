import pygame
#from sys import path
#path.append('fase1')
#path.append('fase2')
#path.append('fase3')
#path.append('fase4')
from fase1 import fase1
from fase2 import fase2
from fase3 import fase3
from fase4 import fase4
from tela_inicial import tela_inicial

def le_memoria():
        with open('memoria.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                return linha.strip()


def altera_memoria(texto):
    with open('memoria.txt', 'w', encoding='utf-8') as f:
        f.write(f'{texto}\n')


def main():
    fase = 'Tela inicial'
    while True:
        comeco = le_memoria()
        if fase == 'Tela inicial' or fase == None:
            fase = tela_inicial()

        if fase == 'Iniciar':
            fase = comeco

        if fase == 'Fase 1':
            selecionado, ganhou = fase1()
            if ganhou:
                altera_memoria('Fase 2')
                fase = 'Fase 2' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 1' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 2':
            selecionado, ganhou = fase2()
            if ganhou:
                altera_memoria('Fase 3')
                fase = 'Fase 3' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 2' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 3':
            selecionado, ganhou = fase3()
            if ganhou:
                altera_memoria('Fase 4')
                fase = 'Fase 4' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 3' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 4':
            selecionado, ganhou = fase4()
            if ganhou:
                altera_memoria('Fase 4')
                fase = 'Fase 4' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 4' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Sair':
            break

if __name__ == '__main__':
    main()
