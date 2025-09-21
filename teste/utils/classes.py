from random import randint
from .arquivo_cores import cores
import pygame

class Jogador:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100) * self.tela.ALTURA
        self.retangulo = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.cor = cores['preto']
        self.velocidade = 0
        self.gravidade = 0


    def define_posicao(self, x, y):
        self.retangulo.x = (x / 100) * self.tela.LARGURA
        self.retangulo.y = (y / 100) * self.tela.ALTURA


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.tela.LARGURA


    def cria_no_mapa(self):
        x_mapa = self.retangulo.x * self.tela.escala_mapa
        y_mapa = self.retangulo.y * self.tela.escala_mapa
        largura_no_mapa = self.largura * self.tela.escala_mapa
        altura_no_mapa = self.altura * self.tela.escala_mapa
        self.no_mapa = pygame.Rect(x_mapa, y_mapa, largura_no_mapa, altura_no_mapa)


    def move_para_cima(self):
        esta_no_topo = self.retangulo.y <= 0
        if not esta_no_topo:
            self.retangulo.y -= self.velocidade


    def move_para_baixo(self):
        esta_em_baixo = self.retangulo.y >= (self.tela.ALTURA - self.altura)
        if not esta_em_baixo:
            self.retangulo.y += self.velocidade


    def move_para_esquerda(self):
        esta_no_comeco = self.retangulo.x <= 0
        if not esta_no_comeco:
            self.retangulo.x -= self.velocidade


    def move_para_direita(self):
        esta_no_final = self.retangulo.x >= (self.tela.LARGURA - self.largura) 
        if not esta_no_final:
            self.retangulo.x += self.velocidade


    def move_para_cima_no_mapa(self):
        esta_no_topo = self.retangulo.y <= 0
        if not esta_no_topo:
            self.no_mapa.y -= self.velocidade * self.tela.escala_mapa


    def move_para_baixo_no_mapa(self):
        esta_em_baixo = self.retangulo.y >= (self.tela.ALTURA - self.altura)
        if not esta_em_baixo:
            self.no_mapa.y += self.velocidade * self.tela.escala_mapa


    def move_para_esquerda_no_mapa(self):
        esta_no_comeco = self.retangulo.x <= 0
        if not esta_no_comeco:
            self.no_mapa.x -= self.velocidade * self.tela.escala_mapa


    def move_para_direita_no_mapa(self):
        esta_no_final = self.retangulo.x >= (self.tela.LARGURA - self.largura) 
        if not esta_no_final:
            self.no_mapa.x += self.velocidade * self.tela.escala_mapa


    def queda_constante(self):
        self.velocidade += self.gravidade
        self.retangulo.y += self.velocidade


    def pular(self):
        self.velocidade = (self.tela.ALTURA / 600) * -5


class Tesouro:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100)  * self.tela.ALTURA
        self.retangulo = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.cor = cores['preto']
        self.velocidade = 0
        self.aparece = True


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.tela.LARGURA


    def muda_posicao(self, lista_elem_evitar):
        while True:
            colidiu = False
            novo_x = randint(0, self.tela.LARGURA - int(self.largura))
            novo_y = randint(0, self.tela.ALTURA - int(self.altura))
            self.retangulo.x, self.retangulo.y = novo_x, novo_y
            for e in lista_elem_evitar:
                if id(self.retangulo) != id(e.retangulo) and self.retangulo.colliderect(e.retangulo): 
                    colidiu = True
            if not colidiu: break


    def muda_posicao2(self, lista_elem_evitar):
        colidiu = False
        while True:
            colidiu = False
            novo_x = randint(0, self.tela.LARGURA - int(self.largura))
            novo_y = - self.tela.ALTURA * 50/100
            self.retangulo.x, self.retangulo.y = novo_x, novo_y
            for e in lista_elem_evitar:
                if id(self.retangulo) != id(e.retangulo) and self.retangulo.colliderect(e.retangulo): 
                    colidiu = True
            if not colidiu: break


    def atualiza_pos_no_mapa(self):
        self.no_mapa.x = self.retangulo.x * self.tela.escala_mapa
        self.no_mapa.y = self.retangulo.y * self.tela.escala_mapa


    def cria_no_mapa(self):
        x_mapa = self.retangulo.x * self.tela.escala_mapa
        y_mapa = self.retangulo.y * self.tela.escala_mapa
        largura_no_mapa = self.largura * self.tela.escala_mapa
        altura_no_mapa = self.altura * self.tela.escala_mapa
        self.no_mapa = pygame.Rect(x_mapa, y_mapa, largura_no_mapa, altura_no_mapa)

    def move_constante_para_baixo(self):
        self.retangulo.y += self.velocidade


class Tela:
    def __init__(self, LARGURA, ALTURA):
        self.ALTURA = ALTURA
        self.LARGURA = LARGURA
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA), pygame.FULLSCREEN)
        self.TAMANHO = (self.LARGURA, self.ALTURA)
        self.cor = cores['branco']


    def cria_mapa(self, escala, x, y):
        self.escala_mapa = escala
        self.largura_mapa = self.LARGURA * self.escala_mapa
        self.altura_mapa = self.ALTURA * self.escala_mapa
        self.mapa_pos_x = (x / 100) * self.LARGURA
        self.mapa_pos_y = (y / 100) * self.ALTURA
        self.mapa = pygame.Surface((self.largura_mapa, self.altura_mapa))


class Retangulo:
    def __init__(self, x, y, largura, altura, tela):
        self.tela = tela
        self.largura = (largura / 100) * self.tela.LARGURA
        self.altura = (altura / 100) * self.tela.ALTURA
        self.retangulo = pygame.Rect((x / 100) * self.tela.LARGURA, (y / 100) * self.tela.ALTURA, self.largura, self.altura)
        self.velocidade = (0.8 / 100) * self.tela.LARGURA
        self.cor = cores['marrom']
        self.aparece = True


    def move_constante_para_esquerda(self):
        self.retangulo.x -= self.velocidade


    def cria_no_mapa(self):
        x_mapa = self.retangulo.x * self.tela.escala_mapa
        y_mapa = self.retangulo.y * self.tela.escala_mapa
        largura_no_mapa = self.largura * self.tela.escala_mapa
        altura_no_mapa = self.altura * self.tela.escala_mapa
        self.no_mapa = pygame.Rect(x_mapa, y_mapa, largura_no_mapa, altura_no_mapa)


    def move_constante_para_baixo(self):
        self.retangulo.y += self.velocidade


    def muda_posicao(self, lista_elem_evitar):
        colidiu = False
        while True:
            colidiu = False
            novo_x = randint(0, self.tela.LARGURA - int(self.largura))
            novo_y = randint(-self.tela.ALTURA, 0) 
            suposto_retangulo = pygame.Rect(novo_x, novo_y, self.largura, self.altura)
            for e in lista_elem_evitar:
#                if id(self.retangulo) != id(e.retangulo) and self.retangulo.colliderect(e.retangulo): 
                if suposto_retangulo.colliderect(e.retangulo):
                    colidiu = True
            if not colidiu: break
        self.retangulo.x, self.retangulo.y = novo_x, novo_y


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.tela.LARGURA
