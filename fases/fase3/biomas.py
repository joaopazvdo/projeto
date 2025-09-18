import pygame
import sys

sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tela
from classes import Tesouro
from classes import Obstaculo_Fase2

def movimentacao(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()

def movimentacao_no_mapa(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima_no_mapa()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo_no_mapa()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda_no_mapa()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita_no_mapa()


def verifica_fim():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False

    return True


def mecanica_biomas(TELA, jogador, tesouro ):
    keys = pygame.key.get_pressed()
    movimentacao(keys, jogador)
    movimentacao_no_mapa(keys, jogador)
    if jogador.retangulo.colliderect(tesouro.retangulo):
        tesouro.muda_posicao()
        return 1
    else:
        return 0


def desenha_biomas(TELA, jogador, tesouro, pontuacao, saida, em_baixo):
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()

    if em_baixo:
        TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, 0))
    else:
        TELA.tela.blit(texto, ((TELA.LARGURA - tamanho_texto[0]) // 2, TELA.ALTURA - tamanho_texto[1]))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.retangulo)
    pygame.draw.rect(TELA.tela, saida.cor, saida.retangulo)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)
    pygame.draw.rect(TELA.mapa, saida.cor, saida.retangulo)


    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))


def entrar_no_bioma(pontuacao, cor_tela, em_baixo):
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cor_tela

    TELA.cria_mapa((1/5), 80, 80)
    TELA.cor_mapa = cores['mapa']

    if em_baixo:
        jogador = Jogador(48.85, 94, 2.3, 4.1, TELA)
        saida = Obstaculo_Fase2(45, 99.5, 10, 0.5, TELA)

    else:
        jogador = Jogador(48.85, 1.4, 2.3, 4.1, TELA)
        saida = Obstaculo_Fase2(45, 0, 10, 0.5, TELA)
        
    jogador.define_velocidade(0.5)
    jogador.cria_no_mapa()

    tesouro = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
    tesouro.cor = cores['dourado']
    tesouro.cria_no_mapa()

    saida.cria_no_mapa()

    clock = pygame.time.Clock()
    FPS = 60

    rodando = True
    while rodando:
        desenha_biomas(TELA, jogador, tesouro, pontuacao, saida, em_baixo)
        rodando = verifica_fim()
        pontuacao += mecanica_biomas(TELA, jogador, tesouro)
        if jogador.retangulo.colliderect(saida.retangulo):
            rodando = False
        pygame.display.flip()
        clock.tick(FPS)

    return pontuacao

    
if __name__ == '__main__':
    pygame.init()
    entrar_no_bioma(0, cores['manguezal'], False)
    pygame.quit()
