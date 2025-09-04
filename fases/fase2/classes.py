import pygame
from random import randint


class Jogador:
    def __init__(self, x, y, largura, altura, velocidade, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.jogador = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.velocidade = velocidade

    def criar_jogador_no_mapa(self, x, y, mapa):
        self.no_mapa = pygame.Rect(x, y, self.largura * mapa.escala, self.altura * mapa.escala)


    def movimento_fase1(self, keys, TELA, tesouro, mapa):
        ponto = 0
        esta_no_fundo = self.jogador.y >= (TELA.ALTURA - self.altura)
        esta_no_topo = self.jogador.y <= 0
        esta_no_final = self.jogador.x >= (TELA.LARGURA - self.largura) 
        esta_no_comeco = self.jogador.x <= 0
        #BAIXO
        if keys[pygame.K_DOWN] and not esta_no_fundo:
            self.y += self.velocidade
            self.jogador.y += self.velocidade
            self.no_mapa.y += self.velocidade * mapa.escala


        #CIMA
        if keys[pygame.K_UP] and not esta_no_topo:
            self.y -= self.velocidade
            self.jogador.y -= self.velocidade
            self.no_mapa.y -= self.velocidade * mapa.escala

        #DIREITA
        if keys[pygame.K_RIGHT] and not esta_no_final:
            self.x += self.velocidade
            self.jogador.x += self.velocidade
            self.no_mapa.x += self.velocidade * mapa.escala

        #ESQUERDA
        if keys[pygame.K_LEFT] and not esta_no_comeco: 
            self.x -= self.velocidade
            self.jogador.x -= self.velocidade
            self.no_mapa.x -= self.velocidade * mapa.escala

        if self.jogador.colliderect(tesouro.tesouro):
            tesouro.muda_posicao(TELA, mapa)
            ponto += 1

        return ponto 

    
    def movimento_fase2(self, keys):
        self.gravidade = 0.25 * self.velocidade
        esta_no_topo = self.jogador.y <= 0
        if keys[pygame.K_SPACE] and not esta_no_topo:
            self.jogador.y -= self.velocidade * 5
            print(self.velocidade)

        else:

            self.jogador.y += self.velocidade * 0.25


class Tesouro:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.tesouro = pygame.Rect(self.x, self.y, self.largura, self.altura)


    def muda_posicao(self, TELA, mapa):
        while True:
            self.x = randint(0, TELA.LARGURA - self.largura)
            self.y = randint(0, TELA.ALTURA - self.altura)
            esta_atras_do_mapa = self.x > mapa.posicao_x and self.y > mapa.posicao_y
            if not esta_atras_do_mapa: break
        self.tesouro.x, self.tesouro.y = self.x, self.y
        self.no_mapa.x, self.no_mapa.y = self.x * mapa.escala, self.y * mapa.escala

    def criar_tesouro_no_mapa(self, x, y, mapa):
        self.no_mapa = pygame.Rect(x, y, self.largura * mapa.escala, self.altura * mapa.escala)


class Tela:
    def __init__(self, LARGURA, ALTURA, cor):
        self.ALTURA = ALTURA
        self.LARGURA = LARGURA
        self.cor = cor
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA), pygame.FULLSCREEN)
        self.TAMANHO = (self.LARGURA, self.ALTURA)


class Mapa(Tela):
    def __init__(self, largura_tela, altura_tela, escala, cor):
        self.escala = escala
        self.largura = largura_tela
        self.largura = self.largura * self.escala
        self.altura = altura_tela  
        self.altura = self.altura * self.escala 
        self.tamanho = (self.largura, self.altura)
        self.posicao_x = largura_tela - self.largura
        self.posicao_y = altura_tela - self.altura
        self.cor = cor
        self.mapa = pygame.Surface((self.largura, self.altura)) 


cores = {
'mapa':(245,222,179),
'mar':(0,105,148),
'marrom':(139,69,19),
'dourado':(255,245,0),
'branco':(255,255,255),
'céu':(135,206,235),
    }
