import pygame
from .arquivo_cores import cores
from .classes import Tela
from .classes import Retangulo

def pega_evento():
    for evento in pygame.event.get():
        return evento

def fim(evento):
    if evento:
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
    cima(keys, jogador)
    baixo(keys, jogador)
    esquerda(keys, jogador)
    direita(keys, jogador)


def cima(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima()


def baixo(keys, jogador):
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo()


def esquerda(keys, jogador):
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda()
    

def direita(keys, jogador):
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita()


def cima_baixo_esquerda_direita_no_mapa(keys, jogador):
    cima_no_mapa(keys, jogador)
    baixo_no_mapa(keys, jogador)
    esquerda_no_mapa(keys, jogador)
    direita_no_mapa(keys, jogador)

def cima_no_mapa(keys, jogador):
    if keys[pygame.K_UP]:
        jogador.move_para_cima_no_mapa()
    

def baixo_no_mapa(keys, jogador):
    if keys[pygame.K_DOWN]:
        jogador.move_para_baixo_no_mapa()


def esquerda_no_mapa(keys, jogador):
    if keys[pygame.K_LEFT]:
        jogador.move_para_esquerda_no_mapa()
    

def direita_no_mapa(keys, jogador):
    if keys[pygame.K_RIGHT]:
        jogador.move_para_direita_no_mapa()


def desenha_tela_ganhador(TELA):
    TELA.tela.fill(cores['dourado'])
    fonte = pygame.font.Font(None, 150)
    texto = fonte.render('Parabéns', False, cores['branco'])
    largura_texto, altura_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - largura_texto) // 2, (TELA.ALTURA - altura_texto) // 2))


def desenha_tela_perdeu(TELA):
    TELA.tela.fill(cores['preto'])
    fonte = pygame.font.Font(None, 150)
    texto = fonte.render('Perdeu', False, cores['branco'])
    largura_texto, altura_texto = texto.get_size()
    TELA.tela.blit(texto, ((TELA.LARGURA - largura_texto) // 2, ((TELA.ALTURA - altura_texto) // 2)))


def roda_perdeu(TELA):
    while True:
        desenha_tela_perdeu(TELA)
        if fim(): break
        pygame.display.flip()


def roda_ganhou(TELA):
    while True:
        desenha_tela_ganhador(TELA)
        if fim(): break
        pygame.display.flip()


def desenha_tela_incial(TELA, opcoes):
    TELA.tela.fill(TELA.cor)
    for c in opcoes:
        pygame.draw.rect(TELA.tela, opcoes[c].cor, opcoes[c].retangulo)


def tela_incial():
    pygame.init()

    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    TELA.cor = cores['preto']

    opcoes = {}
    opcoes['Iniciar'] = Retangulo(40,0,20,10,TELA)
    opcoes['Fase 1'] = Retangulo(40,10,20,10,TELA)
    opcoes['Fase 2'] = Retangulo(40,20,20,10,TELA)
    opcoes['Fase 3'] = Retangulo(40,30,20,10,TELA)
    opcoes['Fase 4'] = Retangulo(40,40,20,10,TELA)
    opcoes['Sair'] = Retangulo(40,50,20,10,TELA)

    clock = pygame.time.Clock()
    FPS = 60
    while True:
        desenha_tela_incial(TELA, opcoes)
        if fim(): break
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
