from random import randint
from cores import cores
import pygame


class Jogador:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100) * self.tela.ALTURA
        self.jogador = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.cor = cores['preto']
        self.velocidade = 0

    def criar_jogador_no_mapa(self, x, y):
        self.no_mapa = pygame.Rect(x, y, self.largura * self.tela.escala_mapa, self.altura * self.tela.escala_mapa)

    def move_para_cima(self):
        esta_no_topo = self.jogador.y <= 0
        if not esta_no_topo:
            self.jogador.y -= self.velocidade
            self.no_mapa.y -= self.velocidade * self.tela.escala_mapa


    def move_para_baixo(self):
        esta_em_baixo = self.jogador.y >= (self.tela.ALTURA - self.altura)
        if not esta_em_baixo:
            self.jogador.y += self.velocidade
            self.no_mapa.y += self.velocidade * self.tela.escala_mapa


    def move_para_esquerda(self):
        esta_no_comeco = self.jogador.x <= 0
        if not esta_no_comeco:
            self.jogador.x -= self.velocidade
            self.no_mapa.x -= self.velocidade * self.tela.escala_mapa


    def move_para_direita(self):
        esta_no_final = self.jogador.x >= (self.tela.LARGURA - self.largura) 
        if not esta_no_final:
            self.jogador.x += self.velocidade
            self.no_mapa.x += self.velocidade * self.tela.escala_mapa


    def queda_constante(self):
        gravidade = (self.tela.ALTURA / 600) * 0.25
        self.velocidade += gravidade
        self.jogador.y += self.velocidade


    def pular(self):
        self.velocidade = (self.tela.ALTURA / 600) * -5


class Tesouro:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100)  * self.tela.ALTURA
        self.tesouro = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.cor = cores['preto']


    def muda_posicao(self):
        while True:
            novo_x = randint(0, self.tela.LARGURA - int(self.largura))
            novo_y = randint(0, self.tela.ALTURA - int(self.altura))
            esta_atras_do_mapa = novo_x > self.tela.mapa_pos_x and novo_y > self.tela.mapa_pos_y
            if not esta_atras_do_mapa: break
        self.tesouro.x, self.tesouro.y = novo_x, novo_y
        self.no_mapa.x, self.no_mapa.y = novo_x * self.tela.escala_mapa, novo_y * self.tela.escala_mapa

    def criar_tesouro_no_mapa(self, x, y):
        self.no_mapa = pygame.Rect(x, y, self.largura * self.tela.escala_mapa, self.altura * self.tela.escala_mapa)


class Tela:
    def __init__(self, LARGURA, ALTURA):
        self.ALTURA = ALTURA
        self.LARGURA = LARGURA
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA), pygame.FULLSCREEN)
        self.TAMANHO = (self.LARGURA, self.ALTURA)
        self.cor = cores['branco']

    def cria_mapa(self, escala):
        self.escala_mapa = escala
        self.largura_mapa = self.LARGURA * self.escala_mapa
        self.altura_mapa = self.ALTURA * self.escala_mapa
        self.mapa = pygame.Surface((self.largura_mapa, self.altura_mapa))


class Obstaculo_Fase2:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100) * self.tela.ALTURA
        self.obstaculo = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.velocidade = (0.8 / 100) * self.tela.LARGURA
        self.cor = cores['marrom']


    def move_constante_para_esquerda(self):
        self.obstaculo.x -= self.velocidade


