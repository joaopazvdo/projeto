from random import randint
from .arquivo_cores import cores
import pygame

class Jogador:
    def __init__(self, x, y, largura, altura, TELA):
        self.TELA = TELA
        self.largura = (largura / 100) * self.TELA.LARGURA
        self.altura = (altura / 100) * self.TELA.ALTURA
        x = (x / 100) * self.TELA.LARGURA
        y = (y / 100) * self.TELA.ALTURA
        self.retangulo = pygame.Rect(x, y, self.largura, self.altura)
        self.cor = cores['preto']
        self.velocidade = 0
        self.gravidade = 0
        self.tipo = 'Jogador'
        self.muda_textura = False


    def define_posicao(self, x, y):
        self.retangulo.x = (x / 100) * self.TELA.LARGURA
        self.retangulo.y = (y / 100) * self.TELA.ALTURA


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.TELA.LARGURA


    def cria_no_mapa(self):
        x_mapa = self.retangulo.x * self.TELA.escala_mapa
        y_mapa = self.retangulo.y * self.TELA.escala_mapa
        largura_no_mapa = self.largura * self.TELA.escala_mapa
        altura_no_mapa = self.altura * self.TELA.escala_mapa
        self.no_mapa = pygame.Rect(x_mapa, y_mapa, 
                                   largura_no_mapa, altura_no_mapa)


    def move_para_cima(self):
        self.retangulo.y -= self.velocidade
        if self.muda_textura:
            self.textura = self.textura_cima


    def move_para_baixo(self):
        self.retangulo.y += self.velocidade
        if self.muda_textura:
            self.textura = self.textura_baixo


    def move_para_esquerda(self):
        self.retangulo.x -= self.velocidade
        if self.muda_textura:
            self.textura = self.textura_esquerda


    def move_para_direita(self):
        self.retangulo.x += self.velocidade
        if self.muda_textura:
            self.textura = self.textura_direita


    def queda_constante(self):
        self.velocidade += self.gravidade
        self.retangulo.y += self.velocidade


    def pular(self):
        self.velocidade = (self.TELA.ALTURA / 600) * -5


    def define_textura_esquerda(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura_esquerda = pygame.transform.scale(imagem, 
                                                      (self.largura, self.altura))
        self.muda_textura = True


    def define_textura_direita(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura_direita = pygame.transform.scale(imagem, 
                                                     (self.largura, self.altura))
        self.muda_textura = True


    def define_textura_cima(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura_cima = pygame.transform.scale(imagem, 
                                                  (self.largura, self.altura))
        self.muda_textura = True


    def define_textura_baixo(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura_baixo = pygame.transform.scale(imagem, 
                                                   (self.largura, self.altura))
        self.muda_textura = True


    def define_textura(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura = pygame.transform.scale(imagem, 
                                             (self.largura, self.altura))


    def texturiza(self):
        self.TELA.tela.blit(self.textura, (self.retangulo.x, self.retangulo.y))


    def texturiza_visual(self):
        self.TELA.tela.blit(self.textura, (self.visual.x, self.visual.y))


    def visual_relativo(self, chave):
        self.visual = self.retangulo.move(-self.TELA.cameras[chave].x, 
                                          -self.TELA.cameras[chave].y)


class Tesouro:
    def __init__(self, x, y, largura, altura, TELA):
        self.TELA = TELA
        self.largura = (largura / 100) * self.TELA.LARGURA
        self.altura = (altura / 100)  * self.TELA.ALTURA
        x = (x / 100) * self.TELA.LARGURA
        y = (y / 100) * self.TELA.ALTURA
        self.retangulo = pygame.Rect(x, y, self.largura, self.altura)
        self.cor = cores['preto']
        self.velocidade = 0
        self.aparece = True
        self.tipo = 'Tesouro'


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.TELA.LARGURA


    def visual_relativo(self, chave):
        self.visual = self.retangulo.move(-self.TELA.cameras[chave].x, 
                                          -self.TELA.cameras[chave].y)


    def move_constante_para_baixo(self):
        self.retangulo.y += self.velocidade


    def define_textura(self, imagem):
        self.textura = pygame.transform.scale(imagem, (self.largura, self.altura))


    def texturiza(self):
        self.TELA.tela.blit(self.textura, (self.retangulo.x, self.retangulo.y))
    

    def texturiza_visual(self):
        self.TELA.tela.blit(self.textura, (self.visual.x, self.visual.y))


    def define_textura(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura = pygame.transform.scale(imagem, 
                                                       (self.largura, self.altura))


class Tela:
    def __init__(self, LARGURA, ALTURA):
        self.ALTURA = ALTURA
        self.LARGURA = LARGURA
        self.TAMANHO = (self.LARGURA, self.ALTURA)
        self.tela = pygame.display.set_mode(self.TAMANHO, pygame.FULLSCREEN)
        self.cor = cores['branco']
        self.tipo = 'Tela'
        self.largura_mundos = {}
        self.altura_mundos = {}
        self.mundos = {}
        self.escala_mapas = {}
        self.mapas = {}
        self.largura_mapas = {}
        self.altura_mapas = {}
        self.mapas_pos_x = {}
        self.mapas_pos_y = {}
        self.cameras = {}
        self.texturas = {}


    def cria_mundo(self, chave, largura_mundo, altura_mundo):
        self.largura_mundos[chave] = largura_mundo / 100 * self.LARGURA
        self.altura_mundos[chave] = altura_mundo/100 * self.ALTURA
        self.mundos[chave] = pygame.Rect(0,0,self.largura_mundos[chave], 
                                         self.altura_mundos[chave])


    def cria_camera(self, chave):
        self.cameras[chave] = pygame.Rect(0,0,self.LARGURA, self.ALTURA)


    def cria_mapa(self,chave, escala, x, y):
        self.escala_mapas[chave] = escala
        self.largura_mapas[chave] = self.largura_mundos[chave] * self.escala_mapas[chave]
        self.altura_mapas[chave] = self.altura_mundos[chave] * self.escala_mapas[chave]
        self.mapas_pos_x[chave] = (x / 100) * self.LARGURA
        self.mapas_pos_y[chave] = (y / 100) * self.ALTURA
        self.mapas[chave] = pygame.Surface((self.largura_mapas[chave], 
                                            self.altura_mapas[chave]))

    def desenha_no_mapa(self, chave, retangulos):
        self.mapas[chave].fill(self.cor)
        for r in retangulos:
            r_mapa = pygame.Rect((r.retangulo.x * self.escala_mapas[chave]),
                                 (r.retangulo.y * self.escala_mapas[chave]),
                                 (r.largura * self.escala_mapas[chave]),
                                 (r.altura * self.escala_mapas[chave]))
            if r.tipo == 'Tesouro':
                pygame.draw.rect(self.mapas[chave], cores['vermelho'], r_mapa)
            else:
                pygame.draw.rect(self.mapas[chave], r.cor, r_mapa)
        pygame.draw.rect(self.mapas[chave], cores['preto'],
                         self.mapas[chave].get_rect(), 1)


    def define_textura(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert()
        self.textura = pygame.transform.scale(imagem, self.TAMANHO)


    def define_textura_mundo(self,chave, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert()
        self.texturas[chave] = pygame.transform.scale(imagem, 
                                              (self.largura_mundos[chave], 
                                               self.altura_mundos[chave]))


    def texturiza_mundo(self, chave):
        self.tela.blit(self.texturas[chave], 
                       (self.mundos[chave].x, self.mundos[chave].y))


class Retangulo:
    def __init__(self, x, y, largura, altura, TELA):
        self.TELA = TELA
        self.largura = (largura / 100) * self.TELA.LARGURA
        self.altura = (altura / 100) * self.TELA.ALTURA
        x = (x / 100) * self.TELA.LARGURA
        y = (y / 100) * self.TELA.ALTURA
        self.retangulo = pygame.Rect(x, y, self.largura, self.altura)
        self.velocidade = (0.8 / 100) * self.TELA.LARGURA
        self.cor = cores['marrom']
        self.aparece = True
        self.tipo = 'Retangulo'


    def move_constante_para_esquerda(self):
        self.retangulo.x -= self.velocidade


    def move_constante_para_baixo(self):
        self.retangulo.y += self.velocidade


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.TELA.LARGURA


    def visual_relativo(self, chave):
        self.visual = self.retangulo.move(-self.TELA.cameras[chave].x, 
                                          -self.TELA.cameras[chave].y)


    def define_textura(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura = pygame.transform.scale(imagem, (self.largura, self.altura))


    def texturiza_visual(self):
        self.TELA.tela.blit(self.textura, (self.visual.x, self.visual.y))


    def texturiza(self):
        self.TELA.tela.blit(self.textura, (self.retangulo.x, self.retangulo.y))


class Triangulo:
    def __init__(self, x, y, largura, altura, TELA):
        self.TELA = TELA
        self.x = x / 100 * self.TELA.LARGURA
        self.y = y / 100 * self.TELA.ALTURA
        self.largura = (largura / 100) * self.TELA.LARGURA
        self.altura = (altura / 100) * self.TELA.ALTURA
        self.vertice1 = (self.x, self.y + self.altura)
        self.vertice2 = (self.x + self.largura / 2, self.y)
        self.vertice3 = (self.x + self.largura, self.y + self.altura)
        self.triangulo = [self.vertice1, self.vertice2, self.vertice3]

        self.velocidade = (0.8 / 100) * self.TELA.LARGURA
        self.cor = cores['marrom']
        self.aparece = True
        self.tipo = 'Triangulo'


    def define_velocidade(self, porcentagem_velocidade):
        self.velocidade = (porcentagem_velocidade / 100) * self.TELA.largura


    def move_constante_para_esquerda(self):
        self.x -= self.velocidade
        self.vertice1 = (self.x, self.y + self.altura)
        self.vertice2 = (self.x + self.largura / 2, self.y)
        self.vertice3 = (self.x + self.largura, self.y + self.altura)
        self.triangulo = [self.vertice1, self.vertice2, self.vertice3]
       

    def colidiu(self,retangulo):
        area_total = self.area(None, None, None)
        ponto_de_contato = (retangulo.retangulo.x + retangulo.largura, 
                            retangulo.retangulo.y + retangulo.altura)
        area1 = self.area(ponto_de_contato, None, None)
        area2 = self.area(None, ponto_de_contato, None)
        area3 = self.area(None, None,ponto_de_contato)
        return area_total == area1 + area2 + area3


    def area(self, ponto1, ponto2, ponto3):
        ponto1 = self.vertice1 if not ponto1 else ponto1
        ponto2 = self.vertice2 if not ponto2 else ponto2
        ponto3 = self.vertice3 if not ponto3 else ponto3
        x1, y1 = ponto1
        x2, y2 = ponto2
        x3, y3 = ponto3
        area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
        return area


    def define_textura(self, endereco_imagem):
        imagem = pygame.image.load(endereco_imagem).convert_alpha()
        self.textura = pygame.transform.scale(imagem, (self.largura, self.altura))


    def texturiza_visual(self):
        self.TELA.tela.blit(self.textura, (self.visual.x, self.visual.y))


    def texturiza(self):
        self.TELA.tela.blit(self.textura, (self.x, self.y))


class Caixa_de_texto:
    def __init__(self, x, y, largura, altura, TELA):
        self.TELA = TELA
        self.largura = (largura / 100) * self.TELA.LARGURA
        self.altura = (altura / 100) * self.TELA.ALTURA
        x = (x / 100) * self.TELA.LARGURA
        y = (y / 100) * self.TELA.ALTURA
        self.retangulo = pygame.Rect(x, y, self.largura, self.altura)
        self.cor = cores['preto']
        self.aparece = True
        self.aparece_texto = True
        self.linhas_de_texto = [''] 
        self.i_linha = 0
        self.fonte = pygame.font.Font(None, 30)
        self.cor_texto = cores['branco']
        self.cor_texto_auxiliar = cores['branco']
        self.tipo = 'Caixa_de_texto'


    def define_linhas_de_texto(self, linhas):
        self.linhas_de_texto = linhas


    def linha_atual(self):
        return self.linhas_de_texto[self.i_linha]


    def renderiza_texto(self):
        self.texto = self.fonte.render(self.linha_atual(), False, self.cor_texto)


    def tamanho_texto(self, i_largura_ou_altura):
        return self.texto.get_size()[i_largura_ou_altura]


    def define_fonte(self, porcentagem_tamanho):
        novo_tamanho = int(self.TELA.LARGURA * porcentagem_tamanho / 100)
        self.fonte = pygame.font.Font(None, novo_tamanho)


    def define_pos_texto(self, orientacao_x, orientacao_y, 
                         porcentagem_margem_x, porcentagem_margem_y):
        margem_x = self.largura * porcentagem_margem_x / 100 
        margem_y = self.altura * porcentagem_margem_y / 100 
        if orientacao_x == 1:
            pos_x = self.retangulo.x + margem_x
        if orientacao_y == 1:
            pos_y = self.retangulo.y + margem_y

        if orientacao_x == 2:
            pos_x = self.retangulo.x + (self.largura - self.tamanho_texto(0)) / 2 
        if orientacao_y == 2:
            pos_y = self.retangulo.y + (self.altura - self.tamanho_texto(1)) / 2 
            
        if orientacao_x == 3:
            pos_x = self.retangulo.x + self.largura - self.tamanho_texto(0) - margem_x
        if orientacao_y == 3:
            pos_y = self.retangulo.y + self.altura - self.tamanho_texto(1) - margem_y

        self.texto_pos_x = pos_x
        self.texto_pos_y = pos_y
        self.texto_pos = (self.texto_pos_x, self.texto_pos_y)


    def cria_texto_auxiliar(self, texto, porcentagem_tamanho_fonte):
        tamanho_fonte_auxiliar = int(self.TELA.LARGURA * porcentagem_tamanho_fonte/100)
        self.fonte_auxiliar = pygame.font.Font(None, tamanho_fonte_auxiliar)
        self.texto_auxiliar = self.fonte_auxiliar.render(texto, False, 
                                                         self.cor_texto_auxiliar)


    def tamanho_texto_auxilar(self, i_largura_ou_altura):
        return self.texto_auxiliar.get_size()[i_largura_ou_altura]


    def define_pos_texto_auxiliar(self, orientacao_x, orientacao_y, 
                         porcentagem_margem_x, porcentagem_margem_y):
        margem_x = self.largura * porcentagem_margem_x / 100 
        margem_y = self.altura * porcentagem_margem_y / 100 
        if orientacao_x == 1:
            pos_x = self.retangulo.x + margem_x
        if orientacao_y == 1:
            pos_y = self.retangulo.y + margem_y

        if orientacao_x == 2:
            pos_x = self.retangulo.x + (self.largura - self.tamanho_texto_auxilar(0)) / 2 
        if orientacao_y == 2:
            pos_y = self.retangulo.y + (self.altura - self.tamanho_texto_auxilar(1)) / 2 
            
        if orientacao_x == 3:
            pos_x = self.retangulo.x +self.largura - self.tamanho_texto_auxilar(0) - margem_x
        if orientacao_y == 3:
            pos_y = self.retangulo.y + self.altura - self.tamanho_texto_auxilar(1) - margem_y

        self.texto_auxiliar_pos_x = pos_x
        self.texto_auxiliar_pos_y = pos_y
        self.texto_auxiliar_pos = (self.texto_auxiliar_pos_x, self.texto_auxiliar_pos_y)


    def visual_relativo(self, chave):
        self.visual = self.retangulo.move(-self.TELA.cameras[chave].x, 
                                          -self.TELA.cameras[chave].y)


    def define_pos_texto_auxiliar_visual(self, orientacao_x, orientacao_y, 
                         porcentagem_margem_x, porcentagem_margem_y):
        margem_x = self.largura * porcentagem_margem_x / 100 
        margem_y = self.altura * porcentagem_margem_y / 100 
        if orientacao_x == 1:
            pos_x = self.visual.x + margem_x
        if orientacao_y == 1:
            pos_y = self.visual.y + margem_y

        if orientacao_x == 2:
            pos_x = self.visual.x + (self.largura - self.tamanho_texto_auxilar(0)) / 2 
        if orientacao_y == 2:
            pos_y = self.visual.y + (self.altura - self.tamanho_texto_auxilar(1)) / 2 
            
        if orientacao_x == 3:
            pos_x = self.visual.x +self.largura - self.tamanho_texto_auxilar(0) - margem_x
        if orientacao_y == 3:
            pos_y = self.visual.y + self.altura - self.tamanho_texto_auxilar(1) - margem_y

        self.texto_auxiliar_pos_x = pos_x
        self.texto_auxiliar_pos_y = pos_y
        self.texto_auxiliar_pos = (self.texto_auxiliar_pos_x, self.texto_auxiliar_pos_y)


    def mostra_texto(self):
        self.TELA.tela.blit(self.texto, self.texto_pos)


    def mostra_texto_auxiliar(self):
        self.TELA.tela.blit(self.texto_auxiliar, self.texto_auxiliar_pos)
