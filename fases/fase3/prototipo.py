import pygame
import sys

sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tela
from classes import Tesouro
from classes import Retangulo
from funcoes_principais import cima_baixo_esquerda_direita
from funcoes_principais import cima_baixo_esquerda_direita_no_mapa
from funcoes_principais import fim
from funcoes_principais import roda_ganhou

def desenha_inicio(TELA, jogador, entradas, pontuacao):
    TELA.tela.fill(TELA.cor)
    for bioma in entradas:
        pygame.draw.rect(TELA.tela, entradas[bioma].cor, entradas[bioma].retangulo)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['preto'])
    tamanho_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))


def desenha_bioma(TELA, ambiente, jogador, lista_de_tesouros, saida, pontuacao):
    TELA.cor = cores[ambiente]
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)
    
    if lista_de_tesouros:
        pygame.draw.rect(TELA.tela, lista_de_tesouros[0].cor, lista_de_tesouros[0].retangulo)
        pygame.draw.rect(TELA.mapa, lista_de_tesouros[0].cor, lista_de_tesouros[0].no_mapa)

    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.no_mapa)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))


def regras_biomas(jogador, lista_de_tesouros, saida, ambiente, pontuacao):
    if lista_de_tesouros:
        if jogador.retangulo.colliderect(lista_de_tesouros[0].retangulo):
            lista_de_tesouros.pop(0)
            pontuacao += 1

    if jogador.retangulo.colliderect(saida.retangulo):
        ambiente = 'inicio'

    return pontuacao, ambiente


def cria_jogadores(TELA):
    jogadores = {}
    jogadores['inicio'] = Jogador(48.85, 47.95,2.3, 4.1, TELA)
    jogadores['inicio'].define_velocidade(0.5)

    jogadores['manguezal'] = Jogador(88.85, 85.9,2.3, 4.1, TELA)
    jogadores['manguezal'].define_velocidade(0.5)
    jogadores['manguezal'].posicao_inicial =  {'x':jogadores['manguezal'].retangulo.x, 'y':jogadores['manguezal'].retangulo.y}

    jogadores['deserto'] = Jogador(10, 85.9,2.3, 4.1, TELA)
    jogadores['deserto'].define_velocidade(0.5)
    jogadores['deserto'].posicao_inicial =  {'x':jogadores['deserto'].retangulo.x, 'y':jogadores['deserto'].retangulo.y}

    jogadores['savana'] = Jogador(88.85, 10,2.3, 4.1, TELA)
    jogadores['savana'].define_velocidade(0.5)
    jogadores['savana'].posicao_inicial =  {'x':jogadores['savana'].retangulo.x, 'y':jogadores['savana'].retangulo.y}

    jogadores['floresta_tropical'] = Jogador(10, 10,2.3, 4.1, TELA)
    jogadores['floresta_tropical'].define_velocidade(0.5)
    jogadores['floresta_tropical'].posicao_inicial =  {'x':jogadores['floresta_tropical'].retangulo.x, 'y':jogadores['floresta_tropical'].retangulo.y}

    return jogadores


def cria_listas_de_tesouros(TELA):
    tesouros = {}
    tesouros['manguezal'] = [None for _ in range(4)]
    for i in range(len(tesouros['manguezal'])):
        tesouros['manguezal'][i] = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
        tesouros['manguezal'][i].cor = cores['dourado'] 
    
    tesouros['deserto'] = [None for _ in range(4)]
    for i in range(len(tesouros['deserto'])):
        tesouros['deserto'][i] = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
        tesouros['deserto'][i].cor = cores['dourado'] 
    
    tesouros['savana'] = [None for _ in range(4)]
    for i in range(len(tesouros['savana'])):
        tesouros['savana'][i] = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
        tesouros['savana'][i].cor = cores['dourado'] 

    tesouros['floresta_tropical'] = [None for _ in range(4)]
    for i in range(len(tesouros['floresta_tropical'])):
        tesouros['floresta_tropical'][i] = Tesouro(90, 0, 2.3, 4.1, TELA)
        tesouros['floresta_tropical'][i].cor = cores['dourado'] 

    return tesouros


def cria_saidas(TELA):
    saidas = {}
    saidas['manguezal'] = Retangulo(90, 90, 10, 10, TELA)
    saidas['deserto'] = Retangulo(0, 90, 10, 10, TELA)
    saidas['savana'] = Retangulo(90, 0, 10, 10, TELA)
    saidas['floresta_tropical'] = Retangulo(0, 0, 10, 10, TELA)
    for b in saidas:
        saidas[b].cor = cores['branco']
    return saidas


