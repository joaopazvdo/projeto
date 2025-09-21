import pygame
#from utils import funcoes_principais
#from utils import classes
#from utils import arquivo_cores
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Jogador
from utils.classes import Retangulo
from random import randint
from utils.funcoes_principais import fim
from utils.funcoes_principais import pulo_e_queda
#from utils.funcoes_principais import roda_ganhou
#from utils.funcoes_principais import roda_perdeu
from tela_ganhou import tela_ganhou
from tela_perdeu import tela_perdeu

def desenha_jogo(TELA, jogador, obstaculos, planice):
    TELA.tela.fill(TELA.cor)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    for montanha in obstaculos:
        pygame.draw.rect(TELA.tela, montanha.cor, montanha.retangulo)

    if obstaculos == []:
        pygame.draw.rect(TELA.tela, planice.cor, planice.retangulo)


def cria_lista_obstaculos(num_obstaculos, distancia_entre_obstaculos, TELA):
    obstaculos = num_obstaculos * [None]
    x_obstaculo = 100
    for i in range(num_obstaculos):
        selecao = randint(0, 3) 
        montanha = Retangulo(x_obstaculo, 20, 20.3, 80, TELA)
        planalto = Retangulo(x_obstaculo, 35, 65, 65, TELA)
        if selecao == 0:
            obstaculo = planalto

        else:
            obstaculo = montanha

        obstaculos[i] = obstaculo
        x_obstaculo += distancia_entre_obstaculos
    return obstaculos


def mecanica_fase2(TELA, jogador, obstaculos, planice):
    rodando = True
    perdeu = False
    ganhou = False

    if obstaculos:
        keys = pygame.key.get_pressed()
        pulo_e_queda(keys, jogador)

    removidos = 0
    for i in range(len(obstaculos)):
        i -= removidos

        if obstaculos[i].retangulo.colliderect(jogador.retangulo):
            perdeu = True
            rodando = False

        obstaculos[i].move_constante_para_esquerda()
        if obstaculos[i].retangulo.x + obstaculos[i].largura <= 0:
            obstaculos.pop(i)
            removidos += 1


    if jogador.retangulo.y <= 0:
        print('a')
        perdeu = True
        rodando = False

    if jogador.retangulo.y >= TELA.ALTURA - jogador.altura:
        perdeu = True
        rodando = False

    if obstaculos == []:
        if jogador.retangulo.x < planice.retangulo.x * 150/100:
            jogador.retangulo.x += planice.velocidade

        if jogador.retangulo.y + jogador.altura < planice.retangulo.y:
            jogador.retangulo.y += planice.velocidade * 0.50

        if planice.retangulo.x > TELA.LARGURA * 50/100:
            planice.move_constante_para_esquerda()


    if planice.retangulo.colliderect(jogador.retangulo):
        ganhou = True
        rodando = False

    return rodando, ganhou, perdeu


def fase2():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['ceu']

    jogador = Jogador(7.8, 30, 2.3, 4.1, TELA)
    jogador.gravidade = (TELA.ALTURA/600) * 0.25
    obstaculos = cria_lista_obstaculos(1, 75 + 20.3, TELA) 
    planice = Retangulo(100, 95.9, 50, 4.1, TELA)

    clock = pygame.time.Clock()
    FPS = 60

    rodando = True
    ganhou = False
    perdeu = False

    while rodando:
        desenha_jogo(TELA, jogador, obstaculos, planice)
        if fim(): 
            return 'Tela inicial', False
        rodando, ganhou, perdeu = mecanica_fase2(TELA, jogador, obstaculos, planice)
        if not rodando: break
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    if perdeu:
        return tela_perdeu(), ganhou

    if ganhou:
        return tela_ganhou(), ganhou

    

if __name__ == '__main__':
    print(fase2())
