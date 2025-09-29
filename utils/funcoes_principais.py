import pygame
import os, sys

def resource_path(rel_path):
    """Retorna o caminho absoluto para recurso, compatível com PyInstaller."""
    if getattr(sys, 'frozen', False):  # executável criado pelo PyInstaller
        base_path = sys._MEIPASS       # pasta temporária usada pelo PyInstaller
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, rel_path)


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


def passa_dialogo(dialogo, evento):
    if evento and evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN:
            dialogo.i_linha += 1

            if dialogo.i_linha == len(dialogo.linhas_de_texto):
                dialogo.aparece = False

            if dialogo.i_linha > len(dialogo.linhas_de_texto):
                dialogo.i_linha = 0
                dialogo.aparece = True


def passa_notificacao(notificacao, evento):
    if evento and evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_SPACE:
            notificacao.aparece = False


def pulo_e_queda(keys, jogador):
    if keys[pygame.K_SPACE]:
        jogador.pular()

    jogador.queda_constante()


def cima_baixo_esquerda_direita(keys, jogador):
    cima(keys, jogador)
    baixo(keys, jogador)
    esquerda(keys, jogador)
    direita(keys, jogador)


def esquerda_direita(keys, jogador):
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
