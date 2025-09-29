import pygame
from random import randint
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Jogador
from utils.classes import Retangulo
from utils.classes import Tesouro
from utils.classes import Caixa_de_texto
from utils.funcoes_principais import fim
from utils.funcoes_principais import pega_evento
from utils.funcoes_principais import esquerda
from utils.funcoes_principais import direita
from utils.funcoes_principais import passa_dialogo
from telas import tela_perdeu
from telas import tela_ganhou
from historia import final_historia

def desenha_jogo(TELA, jogador, rio, obstaculos, tesouro, mar, pontuacao, dialogo):
    TELA.tela.fill(TELA.cor)
    pygame.draw.rect(TELA.tela, rio.cor, rio.retangulo)
    if tesouro.aparece:
        tesouro.texturiza()
    for obstaculo in obstaculos:
        obstaculo.texturiza()
    pygame.draw.rect(TELA.tela, mar.cor, mar.retangulo)
    jogador.texturiza()
    if dialogo.aparece:
        pygame.draw.rect(TELA.tela, dialogo.cor, dialogo.retangulo)
        dialogo.renderiza_texto()
        dialogo.define_pos_texto(2,2,0,0)
        TELA.tela.blit(dialogo.texto, dialogo.texto_pos)
        TELA.tela.blit(dialogo.texto_auxiliar, dialogo.texto_auxiliar_pos)


def cria_obstaculos(TELA):
    conjuntos_de_obstaculo = {}
    conjuntos_de_obstaculo[-1] = [Retangulo(30, -32, 60, 32, TELA)]
    conjuntos_de_obstaculo[0] = [Retangulo(10, -32, 60, 32, TELA)]
    conjuntos_de_obstaculo[1] = [Retangulo(20, -32, 60, 32, TELA)]
    conjuntos_de_obstaculo[2] = [Retangulo(12.3, -20, 34.25, 20, TELA),
                                 Retangulo(53.45, -20, 34.25, 20, TELA)]
    conjuntos_de_obstaculo[3] = [Retangulo(12.3, -20, 22.8, 20, TELA),
                                 Retangulo(64.8, -20, 22.8, 20, TELA),
                                 Retangulo(38.55, -55, 22.8, 20, TELA)]
    conjuntos_de_obstaculo[4] = [Retangulo(10, -20, 40, 10, TELA),
                                 Retangulo(50, -50, 40, 10, TELA),
                                 Retangulo(10, -80, 40, 10, TELA),
                                 Retangulo(50, -110, 40, 10, TELA)]
    conjuntos_de_obstaculo[5] = [Retangulo(12.3, -20, 22.8, 20, TELA),
                                 Retangulo(64.8, -20, 22.8, 20, TELA),
                                 Retangulo(38.55, -60, 22.8, 20, TELA),
                                 Retangulo(12.3, -100, 22.8, 20, TELA),
                                 Retangulo(64.8, -100, 22.8, 20, TELA)]
    for c in conjuntos_de_obstaculo:
        for e in conjuntos_de_obstaculo[c]:
            e.define_velocidade(0.3)
            e.cor = cores['pedra']
            e.define_textura('textura/pedras.png')
    return conjuntos_de_obstaculo


def cria_tesouros(TELA):
    tesouros = {}
    tesouros[-1] = Tesouro(randint(10, 27), randint(-32, 0), 2.3, 4.1,TELA) 
    tesouros[0] = Tesouro(randint(70, 87), randint(-32, 0), 2.3, 4.1, TELA)
    selecao = randint(0,1)
    if selecao:
        tesouros[1] = Tesouro(randint(10, 15), randint(-32, 0), 2.3, 4.1, TELA)
        tesouros[3] = Tesouro(randint(23, 35), -55, 2.3, 4.1, TELA)
        tesouros[4] = Tesouro(30.9, -47.05, 2.3, 4.1, TELA)
    else:
        tesouros[1] = Tesouro(randint(80, 85), randint(-32, 0), 2.3, 4.1, TELA)
        tesouros[3] = Tesouro(randint(62, 87), -55, 2.3, 4.1, TELA)
        tesouros[4] = Tesouro(55, -77.05, 2.3, 4.1, TELA)
    tesouros[2] = Tesouro(48.85, -12.05, 2.3, 4.1, TELA) 
    tesouros[5] = tesouros[3]
    for c in tesouros:
        tesouros[c].define_velocidade(0.3)
        tesouros[c].cor = cores['dourado']
        tesouros[c].define_textura('textura/tesouro.png')
    return tesouros


