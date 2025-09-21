import pygame
#from utils import funcoes_principais
#from utils import classes
#from utils import cores
from utils.arquivo_cores import cores
from utils.classes import Jogador
from utils.classes import Tesouro
from utils.classes import Tela
from utils.classes import Retangulo
from utils.funcoes_principais import cima_baixo_esquerda_direita
from utils.funcoes_principais import cima_baixo_esquerda_direita_no_mapa
from utils.funcoes_principais import fim
#from utils.funcoes_principais import roda_ganhou
from tela_ganhou import tela_ganhou

def desenha_jogo(TELA, jogador, tesouro, pontuacao):
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    TELA.tela.blit(texto, ((TELA.LARGURA - texto.get_size()[0]) // 2, 0))


def fase1():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['mar']
    pygame.display.set_caption("Caça ao Tesouro (FASE 1)")

    TELA.cria_mapa((1/5), 80, 80)
    TELA.cor_mapa = cores['mapa']
    retangulo_mapa = Retangulo(80,80,20,20,TELA)

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
        if fim(): 
            return 'Tela inicial', False
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

    pygame.quit()
    if ganhou:
        return tela_ganhou(), ganhou



if __name__ == '__main__':
    fase1()
