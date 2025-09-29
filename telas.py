import pygame
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Retangulo
from utils.funcoes_principais import fim

def desenha_tela(TELA, opcoes, titulo):
    TELA.tela.fill(TELA.cor)
    fonte = pygame.font.Font(None, 37)
    fonte_titulo = pygame.font.Font(None, 150)
    titulo = fonte_titulo.render(f'{titulo}', False, cores['branco'])
    largura_titulo, altura_titulo = titulo.get_size()
    titulo_pos_x = (TELA.LARGURA - largura_titulo) / 2
    titulo_pos_y = (TELA.ALTURA / 2 - altura_titulo) - TELA.LARGURA * 5/100
    TELA.tela.blit(titulo, (titulo_pos_x, titulo_pos_y))
    textos = {}
    textos_rect = {}
    for i in range(len(opcoes)):
        c = opcoes[i][0]
        textos[c] = fonte.render(c, True, cores['branco']) 
        if opcoes[i][1].aparece:
            pygame.draw.rect(TELA.tela, opcoes[i][1].cor, opcoes[i][1].retangulo)
        textos_rect[c] = textos[c].get_rect(center=opcoes[i][1].retangulo.center)
        TELA.tela.blit(textos[c], textos_rect[c])


def seleciona_opcao(opcoes, i, selecionado, rodando):
    opcoes[i][1].aparece = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                if i < len(opcoes) - 1:
                    opcoes[i][1].aparece = False
                    i += 1 
                else:
                    opcoes[i][1].aparece = False
                    i -= len(opcoes) - 1

            if evento.key == pygame.K_UP:
                if i > 0:                     
                    opcoes[i][1].aparece = False
                    i -= 1 
                else:
                    opcoes[i][1].aparece = False
                    i += len(opcoes) - 1

            if evento.key == pygame.K_RETURN:
                selecionado = True
    return i, selecionado, rodando


def tela_inicial(TELA):
    TELA.cor = cores['ceu']

    opcoes = [['Iniciar', Retangulo(44,50,10,5.5,TELA)],
              ['Reiniciar', Retangulo(44,55.5,10,5.5,TELA)],
              ['Fase 1', Retangulo(44,61,10,5.5,TELA)],
              ['Fase 2', Retangulo(44,66.5,10,5.5,TELA)],
              ['Fase 3', Retangulo(44,72,10,5.5,TELA)],
              ['Fase 4', Retangulo(44,77.5,10,5.5,TELA)],
              ['Sair', Retangulo(44,82,10,5.5,TELA)]]
    for i in range(len(opcoes)):
        opcoes[i][1].aparece = False
        opcoes[i][1].cor = cores['amarelo']
    i = 0

    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    selecionado = False
    while True:
        desenha_tela(TELA, opcoes, 'TERRA À VISTA')
        if not rodando: break
        i, selecionado, rodando = seleciona_opcao(opcoes, i, selecionado, rodando)
        if selecionado:
            return opcoes[i][0]
        pygame.display.flip()
        clock.tick(FPS)


def tela_perdeu(TELA):
    TELA.cor = cores['ceu']

    opcoes = [['Reiniciar', Retangulo(44,50,10,5.5,TELA)],
              ['Tela inicial', Retangulo(44,55.5,10,5.5,TELA)]]

    for i in range(len(opcoes)):
        opcoes[i][1].aparece = False
        opcoes[i][1].cor = cores['amarelo']
    i = 0

    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    selecionado = False
    while True:
        desenha_tela(TELA, opcoes, 'PERDEU')
        if not rodando: break
        i, selecionado, rodando = seleciona_opcao(opcoes, i, selecionado, rodando)
        if selecionado:
            return opcoes[i][0]
        pygame.display.flip()
        clock.tick(FPS)


def tela_ganhou(TELA):
    TELA.cor = cores['ceu']

    opcoes = [['Próxima Fase', Retangulo(44,50,10,5.5,TELA)],
              ['Tela inicial', Retangulo(44,55.5,10,5.5,TELA)]]

    for i in range(len(opcoes)):
        opcoes[i][1].aparece = False
        opcoes[i][1].cor = cores['amarelo']
    i = 0

    clock = pygame.time.Clock()
    FPS = 60
    rodando = True
    selecionado = False
    while True:
        desenha_tela(TELA, opcoes, 'GANHOU')
        if not rodando: break
        i, selecionado, rodando = seleciona_opcao(opcoes, i, selecionado, rodando)
        if selecionado:
            return opcoes[i][0]
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    print(tela_inicial(TELA))
    print(tela_perdeu(TELA))
    print(tela_ganhou(TELA))
    pygame.quit()
