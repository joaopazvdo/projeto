import pygame
import sys
sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tesouro
from classes import Tela
from funcoes_principais import cima_baixo_esquerda_direita
from funcoes_principais import cima_baixo_esquerda_direita_no_mapa
from funcoes_principais import fim

def desenha_jogo(TELA, jogador, tesouro, pontuacao):
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    TELA.tela.blit(texto, ((TELA.LARGURA - texto.get_size()[0]) // 2, 0))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))

def desenha_tela_ganhador(TELA):
    TELA.tela.fill(cores['dourado'])
    fonte = pygame.font.Font(None, 150)
    texto = fonte.render('Parabéns', False, cores['branco'])
    largura_texto, altura_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - largura_texto) // 2, (TELA.ALTURA - altura_texto) // 2))


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['mar']
    pygame.display.set_caption("Caça ao Tesouro (FASE 1)")

    TELA.cria_mapa((1/5), 80, 80)
    TELA.cor_mapa = cores['mapa']
    retangulo_mapa = pygame.Rect(80, 80, 20, 20)

    jogador = Jogador(50, 50, 2.3, 4.1, TELA)
    jogador.cor = cores['marrom']
    jogador.define_velocidade(0.5)
    jogador.cria_no_mapa()

    tesouro = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
    tesouro.cor = cores['dourado']
    tesouro.cria_no_mapa()

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    PONTUACAO_MAXIMA = 10
    rodando = True
    ganhou = False
    while rodando:
        desenha_jogo(TELA, jogador, tesouro, pontuacao)
        if fim(): break
        keys = pygame.key.get_pressed()
        cima_baixo_esquerda_direita(keys, jogador)
        cima_baixo_esquerda_direita_no_mapa(keys, jogador)
        if jogador.retangulo.colliderect(tesouro.retangulo):
            tesouro.muda_posicao([retangulo_mapa])
            tesouro.atualiza_pos_no_mapa()
            pontuacao += 1
        if pontuacao >= PONTUACAO_MAXIMA:
            ganhou = True
            rodando = False
        pygame.display.flip()
        clock.tick(FPS)

    while ganhou:
        desenha_tela_ganhador(TELA)
        if fim(): break
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
