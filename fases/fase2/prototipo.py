import pygame
from pygame.display import flip
from classes import cores
from classes import Tela
from classes import Jogador


class Obstaculo:
    def __init__(self, x, y, largura, altura, velocidade, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.cor = cor
        self.obstaculo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def movimentacao(self):
        self.obstaculo.x -= self.velocidade 


class Jogador_Fase2(Jogador):
    def __init__(self, x, y, largura, altura, cor, pulo, gravidade):
        super().__init__(x, y, largura, altura, 0, cor)
        self.gravidade = gravidade
        self.pulo = pulo
        self.jogador = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def movimento_fase2(self, keys):
        esta_no_topo = self.jogador.y <= 0
        if keys[pygame.K_SPACE] and not esta_no_topo:
            self.velocidade = self.pulo

        self.velocidade += self.gravidade
        if not esta_no_topo:
            self.y += self.velocidade
            self.jogador.y += self.velocidade


def desenha_jogo(TELA, jogador, montanha):
    TELA.tela.fill(TELA.cor)
    pygame.draw.rect(TELA.tela, jogador.cor, jogador.jogador)
    pygame.draw.rect(TELA.tela, montanha.cor, montanha.obstaculo)


def main():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h, cores['céu'])

    jogador = Jogador_Fase2(45, (TELA.ALTURA - 45) // 2, 45, 45, cores['marrom'], (TELA.ALTURA / 600) * -5, (TELA.ALTURA // 600) * 0.25)
    montanha = Obstaculo(TELA.LARGURA, TELA.ALTURA - TELA.ALTURA * (3/4), 400, TELA.ALTURA * (3/4), 20, cores['marrom'])
    
    clock = pygame.time.Clock()
    FPS = 60

    rodando = True
    while rodando:
        desenha_jogo(TELA, jogador, montanha)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        keys = pygame.key.get_pressed()
        jogador.movimento_fase2(keys)
        montanha.movimentacao()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

    

main()
