import pygame
import sys
sys.path.append("../../utils")
from cores import cores
from classes import Tela
from classes import Jogador
from classes import Obstaculo_Fase2

def desenha_jogo(TELA, jogador, obstaculos, perdeu, ganhou):
    if not perdeu and not ganhou:
        TELA.tela.fill(TELA.cor)
        pygame.draw.rect(TELA.tela, jogador.cor, jogador.jogador)
        for montanha in obstaculos:
            pygame.draw.rect(TELA.tela, montanha.cor, montanha.obstaculo)

    if perdeu:
        TELA.tela.fill(cores['preto'])
        fonte = pygame.font.Font(None, 150)
        texto = fonte.render('Perdeu', False, cores['branco'])
        largura_texto, altura_texto = texto.get_size()
        TELA.tela.blit(texto, ((TELA.LARGURA - largura_texto) // 2, ((TELA.ALTURA - altura_texto) // 2)))


def movimentacao(keys, jogador):
    if keys[pygame.K_SPACE]:
        jogador.pular()

    jogador.queda_constante()


def cria_lista_obstaculos(num_obstaculos, distancia_entre_obstaculos, TELA):
    obstaculos = num_obstaculos * [None]
    x_obstaculo = 100
    for i in range(num_obstaculos):
       montanha = Obstaculo_Fase2(x_obstaculo, 35, 20.3, 65, TELA)
       obstaculos[i] = montanha
       x_obstaculo += distancia_entre_obstaculos

    return obstaculos


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['ceu']

    jogador = Jogador(7.8, 30, 2.3, 4.1, TELA)
    obstaculos = cria_lista_obstaculos(20, 75 + 20.3, TELA)

    clock = pygame.time.Clock()
    FPS = 60

    ganhou = False
    perdeu = False
    rodando = True
    while rodando:
        desenha_jogo(TELA, jogador, obstaculos, perdeu, ganhou)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        for montanha in obstaculos:
            montanha.move_constante_para_esquerda()
            if montanha.obstaculo.colliderect(jogador.jogador):
                perdeu = True
        if jogador.jogador.y <= 0:
            perdeu = True

        if jogador.jogador.y >= TELA.ALTURA - jogador.altura:
            perdeu = True
        keys = pygame.key.get_pressed()
        movimentacao(keys, jogador)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    

if __name__ == '__main__':
    main()
