import pygame
import sys
sys.path.append("../../utils")
from cores import cores
from classes import Jogador
from classes import Tesouro
from classes import Tela

def desenha_jogo(TELA, jogador, tesouro, pontuacao):
    TELA.tela.fill(TELA.cor)
    TELA.mapa.fill(TELA.cor_mapa)

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontos: {pontuacao}', False, cores['branco'])
    TELA.tela.blit(texto, ((TELA.LARGURA - texto.get_size()[0]) // 2, 0))
    
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.jogador)
    pygame.draw.rect(TELA.tela, tesouro.cor, tesouro.tesouro)
    
    pygame.draw.rect(TELA.mapa, jogador.cor, jogador.no_mapa)
    pygame.draw.rect(TELA.mapa, tesouro.cor, tesouro.no_mapa)

    TELA.tela.blit(TELA.mapa, (TELA.mapa_pos_x, TELA.mapa_pos_y))

def desenha_tela_ganhador(TELA):
    TELA.tela.fill(cores['dourado'])
    fonte = pygame.font.Font(None, 150)
    texto = fonte.render('Parabéns', False, cores['branco'])
    largura_texto, altura_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - largura_texto) // 2, (TELA.ALTURA - altura_texto) // 2))


def movimentacao(keys, jogador, TELA, tesouro):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()

    if jogador.jogador.colliderect(tesouro.tesouro):
        tesouro.muda_posicao()
        return 1 

    return 0


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['mar']
    pygame.display.set_caption("Caça ao Tesouro (FASE 1)")

    TELA.cria_mapa((1/5))
    TELA.cor_mapa = cores['mapa']
    TELA.mapa_pos_x = TELA.LARGURA - TELA.largura_mapa
    TELA.mapa_pos_y = TELA.ALTURA - TELA.altura_mapa

    jogador = Jogador(50, 50, 2.3, 4.1, TELA)
    jogador.cor = cores['marrom']
    jogador.velocidade = (0.5 / 100) * TELA.LARGURA
    jogador.criar_jogador_no_mapa(jogador.jogador.x * TELA.escala_mapa, jogador.jogador.y * TELA.escala_mapa)

    tesouro = Tesouro(0.5, 0.9, 2.3, 4.1, TELA)
    tesouro.cor = cores['dourado']
    tesouro.criar_tesouro_no_mapa(tesouro.tesouro.y * TELA.escala_mapa, tesouro.tesouro.y * TELA.escala_mapa)

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    PONTUACAO_MAXIMA = 10
    rodando = True
    ganhou = False
    while rodando:
        desenha_jogo(TELA, jogador, tesouro, pontuacao)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        keys = pygame.key.get_pressed()
        pontuacao += movimentacao(keys, jogador, TELA, tesouro)
        if pontuacao >= PONTUACAO_MAXIMA:
            ganhou = True
            rodando = False
        pygame.display.flip()
        clock.tick(FPS)

    while ganhou:
        desenha_tela_ganhador(TELA)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ganhou = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ganhou = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
