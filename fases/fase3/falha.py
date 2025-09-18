import pygame
import sys

from biomas import verifica_fim
sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tela
from classes import Tesouro
from classes import Obstaculo_Fase2
from biomas import entrar_no_bioma


def movimentacao(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()


def desenha_inicio(TELA, jogador, entradas):
    TELA.tela.fill(TELA.cor)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo) 
    for c in entradas:
        pygame.draw.rect(TELA.tela, entradas[c].cor, entradas[c].retangulo)
    

def entrar_no_inicio(TELA, jogador, entradas):
    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    while rodando:
        desenha_inicio(TELA, jogador, entradas)
        rodando = verifica_fim
            
        keys = pygame.key.get_pressed()
        movimentacao(keys, jogador)
        for bioma in entradas:
            if entradas[bioma].retangulo.colliderect(jogador.retangulo):
                return bioma
        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)

    jogador = Jogador(50, 50, 2.3, 4.1, TELA)
    jogador.define_velocidade(0.5)
    
    entradas = {}
    entradas['manguezal'] = Obstaculo_Fase2(0, 0, 10, 10, TELA)
    entradas['deserto'] = Obstaculo_Fase2(90, 0, 10, 10, TELA)
    entradas['savana'] = Obstaculo_Fase2(0, 90, 10, 10, TELA)
    entradas['floresta_tropical'] = Obstaculo_Fase2(90, 90, 10, 10, TELA)

    entrar_no_inicio(TELA, jogador, entradas)
    pontuacao = 0
    rodando = True
#    while rodando:
#        bioma = entrar_no_inicio(TELA, jogador, entradas)
#        if bioma == 'manguezal':
#            em_baixo = True
#        if bioma == 'deserto':
#            em_baixo = True
#        if bioma == 'savana':
#            em_baixo = False
#        if bioma == 'floresta_tropical':
#            em_baixo = False
#        pontuacao = entrar_no_bioma(pontuacao, cores[bioma], em_baixo) 
#        rodando = verifica_fim
    pygame.quit()
        


if __name__ == '__main__':
       main()
