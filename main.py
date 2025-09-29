import pygame
from utils.classes import Tela
from fase1 import fase1
from fase2 import fase2
from fase3 import fase3
from fase4 import fase4
from telas import tela_inicial
from historia import apresenta_historia
from importacao import resource_path

def le_memoria():
        with open(resource_path('memoria.txt'), 'r', encoding='utf-8') as f:
            for linha in f:
                return linha.strip()


def altera_memoria(texto):
    with open(resource_path('memoria.txt'), 'w', encoding='utf-8') as f:
        f.write(f'{texto}\n')


def main():
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    fase = 'Tela inicial'
    while True:
        comeco = le_memoria()
        if fase == 'Tela inicial' or fase == None:
            fase = tela_inicial(TELA)

        if fase == 'Iniciar':
            fase = comeco

        if fase == 'Reiniciar':
            apresenta_historia(TELA)
            selecionado, ganhou = fase1(TELA)
            if ganhou:
                altera_memoria('Fase 2')
                fase = 'Fase 2' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                altera_memoria('Fase 1')
                fase = 'Fase 1' if selecionado == 'Reiniciar' else selecionado



        if fase == 'Fase 1':
            selecionado, ganhou = fase1(TELA)
            if ganhou:
                altera_memoria('Fase 2')
                fase = 'Fase 2' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 1' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 2':
            selecionado, ganhou = fase2(TELA)
            if ganhou:
                altera_memoria('Fase 3')
                fase = 'Fase 3' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 2' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 3':
            selecionado, ganhou = fase3(TELA)
            if ganhou:
                altera_memoria('Fase 4')
                fase = 'Fase 4' if selecionado == 'Próxima Fase' else selecionado
            if not ganhou:
                fase = 'Fase 3' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Fase 4':
            selecionado, ganhou = fase4(TELA)
            if ganhou:
                fase ='Tela inicial'
            if not ganhou:
                fase = 'Fase 4' if selecionado == 'Reiniciar' else selecionado

        if fase == 'Sair':
            break
    pygame.quit()

if __name__ == '__main__':
    main()