def chegando_no_mar(mar, ganhou):
    if mar.retangulo.y < 0:
        mar.move_constante_para_baixo()
    else:
        ganhou = True
    return ganhou


def mecanica(TELA, jogador, obstaculos, tesouros, c, perdeu, pontuacao):
    keys = pygame.key.get_pressed()
    direita(keys, jogador)
    esquerda(keys, jogador)

    for obstaculo in obstaculos[c]:
        obstaculo.move_constante_para_baixo()
        if obstaculo.retangulo.colliderect(jogador.retangulo):
            perdeu = True
        if obstaculos[c][len(obstaculos[c])-1].retangulo.y >= TELA.ALTURA:
            obstaculos = cria_obstaculos(TELA)
            tesouros = cria_tesouros(TELA)
            c = randint(-1,5)

    if jogador.retangulo.colliderect(tesouros[c].retangulo):
        pontuacao += 1 if tesouros[c].aparece else 0
        tesouros[c].aparece = False
    tesouros[c].move_constante_para_baixo()

    return perdeu, c, obstaculos, tesouros, pontuacao


def fase4(TELA):
    TELA.cor = cores['floresta_tropical']
    tesouros = cria_tesouros(TELA)
    rio = Retangulo(10, 0, 80, 100, TELA)
    rio.cor = cores['mar']

    obstaculos = cria_obstaculos(TELA)
    c = randint(-1,5)

    mar = Retangulo(0, -100, 100, 100, TELA)
    mar.cor = cores['mar']
    mar.define_velocidade(0.3)

    jogador = Jogador(48.85, 75, 2.3, 4.1, TELA)
    jogador.define_velocidade(0.5)
    jogador.define_textura('textura/com_canoa.png')

    dialogo = Caixa_de_texto(30,42.5,40,15, TELA)
    linhas_do_dialogo = [f'Seu irmão está nessa ilha, está na hora de busca-lo',
                    f'agora que você conseguiu resgatar ele',
                    f'você tem que sair da ilha atravéz do rio',
                    f'Siga pegando as coordenadas até o mar',
                    f'Desvie das pedras deslizando para a esquerda e direita']
    dialogo.define_linhas_de_texto(linhas_do_dialogo)
    dialogo.define_fonte(1.7)
    dialogo.cria_texto_auxiliar('APERTE ENTER', 1)
    dialogo.define_pos_texto_auxiliar(3,3, 1,4)

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    PONTUACAO_MAXIMA = 10
    rodando = True
    perdeu = False
    ganhou = False
    while rodando:
        desenha_jogo(TELA, jogador, rio, obstaculos[c], 
                     tesouros[c], mar, pontuacao, dialogo)
        evento = pega_evento()
        if not dialogo.aparece:
            jogador.retangulo.clamp_ip(rio.retangulo)
            perdeu, c, obstaculos, tesouros, pontuacao = mecanica(
                    TELA, jogador, obstaculos, tesouros, c, perdeu, pontuacao)
        passa_dialogo(dialogo, evento)
        if fim(evento) or perdeu or ganhou: break
        if pontuacao >= PONTUACAO_MAXIMA:
            ganhou = chegando_no_mar(mar, ganhou)
        pygame.display.flip()
        clock.tick(FPS)
    retorno = 'Tela inicial'
    if ganhou:
        final_historia(TELA)
    retorno = tela_perdeu(TELA) if perdeu else retorno
    return retorno, ganhou

        
if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    print(fase4(TELA))
    pygame.quit()
