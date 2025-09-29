import pygame
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Jogador
from utils.classes import Retangulo
from utils.classes import Triangulo
from utils.classes import Caixa_de_texto
from utils.funcoes_principais import fim
from utils.funcoes_principais import pega_evento
from utils.funcoes_principais import pulo_e_queda
from utils.funcoes_principais import passa_dialogo
from telas import tela_ganhou
from telas import tela_perdeu
from random import randint

def desenha_jogo(TELA, jogador, obstaculos, planice, dialogo):
    TELA.tela.blit(TELA.textura, (0,0))
    jogador.texturiza()
    for o in obstaculos:
        if o.tipo == 'Retangulo': 
            o.texturiza()

        elif o.tipo == 'Triangulo':
            o.texturiza()

    if obstaculos == []:
        pygame.draw.rect(TELA.tela, planice.cor, planice.retangulo)
        planice.texturiza()

    if dialogo.aparece:
        pygame.draw.rect(TELA.tela, dialogo.cor, dialogo.retangulo)
        dialogo.renderiza_texto()
        dialogo.define_pos_texto(2,2,0,0)
        TELA.tela.blit(dialogo.texto, dialogo.texto_pos)
        TELA.tela.blit(dialogo.texto_auxiliar, dialogo.texto_auxiliar_pos)


def cria_lista_obstaculos(num_obstaculos, distancia_entre_obstaculos, TELA):
    obstaculos = (num_obstaculos + 1) * [None]
    x_obstaculo = 100
    obstaculos[0] = Retangulo(-54.9,35,65,65, TELA)
    obstaculos[0].define_textura('textura/planalto.png')
    for i in range(1, len(obstaculos)):
        selecao = randint(0, 3) 
        montanha = Triangulo(x_obstaculo, 20, 60, 80, TELA)
        planalto = Retangulo(x_obstaculo, 35, 65, 65, TELA)
        if selecao == 0:
            obstaculo = planalto
            obstaculo.define_textura('textura/planalto.png')
        else:
            obstaculo = montanha
            obstaculo.define_textura('textura/montanha.png')
        obstaculos[i] = obstaculo
        x_obstaculo += distancia_entre_obstaculos
    return obstaculos


def mecanica(TELA, jogador, obstaculos, planice):
    perdeu = False
    ganhou = False
    if obstaculos:
        keys = pygame.key.get_pressed()
        pulo_e_queda(keys, jogador)
    removidos = 0
    for i in range(len(obstaculos)):
        i -= removidos
        obstaculos[i].move_constante_para_esquerda()
        if obstaculos[i].tipo == 'Retangulo':
            if obstaculos[i].retangulo.colliderect(jogador.retangulo):
                perdeu = True
            if obstaculos[i].retangulo.x + obstaculos[i].largura <= 0:
                obstaculos.pop(i)
                removidos += 1
        elif obstaculos[i].tipo == 'Triangulo':
            if obstaculos[i].colidiu(jogador):
                perdeu = True
            if obstaculos[i].vertice3[0] <= 0:
                obstaculos.pop(i)
                removidos += 1

    if jogador.retangulo.y <= 0:
        perdeu = True
    if jogador.retangulo.y >= TELA.ALTURA - jogador.altura:
        perdeu = True
    if obstaculos == []:
        if jogador.retangulo.x < planice.retangulo.x * 150/100:
            jogador.retangulo.x += planice.velocidade
        if jogador.retangulo.y + jogador.altura < planice.retangulo.y:
            jogador.retangulo.y += planice.velocidade * 0.50
        if planice.retangulo.x > TELA.LARGURA * 50/100:
            planice.move_constante_para_esquerda()
    if planice.retangulo.colliderect(jogador.retangulo):
        ganhou = True

    return ganhou, perdeu


def fase2(TELA):
    TELA.cor = cores['ceu']

    TELA.define_textura('textura/ceu.png')

    jogador = Jogador(7.8, 27, 3.4, 6.1, TELA)
    jogador.gravidade = (TELA.ALTURA/600) * 0.25
    jogador.define_textura('textura/com_asas.png')
    obstaculos = cria_lista_obstaculos(10, 75 + 20.3, TELA) 
    planice = Retangulo(100, 95.9, 50, 4.1, TELA)
    planice.define_textura('textura/grama.png')

    dialogo = Caixa_de_texto(30,42.5,40,15, TELA)
    linhas_do_dialogo = [f'Esta ilha tem várias formas de relevo,',
                    f'você vai precisar passar voando pelas montanhas e planaltos',
                    f'até chegar na planice no final da ilha, onde conseguiremos sair',
                    f'Cuidado para não bater nas montanhas ou nos planaltos,',
                    f'Além disso, não caia nem vá muito para cima,',
                    f'Quanto mais alto menos oxigênio',
                    f'Pode começar, aperte espaço para voar.']
    dialogo.define_linhas_de_texto(linhas_do_dialogo)
    dialogo.define_fonte(1.7)
    dialogo.cria_texto_auxiliar('APERTE ENTER', 1)
    dialogo.define_pos_texto_auxiliar(3,3, 1,4)
    
    clock = pygame.time.Clock()
    FPS = 60

    ganhou = False
    perdeu = False
    while True:
        desenha_jogo(TELA, jogador, obstaculos, planice, dialogo)
        evento = pega_evento()
        passa_dialogo(dialogo, evento)
        if not dialogo.aparece:
            ganhou, perdeu = mecanica(TELA, jogador, obstaculos, planice)
        if fim(evento) or perdeu or ganhou: break 
        pygame.display.flip()
        clock.tick(FPS)
    retorno = 'Tela inicial'
    retorno = tela_perdeu(TELA) if perdeu else retorno
    retorno = tela_ganhou(TELA) if ganhou else retorno
    return retorno, ganhou
    

if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    print(fase2(TELA))
    pygame.quit()