def cria_entradas(TELA):
    entradas = {}
    entradas['manguezal'] = Retangulo(0, 0, 10, 10, TELA)
    entradas['deserto'] = Retangulo(90, 0, 10, 10, TELA)
    entradas['savana'] = Retangulo(0, 90, 10, 10, TELA)
    entradas['floresta_tropical'] = Retangulo(90, 90, 10, 10, TELA)
    return entradas


def main():
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)

    jogadores = cria_jogadores(TELA)
    tesouros = cria_listas_de_tesouros(TELA)
    saidas = cria_saidas(TELA)

    entradas = cria_entradas(TELA)
    for b in entradas:
        entradas[b].cor = cores[b]

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    ambiente = 'inicio'
    rodando = True
    ganhou = False
    while rodando:
        keys = pygame.key.get_pressed()
        if ambiente == 'inicio':
            TELA.cor = cores['branco']
            desenha_inicio(TELA, jogadores['inicio'], entradas, pontuacao)
            cima_baixo_esquerda_direita(keys, jogadores['inicio'])
            for b in entradas:
                if jogadores['inicio'].retangulo.colliderect(entradas[b].retangulo):
                    ambiente = b
        else:
            desenha_bioma(TELA, ambiente, jogadores[ambiente], 
                          tesouros[ambiente], saidas[ambiente], pontuacao)
            pontuacao, ambiente = regras_biomas(jogadores[ambiente], tesouros[ambiente], 
                                                saidas[ambiente], ambiente, pontuacao)

        if ambiente == 'manguezal':
            jogadores['inicio'].define_posicao(11,11)
            TELA.cor = cores[ambiente]
            TELA.cria_mapa((1/5), 0, 0)
            TELA.cor_mapa = cores['mapa']
            jogadores['manguezal'].cria_no_mapa()
            saidas['manguezal'].cria_no_mapa()
            for tesouro in tesouros['manguezal']:
                tesouro.cria_no_mapa()
            cima_baixo_esquerda_direita(keys, jogadores['manguezal'])
            cima_baixo_esquerda_direita_no_mapa(keys, jogadores['manguezal'])

        if ambiente == 'deserto':
            jogadores['inicio'].define_posicao(87.7,11)
            TELA.cor = cores[ambiente]
            TELA.cria_mapa((1/5), 80, 0)
            TELA.cor_mapa = cores['mapa']
            jogadores['deserto'].cria_no_mapa()
            saidas['deserto'].cria_no_mapa()
            for tesouro in tesouros['deserto']:
                tesouro.cria_no_mapa()
            cima_baixo_esquerda_direita(keys, jogadores['deserto'])
            cima_baixo_esquerda_direita_no_mapa(keys, jogadores['deserto'])

        if ambiente == 'savana':
            jogadores['inicio'].define_posicao(11,85.9)
            TELA.cor = cores[ambiente]
            TELA.cria_mapa((1/5), 0, 80)
            TELA.cor_mapa = cores['mapa']
            jogadores['savana'].cria_no_mapa()
            saidas['savana'].cria_no_mapa()
            for tesouro in tesouros['savana']:
                tesouro.cria_no_mapa()
            cima_baixo_esquerda_direita(keys, jogadores['savana'])
            cima_baixo_esquerda_direita_no_mapa(keys, jogadores['savana'])

        if ambiente == 'floresta_tropical':
            jogadores['inicio'].define_posicao(87.7,85.9)
            TELA.cor = cores[ambiente]
            TELA.cria_mapa((1/5), 0, 80)
            TELA.cor_mapa = cores['mapa']
            jogadores['floresta_tropical'].cria_no_mapa()
            saidas['floresta_tropical'].cria_no_mapa()
            for tesouro in tesouros['floresta_tropical']:
                tesouro.cria_no_mapa()
            cima_baixo_esquerda_direita(keys, jogadores['floresta_tropical'])
            cima_baixo_esquerda_direita_no_mapa(keys, jogadores['floresta_tropical'])
            
        if fim(): break
        if [v for v in tesouros.values()] == [[],[],[],[]]:
            ganhou = True
            rodando = False
            break
        pygame.display.flip()
        clock.tick(FPS)
    if ganhou:
        roda_ganhou(TELA)
    pygame.quit()
                                                  

if __name__ == '__main__':
    main()
