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


def desenha_jogo(TELA, jogador, entrada_manguezal, entrada_deserto, entrada_savana, entrada_floresta_tropical):
    TELA.tela.fill(TELA.cor)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.retangulo) 
    pygame.draw.rect(TELA.tela, entrada_manguezal.cor, entrada_manguezal.retangulo) 
    pygame.draw.rect(TELA.tela, entrada_deserto.cor, entrada_deserto.retangulo) 
    pygame.draw.rect(TELA.tela, entrada_savana.cor, entrada_savana.retangulo) 
    pygame.draw.rect(TELA.tela, entrada_floresta_tropical.cor, entrada_floresta_tropical.retangulo) 
    
def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)

    jogador = Jogador(50, 50, 2.3, 4.1, TELA)
    
    entrada_manguezal = Obstaculo_Fase2(0, 0, 10, 10, TELA)
    entrada_deserto = Obstaculo_Fase2(90, 0, 10, 10, TELA)
    entrada_savana = Obstaculo_Fase2(0, 90, 10, 10, TELA)
    entrada_floresta_tropical = Obstaculo_Fase2(90, 90, 10, 10, TELA)

    clock = pygame.time.Clock()
    FPS = 60

    rodando = True
    while rodando:
        desenha_jogo(TELA, jogador, entrada_manguezal, entrada_deserto, entrada_savana, entrada_floresta_tropical)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
        keys = pygame.key.get_pressed()
        movimentacao(keys, jogador)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()




if __name__ == '__main__':
    main()
