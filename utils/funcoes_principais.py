import pygame
def fim():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return True

    return False


def pulo_e_queda(keys, jogador):
    if keys[pygame.K_SPACE]:
        jogador.pular()

    jogador.queda_constante()


def cima_baixo_esquerda_direita(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()


def cima_baixo_esquerda_direita_no_mapa(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima_no_mapa()
    
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo_no_mapa()
    
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda_no_mapa()
    
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita_no_mapa()


