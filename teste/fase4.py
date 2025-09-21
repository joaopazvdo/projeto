import pygame
from random import randint
#from utils import funcoes_principais
#from utils import classes
#from utils import arquivo_cores
#from classes import Jogador
#from classes import Retangulo
#from classes import Tesouro
#from classes import Tela
#from funcoes_principais import fim
#from funcoes_principais import esquerda
#from funcoes_principais import direita
#from arquivo_cores import cores
#from funcoes_principais import roda_perdeu
#from funcoes_principais import roda_ganhou
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Jogador
from utils.classes import Retangulo
from utils.classes import Tesouro
from utils.funcoes_principais import fim
from utils.funcoes_principais import esquerda
from utils.funcoes_principais import direita
from utils.funcoes_principais import roda_ganhou
from utils.funcoes_principais import roda_perdeu
from tela_ganhou import tela_ganhou
from tela_perdeu import tela_perdeu

def desenha_jogo(TELA, jogador, margens, obstaculos, tesouro, mar, pontuacao):
    TELA.tela.fill(TELA.cor)
    if tesouro.aparece:
        pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    for obstaculo in obstaculos:
        pygame.draw.rect(TELA.tela, obstaculo.cor, obstaculo.retangulo)
    for d in margens:
        pygame.draw.rect(TELA.tela, margens[d].cor, margens[d].retangulo)
    pygame.draw.rect(TELA.tela, mar.cor, mar.retangulo)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    TELA.tela.blit(texto, ((TELA.LARGURA - texto.get_size()[0]) // 2, 0))


def cria_obstaculos(TELA):
    conjuntos_de_obstaculo = {}
    conjuntos_de_obstaculo[-1] = [Retangulo(30, -32, 60, 32, TELA)]

    conjuntos_de_obstaculo[0] = [Retangulo(10, -32, 60, 32, TELA)]

    conjuntos_de_obstaculo[1] = [Retangulo(20, -32, 60, 32, TELA)]

    conjuntos_de_obstaculo[2] = [Retangulo(12.3, -20, 34.25, 20, TELA),
                                 Retangulo(53.45, -20, 34.25, 20, TELA)]

    conjuntos_de_obstaculo[3] = [Retangulo(12.3, -20, 22.8, 20, TELA),
                                 Retangulo(64.8, -20, 22.8, 20, TELA),
                                 Retangulo(38.55, -55, 22.8, 20, TELA)]

    conjuntos_de_obstaculo[4] = [Retangulo(10, -20, 40, 10, TELA),
                                 Retangulo(50, -50, 40, 10, TELA),
                                 Retangulo(10, -80, 40, 10, TELA),
                                 Retangulo(50, -110, 40, 10, TELA)]

    conjuntos_de_obstaculo[5] = [Retangulo(12.3, -20, 22.8, 20, TELA),
                                 Retangulo(64.8, -20, 22.8, 20, TELA),
                                 Retangulo(38.55, -60, 22.8, 20, TELA),
                                 Retangulo(12.3, -100, 22.8, 20, TELA),
                                 Retangulo(64.8, -100, 22.8, 20, TELA)]
    for c in conjuntos_de_obstaculo:
        for e in conjuntos_de_obstaculo[c]:
            e.define_velocidade(0.3)
            e.cor = cores['madeira'] if c in [4,-1,0] else cores['pedra']
    return conjuntos_de_obstaculo


def cria_tesouros(TELA):
    tesouros = {}
    tesouros[-1] = Tesouro(randint(10, 27), randint(-32, 0), 2.3, 4.1,TELA) 
    tesouros[0] = Tesouro(randint(70, 87), randint(-32, 0), 2.3, 4.1, TELA)
    selecao = randint(0,1)
    if selecao:
        tesouros[1] = Tesouro(randint(10, 15), randint(-32, 0), 2.3, 4.1, TELA)
        tesouros[3] = Tesouro(randint(23, 35), -55, 2.3, 4.1, TELA)
        tesouros[4] = Tesouro(30.9, -47.05, 2.3, 4.1, TELA)
    else:
        tesouros[1] = Tesouro(randint(80, 85), randint(-32, 0), 2.3, 4.1, TELA)
        tesouros[3] = Tesouro(randint(62, 87), -55, 2.3, 4.1, TELA)
        tesouros[4] = Tesouro(55, -77.05, 2.3, 4.1, TELA)
    tesouros[2] = Tesouro(48.85, -12.05, 2.3, 4.1, TELA) 
    tesouros[5] = tesouros[3]
    for c in tesouros:
        tesouros[c].define_velocidade(0.3)
    return tesouros


def chegando_no_mar(mar, rodando, ganhou):
    if mar.retangulo.y < 0:
        mar.move_constante_para_baixo()
    else:
        ganhou = True
        rodando = False
    return rodando, ganhou

def movimentacao_jogador(jogador, margens):
    keys = pygame.key.get_pressed()
    if jogador.retangulo.x + jogador.largura < margens['direita'].retangulo.x:
        direita(keys, jogador)
    if jogador.retangulo.x > margens['esquerda'].largura:
        esquerda(keys, jogador)


def movimentacao_obstaculos(TELA, jogador, obstaculos, tesouros, c, rodando, perdeu):
    for obstaculo in obstaculos[c]:
        obstaculo.move_constante_para_baixo()
        if obstaculo.retangulo.colliderect(jogador.retangulo):
            perdeu = True
            rodando = False
        if obstaculos[c][len(obstaculos[c])-1].retangulo.y >= TELA.ALTURA:
            obstaculos = cria_obstaculos(TELA)
            tesouros = cria_tesouros(TELA)
            c = randint(-1,5)
    return rodando, perdeu, c, obstaculos, tesouros


def movimentacao_tesouro(jogador, tesouro, pontuacao):
    if jogador.retangulo.colliderect(tesouro.retangulo):
        pontuacao += 1 if tesouro.aparece else 0
        tesouro.aparece = False
    tesouro.move_constante_para_baixo()
    return pontuacao


def fase4():
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['mar']

    tesouros = cria_tesouros(TELA)

    margens = {}
    margens['esquerda'] = Retangulo(0,0,10,100,TELA)
    margens['direita'] = Retangulo(90,0,10,100, TELA)
    for c in margens:
        margens[c].cor = cores['floresta_tropical']

    obstaculos = cria_obstaculos(TELA)
    c = randint(-1,5)

    mar = Retangulo(0, -100, 100, 100, TELA)
    mar.cor = cores['mar']
    mar.define_velocidade(0.3)

    jogador = Jogador(48.85, 75, 2.3, 4.1, TELA)
    jogador.define_velocidade(0.5)

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    PONTUACAO_MAXIMA = 3
    rodando = True
    perdeu = False
    ganhou = False
    while rodando:
        desenha_jogo(TELA, jogador, margens, obstaculos[c], tesouros[c], mar, pontuacao)
        if fim(): 
            return 'Tela inicial', False
        movimentacao_jogador(jogador, margens)
        rodando, perdeu, c, obstaculos, tesouros = movimentacao_obstaculos(TELA, jogador,obstaculos, 
                                                     tesouros, c, rodando, perdeu)
        if not rodando: break
        pontuacao = movimentacao_tesouro(jogador, tesouros[c], pontuacao)
        if not rodando: break
        if pontuacao >= PONTUACAO_MAXIMA:
            rodando, ganhou = chegando_no_mar(mar, rodando, ganhou)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    if perdeu:
        return tela_perdeu(), ganhou

    if ganhou:
        return tela_ganhou(), ganhou

        
if __name__ == '__main__':
    fase4()
