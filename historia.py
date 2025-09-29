import pygame
from utils.classes import Tela
from utils.classes import Caixa_de_texto
from utils.arquivo_cores import cores
from utils.funcoes_principais import fim
from utils.funcoes_principais import pega_evento

def passa_texto(historia,evento):
    if evento and evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN:
            historia.i_linha += 1 
            if historia.i_linha > len(historia.linhas_de_texto) - 1: 
                return False
    return True


def apresenta_historia(TELA):
    TELA.cor = cores['ceu']

    historia = Caixa_de_texto(0,0,100,100, TELA)
    linhas_historia = [f'Seu irmão foi sequestrado por piratas, por esse motivo você',
                f'terá de percorrer uma caminho de ilhas até o covil desses piratas.', 
                f'Em cada ilha você terá de achar as coordenadas para seguir em frente.',
                f'Boa, sorte!']
    historia.define_linhas_de_texto(linhas_historia)
    historia.define_fonte(3.5)
    historia.cria_texto_auxiliar('APERTE ENTER', 2)
    historia.define_pos_texto_auxiliar(3,3, 1,2)

    while True:
        TELA.tela.fill(TELA.cor)
        historia.renderiza_texto()
        historia.define_pos_texto(2,2,0,0)
        TELA.tela.blit(historia.texto, historia.texto_pos)
        TELA.tela.blit(historia.texto_auxiliar, historia.texto_auxiliar_pos)
        evento = pega_evento()
        if fim(evento): break
        if not passa_texto(historia, evento): break
        pygame.display.flip()


def final_historia(TELA):
    TELA.cor = cores['ceu']

    historia = Caixa_de_texto(0,0,100,100, TELA)
    linhas_da_historia = [f'Parabéns, você conseguiu recuperar seu irmão',
                f'Sua missão está completa']
    historia.define_linhas_de_texto(linhas_da_historia)
    historia.define_fonte(3.5)
    historia.cria_texto_auxiliar('APERTE ENTER', 2)
    historia.define_pos_texto_auxiliar(3,3, 1,2)

    while True:
        TELA.tela.fill(TELA.cor)
        historia.renderiza_texto()
        historia.define_pos_texto(2,2,0,0)
        TELA.tela.blit(historia.texto, historia.texto_pos)
        TELA.tela.blit(historia.texto_auxiliar, historia.texto_auxiliar_pos)
        evento = pega_evento()
        if fim(evento): break
        if not passa_texto(historia, evento): break
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    apresenta_historia(TELA)
    final_historia(TELA)
    pygame.quit()
