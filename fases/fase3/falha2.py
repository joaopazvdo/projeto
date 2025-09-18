import pygame
import sys

sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tela
from classes import Tesouro
from classes import Obstaculo_Fase2
from biomas import entrar_no_bioma

def verifica_fim():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False

    return True


def movimentacao(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()


def desenha_inicio(TELA, jogador, entradas, pontuacao):
    TELA.tela.fill(TELA.cor)
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    for bioma in entradas:
        pygame.draw.rect(TELA.tela, entradas[bioma].cor, entradas[bioma].retangulo)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    

def entrar_no_inicio(TELA, jogador, entradas, pontuacao):
    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    while rodando:
        desenha_inicio(TELA, jogador, entradas, pontuacao)
        rodando = verifica_fim()
        keys = pygame.key.get_pressed()
        movimentacao(keys, jogador)
        for bioma in entradas:
            if jogador.retangulo.colliderect(entradas[bioma].retangulo):
                return bioma
        pygame.display.flip()
        clock.tick(FPS)


def tira_jogador_de_dentro(jogador, entradas, bioma):
    while True:
        encostou_na_esqueda = jogador.retangulo.x + jogador.largura == entradas[bioma].retangulo.x
        encostou_na_direita = jogador.retangulo.x == entradas[bioma].retangulo.x + entradas[bioma].largura
        print(encostou_na_esqueda)
        print(encostou_na_direita)
        if not encostou_na_direita and not encostou_na_esqueda: break
        if encostou_na_direita and not encostou_na_esqueda:
            jogador.move_para_esquerda()
            jogador.move_para_esquerda()

        if encostou_na_esqueda and not encostou_na_direita: 
            jogador.move_para_direita()
            jogador.move_para_direita()

    while True:
        encostou_em_cima = jogador.retangulo.y == jogador.altura >= entradas[bioma].retangulo.y
        encostou_em_baixo = jogador.retangulo.y == entradas[bioma].retangulo.y + entradas[bioma].altura
        if not encostou_em_baixo and not encostou_em_cima: break
        if encostou_em_cima and not encostou_em_baixo:
            jogador.move_para_baixo()
            jogador.move_para_baixo()

        if encostou_em_baixo and not encostou_em_cima:
            jogador.move_para_cima()
            jogador.move_para_cima()

        print(jogador.retangulo.x)
        print(jogador.retangulo.y)


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

    pontuacao = 0
    rodando = True
    while rodando:
        bioma = entrar_no_inicio(TELA, jogador, entradas, pontuacao)
        tira_jogador_de_dentro(jogador, entradas, bioma)
        if bioma == 'manguezal':
            em_baixo = True
        if bioma == 'deserto':
            em_baixo = True
        if bioma == 'savana':
            em_baixo = False
        if bioma == 'floresta_tropical':
            em_baixo = False
        if bioma:
            entrar_no_bioma(pontuacao, cores[bioma], em_baixo)


    pygame.quit()


if __name__ == '__main__':
    main()
