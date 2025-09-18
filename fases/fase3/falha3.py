import pygame
import sys

sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tela
from classes import Tesouro
from classes import Obstaculo_Fase2
from funcoes_principais import movimentacao
from funcoes_principais import movimentacao_no_mapa
from funcoes_principais import verifica_fim

def desenha_biomas(TELA, jogador, tesouro, pontuacao, saida, entrada_em_baixo):
    jogador.cria_no_mapa()
    tesouro.cria_no_mapa()
    saida.cria_no_mapa()
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    if entrada_em_baixo:
        TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, TELA.ALTURA - tamanho_texto[1]))
        saida.retangulo.y = 0
    else:
        TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))

def desenha_manguezal(TELA, jogador, tesouro, saida, pontuacao):
    TELA.cor = cores['manguezal']
    jogador.cria_no_mapa()
    tesouro.cria_no_mapa()
    saida.cria_no_mapa()
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))


def desenha_deserto(TELA, jogador, tesouro, saida, pontuacao):
    TELA.cor = cores['deserto']
    jogador.cria_no_mapa()
    tesouro.cria_no_mapa()
    saida.cria_no_mapa()
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))


def desenha_savana(TELA, jogador, tesouro, saida, pontuacao):
    TELA.cor = cores['savana']
    jogador.cria_no_mapa()
    tesouro.cria_no_mapa()
    saida.cria_no_mapa()
    saida.retangulo.y = 0
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, TELA.ALTURA - tamanho_texto[1]))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))


def desenha_floresta_tropical(TELA, jogador, tesouro, saida, pontuacao):
    TELA.cor = cores['floresta_tropical']
    jogador.cria_no_mapa()
    tesouro.cria_no_mapa()
    saida.cria_no_mapa()
    saida.retangulo.y = 0
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, TELA.ALTURA - tamanho_texto[1]))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))


def mecanica_biomas(TELA, jogador, tesouro):
    keys = pygame.key.get_pressed()
    movimentacao(keys, jogador)
    movimentacao_no_mapa(keys, jogador)
    if jogador.retangulo.colliderect(tesouro.retangulo):
        tesouro.muda_posicao()
        return 1
    else:
        return 0


def desenha_inicio(TELA, jogador, entradas, pontuacao):
    TELA.tela.fill(TELA.cor)
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['preto'])
    tamanho_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    for bioma in entradas:
        pygame.draw.rect(TELA.tela, entradas[bioma].cor, entradas[bioma].retangulo)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    

def coloca_na_frente_da_saida(jogador, saida, ambiente):
    if ambiente == 'manguezal':
        jogador.retangulo.y = entradas[ambiente].altura + 2
    if ambiente == 'deserto':
        jogador.retangulo.y = entradas[ambiente].altura + 2
    if ambiente == 'savana':
        jogador.retangulo.y = saida
    if ambiente == 'floresta_tropical':
        jogador.retangulo.y = entradas[ambiente].retangulo.y - 5 - jogador.altura
    jogador.retangulo.x = entradas[ambiente].retangulo.x + entradas[ambiente].largura / 2

def coloca_na_frente_da_entrada(jogador, entradas, ambiente):
    if ambiente == 'manguezal':
        jogador.retangulo.y = entradas[ambiente].altura + 2
    if ambiente == 'deserto':
        jogador.retangulo.y = entradas[ambiente].altura + 2
    if ambiente == 'savana':
        jogador.retangulo.y = entradas[ambiente].retangulo.y - 5 - jogador.altura
    if ambiente == 'floresta_tropical':
        jogador.retangulo.y = entradas[ambiente].retangulo.y - 5 - jogador.altura
    jogador.retangulo.x = entradas[ambiente].retangulo.x + entradas[ambiente].largura / 2


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)

    TELA.cria_mapa((1/5), 80, 80)
    TELA.cor_mapa = cores['mapa']

    jogador = Jogador(50, 50, 2.3, 4.1, TELA)
    jogador.define_velocidade(0.5)
    
    entradas = {}
    entradas['manguezal'] = Obstaculo_Fase2(0, 0, 10, 10, TELA)
    entradas['deserto'] = Obstaculo_Fase2(90, 0, 10, 10, TELA)
    entradas['savana'] = Obstaculo_Fase2(0, 90, 10, 10, TELA)
    entradas['floresta_tropical'] = Obstaculo_Fase2(90, 90, 10, 10, TELA)

    entrada_em_baixo = {}
    entrada_em_baixo['manguezal'] = False
    entrada_em_baixo['deserto'] = False
    entrada_em_baixo['savana'] = True
    entrada_em_baixo['floresta_tropical'] = True

    tesouro = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
    tesouro.cor = cores['dourado']

    saida = Obstaculo_Fase2(45, 99, 10, 1, TELA)

    pontuacao = 0
    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    ambiente = 'inicio'
    while rodando:
        if ambiente == 'inicio':
            TELA.cor = cores['branco']
            desenha_inicio(TELA, jogador, entradas, pontuacao)
            keys = pygame.key.get_pressed()
            movimentacao(keys, jogador)
            for bioma in entradas:
                if jogador.retangulo.colliderect(entradas[bioma].retangulo):
                    ambiente = bioma
                    coloca_na_frente_da_saida(jogador, entradas, ambiente)

        if ambiente == 'manguezal':
            desenha_manguezal(TELA, jogador, tesouro, saida, pontuacao)
            pontuacao += mecanica_biomas(TELA, jogador, tesouro)
            if jogador.retangulo.colliderect(saida.retangulo):
                coloca_na_frente_da_entrada(jogador, entradas, ambiente)
                ambiente = 'inicio'
        if ambiente == 'deserto':
            desenha_deserto(TELA, jogador, tesouro, saida, pontuacao)
            pontuacao += mecanica_biomas(TELA, jogador, tesouro)
            if jogador.retangulo.colliderect(saida.retangulo):
                coloca_na_frente_da_entrada(jogador, entradas, ambiente)
                ambiente = 'inicio'
        if ambiente == 'savana':
            desenha_savana(TELA, jogador, tesouro, saida, pontuacao)
            pontuacao += mecanica_biomas(TELA, jogador, tesouro)
            if jogador.retangulo.colliderect(saida.retangulo):
                coloca_na_frente_da_entrada(jogador, entradas, ambiente)
                ambiente = 'inicio'
        if ambiente == 'floresta_tropical':
            desenha_floresta_tropical(TELA, jogador, tesouro, saida, pontuacao)
            pontuacao += mecanica_biomas(TELA, jogador, tesouro)
            if jogador.retangulo.colliderect(saida.retangulo):
                coloca_na_frente_da_entrada(jogador, entradas, ambiente)
                ambiente = 'inicio'
            
        rodando = verifica_fim()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
