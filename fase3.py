import pygame
from utils.arquivo_cores import cores
from utils.classes import Tela
from utils.classes import Jogador
from utils.classes import Tesouro
from utils.classes import Caixa_de_texto
from utils.funcoes_principais import fim
from utils.funcoes_principais import pega_evento
from utils.funcoes_principais import cima_baixo_esquerda_direita
from utils.funcoes_principais import passa_dialogo
from utils.funcoes_principais import passa_notificacao
from telas import tela_ganhou

def desenha_inicio(TELA, jogador, entradas, pontuacao, dialogo):
    TELA.tela.fill(TELA.cor)
    TELA.texturiza_mundo('inicio')
    for bioma in entradas:
        TELA.tela.blit(entradas[bioma].texto_auxiliar, 
                       entradas[bioma].texto_auxiliar_pos)
    jogador.texturiza()
    fonte = pygame.font.Font(None, 40)
    texto = fonte.render(f'Materiais: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()
    pontuacao_pos_x = (TELA.LARGURA - tamanho_texto[0]) // 2
    TELA.tela.blit(texto, (pontuacao_pos_x, 5))
    if dialogo.aparece:
        pygame.draw.rect(TELA.tela, dialogo.cor, dialogo.retangulo)
        dialogo.renderiza_texto()
        dialogo.define_pos_texto(2,2,0,0)
        dialogo.mostra_texto()
        dialogo.mostra_texto_auxiliar()


def desenha_bioma(TELA, ambiente, jogador, tesousos, saida, pontuacao, conquista):
    TELA.cor = cores[ambiente]
    TELA.tela.fill(TELA.cor)
    visual = TELA.mundos[ambiente].move(-TELA.cameras[ambiente].x, 
                                       -TELA.cameras[ambiente].y)
    TELA.tela.blit(TELA.texturas[ambiente], (visual.x,visual.y))
    jogador.visual_relativo(ambiente)
    jogador.texturiza_visual()
    saida.visual_relativo(ambiente)
    saida.define_pos_texto_auxiliar_visual(2,2,0,0)
    saida.mostra_texto_auxiliar()
    if tesousos:
        tesousos[0].visual_relativo(ambiente)
        tesousos[0].texturiza_visual()
        TELA.desenha_no_mapa(ambiente, [jogador, saida, tesousos[0]])
    else:
        TELA.desenha_no_mapa(ambiente, [jogador, saida])
    TELA.tela.blit(TELA.mapas[ambiente], (TELA.mapas_pos_x[ambiente],
                                          TELA.mapas_pos_y[ambiente]))
    fonte = pygame.font.Font(None, 40)
    texto = fonte.render(f'Materiais: {pontuacao}', False, cores['branco'])
    tamanho_texto = texto.get_size()
    pontuacao_pos_x = (TELA.LARGURA - tamanho_texto[0]) // 2
    TELA.tela.blit(texto, (pontuacao_pos_x, 5))
    if conquista.aparece:
        pygame.draw.rect(TELA.tela, conquista.cor, conquista.retangulo)
        conquista.renderiza_texto()
        conquista.define_pos_texto(2,2,0,0)
        conquista.mostra_texto()
        conquista.mostra_texto_auxiliar()


def regras_biomas(jogador, tesousos, saida, ambiente, pontuacao, conquista):
    if tesousos:
        if jogador.retangulo.colliderect(tesousos[0].retangulo):
            tesousos.pop(0)
            conquista.aparece = True 
            pontuacao += 1
    if jogador.retangulo.colliderect(saida.retangulo):
        ambiente = 'inicio'
    return pontuacao, ambiente


def cria_jogadores(TELA):
    jogadores = {}
    jogadores['inicio'] = Jogador(48.85, 47.95,3, 6, TELA)
    jogadores['inicio'].define_velocidade(0.5)

    jogadores['manguezal'] = Jogador(143, 262,3, 6, TELA)
    jogadores['manguezal'].define_velocidade(0.5)
    jogadores['manguezal'].posicao_inicial =  {'x':jogadores['manguezal'].retangulo.x, 
                                               'y':jogadores['manguezal'].retangulo.y}

    jogadores['deserto'] = Jogador(10, 262,3, 6, TELA)
    jogadores['deserto'].define_velocidade(0.5)
    jogadores['deserto'].posicao_inicial =  {'x':jogadores['deserto'].retangulo.x, 
                                             'y':jogadores['deserto'].retangulo.y}

    jogadores['savana'] = Jogador(143, 10,3, 6, TELA)
    jogadores['savana'].define_velocidade(0.5)
    jogadores['savana'].posicao_inicial =  {'x':jogadores['savana'].retangulo.x, 
                                            'y':jogadores['savana'].retangulo.y}

    jogadores['floresta_tropical'] = Jogador(10, 10,3,6, TELA)
    jogadores['floresta_tropical'].define_velocidade(0.5)
    jogadores['floresta_tropical'].posicao_inicial =  {
                                        'x':jogadores['floresta_tropical'].retangulo.x, 
                                        'y':jogadores['floresta_tropical'].retangulo.y}
    for b in jogadores:
        jogadores[b].define_textura_baixo('textura/baixo.png')
        jogadores[b].define_textura_cima('textura/cima.png')
        jogadores[b].define_textura_esquerda('textura/esquerda.png')
        jogadores[b].define_textura_direita('textura/direita.png')
        jogadores[b].textura = jogadores[b].textura_baixo
    return jogadores


def cria_listas_de_tesouros(TELA):
    tesouros = {}
    largura_tesouro = 4.6
    altura_tesouro = 8.2
    tesouros['manguezal'] = [Tesouro(5.4, 14.2, largura_tesouro, altura_tesouro, TELA),
                Tesouro(30, 237, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 35, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 210, largura_tesouro, altura_tesouro, TELA),
                Tesouro(44.4, 150, largura_tesouro, altura_tesouro, TELA)]
    tesouros['deserto'] = [Tesouro(5.4, 14.2, largura_tesouro, altura_tesouro, TELA),
                Tesouro(30, 237, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 35, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 210, largura_tesouro, altura_tesouro, TELA),
                Tesouro(44.4, 150, largura_tesouro, altura_tesouro, TELA)]
    tesouros['savana'] = [Tesouro(5.4, 14.2, largura_tesouro, altura_tesouro, TELA),
                Tesouro(30, 237, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 35, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 210, largura_tesouro, altura_tesouro, TELA),
                Tesouro(44.4, 150, largura_tesouro, altura_tesouro, TELA)]
    tesouros['floresta_tropical'] = [Tesouro(5.4, 14.2, largura_tesouro, altura_tesouro, TELA),
                Tesouro(30, 237, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 35, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 210, largura_tesouro, altura_tesouro, TELA),
                Tesouro(44.4, 150, largura_tesouro, altura_tesouro, TELA)]
    for b in tesouros:
        for tesouro in tesouros[b]:
            tesouro.cor = cores['dourado']
            tesouro.define_textura('textura/tesouro.png')
    return tesouros


def cria_saidas(TELA):
    saidas = {}
    saidas['manguezal'] = Caixa_de_texto(146, 267, 10, 10, TELA)
    saidas['deserto'] = Caixa_de_texto(0, 267, 10, 10, TELA)
    saidas['savana'] = Caixa_de_texto(146, 0, 10, 10, TELA)
    saidas['floresta_tropical'] = Caixa_de_texto(0, 0, 10, 10, TELA)
    for b in saidas:
        saidas[b].cria_texto_auxiliar('SAÍDA', 3)
        saidas[b].cor = cores['areia']
    return saidas


def cria_entradas(TELA):
    entradas = {}
    entradas['manguezal'] = Caixa_de_texto(0, 0, 10, 10, TELA)
    entradas['manguezal'].cria_texto_auxiliar('Manguezal', 1.5)

    entradas['deserto'] = Caixa_de_texto(90, 0, 10, 10, TELA)
    entradas['deserto'].cria_texto_auxiliar('Deserto', 1.5)

    entradas['savana'] = Caixa_de_texto(0, 90, 10, 10, TELA)
    entradas['savana'].cria_texto_auxiliar('Savana', 1.5)

    entradas['floresta_tropical'] = Caixa_de_texto(90, 90, 10, 10, TELA)
    entradas['floresta_tropical'].cria_texto_auxiliar('Floresta Tropical', 1.5)
    for b in entradas:
        entradas[b].define_pos_texto_auxiliar(2,2, 0,0)
    return entradas


def fase3(TELA):
    TELA.cria_mundo('inicio', 100, 100)
    TELA.define_textura_mundo('inicio', 'textura/fase3.png')

    TELA.cria_mundo('manguezal', 156, 277)
    TELA.cria_camera('manguezal')
    TELA.define_textura_mundo('manguezal', 'textura/manguezal.png')
    TELA.cria_mapa('manguezal',1/10, 1, 2)

    TELA.cria_mundo('deserto', 156, 277)
    TELA.cria_camera('deserto')
    TELA.define_textura_mundo('deserto', 'textura/deserto.png')
    TELA.cria_mapa('deserto',1/10, 83, 2)

    TELA.cria_mundo('savana', 156, 277)
    TELA.cria_camera('savana')
    TELA.define_textura_mundo('savana', 'textura/savana.png')
    TELA.cria_mapa('savana',1/10, 1, 71)

    TELA.cria_mundo('floresta_tropical', 156, 277)
    TELA.cria_camera('floresta_tropical')
    TELA.define_textura_mundo('floresta_tropical', 'textura/floresta_tropical.png')
    TELA.cria_mapa('floresta_tropical',1/10, 84, 71)

    jogadores = cria_jogadores(TELA)
    tesouros = cria_listas_de_tesouros(TELA)
    saidas = cria_saidas(TELA)

    entradas = cria_entradas(TELA)
    for b in entradas:
        entradas[b].cor = cores[b]

    dialogo = Caixa_de_texto(30,42.5,40,15, TELA)
    linhas_do_dialogo = [f'Aqui nessa ilha há diversos biomas, você vai ter que ir',
                    f'até os biomas de mangue, deserto, savana e floresta tropical',
                    f'para coletar diversos materiais (5 em cada bioma),', 
                    f'você teŕa de ver a localiação',
                    f'de cada um em seus respectivos mapas',
                    f'Quando terminar de coletar podemos partir para a próxima ilha']
    dialogo.define_linhas_de_texto(linhas_do_dialogo)
    dialogo.define_fonte(1.7)
    dialogo.cria_texto_auxiliar('APERTE ENTER', 1)
    dialogo.define_pos_texto_auxiliar(3,3, 1,4)

    conquista = Caixa_de_texto(30,42.5,40,15, TELA)
    linha_conquista = [f'Você conseguiu um material']
    conquista.define_linhas_de_texto(linha_conquista)
    conquista.define_fonte(1.7)
    conquista.cria_texto_auxiliar('APERTE ESPAÇO', 1)
    conquista.define_pos_texto_auxiliar(3,3, 1,4)
    conquista.aparece = False

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    ambiente = 'inicio'
    ganhou = False
    while True:
        keys = pygame.key.get_pressed()
        if ambiente == 'inicio':
            TELA.cor = cores['areia']
            jogadores[ambiente].retangulo.clamp_ip(TELA.mundos[ambiente])
            desenha_inicio(TELA, jogadores['inicio'], entradas, pontuacao, dialogo)
            cima_baixo_esquerda_direita(keys, jogadores['inicio'])
            for b in entradas:
                if jogadores['inicio'].retangulo.colliderect(entradas[b].retangulo):
                    ambiente = b
        
        else:
            TELA.cameras[ambiente].center = jogadores[ambiente].retangulo.center
            TELA.cameras[ambiente].clamp_ip(TELA.mundos[ambiente])
            jogadores[ambiente].retangulo.clamp_ip(TELA.mundos[ambiente])
            desenha_bioma(TELA, ambiente, jogadores[ambiente], tesouros[ambiente], 
                          saidas[ambiente], pontuacao, conquista)
            pontuacao, ambiente = regras_biomas(jogadores[ambiente], tesouros[ambiente], 
                                                saidas[ambiente], ambiente, 
                                                pontuacao, conquista)
        
        if ambiente == 'manguezal':
            jogadores['inicio'].define_posicao(11,11)
            TELA.cor = cores[ambiente]
            cima_baixo_esquerda_direita(keys, jogadores['manguezal'])

        if ambiente == 'deserto':
            jogadores['inicio'].define_posicao(87.7,11)
            TELA.cor = cores[ambiente]
            cima_baixo_esquerda_direita(keys, jogadores['deserto'])

        if ambiente == 'savana':
            jogadores['inicio'].define_posicao(11,85.9)
            TELA.cor = cores[ambiente]
            cima_baixo_esquerda_direita(keys, jogadores['savana'])

        if ambiente == 'floresta_tropical':
            jogadores['inicio'].define_posicao(85,85)
            TELA.cor = cores[ambiente]
            cima_baixo_esquerda_direita(keys, jogadores['floresta_tropical'])
            
        evento = pega_evento()
        if fim(evento): break 
        passa_dialogo(dialogo,evento)
        passa_notificacao(conquista,evento)
        if [v for v in tesouros.values()] == [[],[],[],[]]:
            ganhou = True
            break
        pygame.display.flip()
        clock.tick(FPS)
    retorno = tela_ganhou(TELA) if ganhou else 'Tela inicial'
    return retorno, ganhou
                                                  

if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    print(fase3(TELA))
    pygame.quit()
