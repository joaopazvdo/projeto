import pygame
from utils.arquivo_cores import cores
from utils.classes import Jogador
from utils.classes import Tesouro
from utils.classes import Tela
from utils.classes import Retangulo
from utils.classes import Caixa_de_texto
from utils.funcoes_principais import cima_baixo_esquerda_direita
from utils.funcoes_principais import fim
from utils.funcoes_principais import pega_evento
from utils.funcoes_principais import passa_dialogo
from utils.funcoes_principais import passa_notificacao
from telas import tela_ganhou
from importacao import resource_path

def desenha_fase1(TELA, jogador, tesouros, pontuacao, 
                  PONTUACAO_MAXIMA, dialogo, detalhes, conquista):
    TELA.tela.fill(TELA.cor)

    for d in detalhes:
        d.visual_relativo('unico')
        d.texturiza_visual()
    
    jogador.visual_relativo('unico')
    jogador.texturiza_visual()
    
    for t in tesouros:
        if t.aparece:
            t.visual_relativo('unico')
            t.texturiza_visual()
    
    TELA.desenha_no_mapa('unico',detalhes +[jogador]+tesouros)
    TELA.tela.blit(TELA.mapas['unico'], 
                   (TELA.mapas_pos_x['unico'], TELA.mapas_pos_y['unico']))
    
    fonte_pontuacao = pygame.font.Font(None, 40)
    texto_pontuacao = fonte_pontuacao.render(f'Coordenas {pontuacao}/{PONTUACAO_MAXIMA}', 
                                             False, cores['preto'])
    pontuacao_pos_x = (TELA.LARGURA - texto_pontuacao.get_size()[0]) // 2
    TELA.tela.blit(texto_pontuacao, (pontuacao_pos_x, 5))

    if dialogo.aparece:
        pygame.draw.rect(TELA.tela, dialogo.cor, dialogo.retangulo)
        dialogo.renderiza_texto()
        dialogo.define_pos_texto(2,2,0,0)
        dialogo.mostra_texto()
        dialogo.mostra_texto_auxiliar()

    if conquista.aparece:
        pygame.draw.rect(TELA.tela, conquista.cor, conquista.retangulo)
        conquista.renderiza_texto()
        conquista.define_pos_texto(2,2,0,0)
        conquista.mostra_texto()
        conquista.mostra_texto_auxiliar()


def cria_cidade(TELA):
    cidade = [None] * 15 
    x_inicial = 2 
    y_inicial = 2 
    largura_casa = 9.2 
    altura_casa = 16.4
    for i in range(5):
        x = x_inicial 
        y = (i+1) * y_inicial + i * altura_casa 
        cidade[i] = Retangulo(x, y, largura_casa, altura_casa, TELA)
        cidade[i].define_textura(resource_path('textura/casa.png'))
    for i in range(5,10):
        x = 2 * x_inicial + largura_casa
        y = (i+1-5) * y_inicial + (i-5) * altura_casa 
        cidade[i] = Retangulo(x, y, largura_casa, altura_casa, TELA)
        cidade[i].define_textura(resource_path('textura/casa.png'))
    for i in range(10,15):
        x = 3 * x_inicial + 2 * largura_casa
        y = (i+1-10) * y_inicial + (i-10) * altura_casa 
        cidade[i] = Retangulo(x, y, largura_casa, altura_casa, TELA)
        cidade[i].define_textura(resource_path('textura/casa.png'))
    return cidade    


def mecanica(jogador, tesouros, conquista, pontuacao):
    keys = pygame.key.get_pressed()
    cima_baixo_esquerda_direita(keys, jogador)
    for tesouro in tesouros:
        if jogador.retangulo.colliderect(tesouro.retangulo):
            pontuacao += 1 if tesouro.aparece else 0
            conquista.aparece = True if tesouro.aparece else conquista.aparece
            tesouro.aparece = False
    return pontuacao


def fase1(TELA):
    TELA.cor = cores['mar']
    pygame.display.set_caption("Caça ao Tesouro (FASE 1)")

    TELA.cria_mundo('unico', 156,277)
    TELA.cria_camera('unico')
    TELA.cria_mapa('unico',1/10, 83.4, 2)

    jogador = Jogador(50, 50, 3, 6, TELA)
    jogador.cor = cores['preto']
    jogador.define_velocidade(0.5)
    jogador.define_textura_cima(resource_path('textura/cima.png'))
    jogador.define_textura_baixo(resource_path('textura/baixo.png'))
    jogador.define_textura_esquerda(resource_path('textura/esquerda.png'))
    jogador.define_textura_direita(resource_path('textura/direita.png'))
    jogador.textura = jogador.textura_baixo

    areia = Retangulo(0,0,120, 277, TELA)
    areia.cor = cores['areia']
    areia.define_textura(resource_path('textura/praia.png'))
    
    porto = Retangulo(95, 200, 61, 40, TELA)
    porto.define_textura(resource_path('textura/madeira.png'))

    cidade = cria_cidade(TELA)
    detalhes = [areia, porto] + cidade

    largura_tesouro = 4.6
    altura_tesouro = 8.2
    tesouros = [Tesouro(5.4, 14.2, largura_tesouro, altura_tesouro, TELA),
                Tesouro(30, 237, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 35, largura_tesouro, altura_tesouro, TELA),
                Tesouro(100, 210, largura_tesouro, altura_tesouro, TELA),
                Tesouro(44.4, 150, largura_tesouro, altura_tesouro, TELA)]
    for t in tesouros:
        t.cor = cores['vermelho']
        t.define_textura(resource_path('textura/tesouro.png'))

    dialogo = Caixa_de_texto(30,42.5,40,15, TELA)
    linhas_dialogo = [f'Veja, o mapa está no canto inferior direito,',
                    f'nele você pode ver onde estão localizados  nossos tesouros,', 
                    f'que são as coordenas,',
                    f'vou ficar te informando quantos já pegamos e quantas faltam.',
                    f'Quando pegar todas vá para o porto.']
    dialogo.define_linhas_de_texto(linhas_dialogo)
    dialogo.define_fonte(1.7)
    dialogo.cria_texto_auxiliar('APERTE ENTER', 1)
    dialogo.define_pos_texto_auxiliar(3,3, 1,4)

    conquista = Caixa_de_texto(30,42.5,40,15, TELA)
    linha_conquista = [f'Você conseguiu uma coordena']
    conquista.define_linhas_de_texto(linha_conquista)
    conquista.define_fonte(1.7)
    conquista.cria_texto_auxiliar('APERTE ESPAÇO', 1)
    conquista.define_pos_texto_auxiliar(3,3, 1,4)
    conquista.aparece = False

    clock = pygame.time.Clock()
    FPS = 60

    pontuacao = 0
    PONTUACAO_MAXIMA = 5
    while True:
        evento = pega_evento()
        jogador.retangulo.clamp_ip(areia.retangulo)
        TELA.cameras['unico'].center = jogador.retangulo.center
        TELA.cameras['unico'].clamp_ip(TELA.mundos['unico'])
        desenha_fase1(TELA, jogador, tesouros, pontuacao, 
                      PONTUACAO_MAXIMA, dialogo, detalhes, conquista)

        pontuacao = mecanica(jogador, tesouros, conquista, pontuacao)
        passa_dialogo(dialogo, evento)
        passa_notificacao(conquista, evento)

        ganhou = pontuacao >= PONTUACAO_MAXIMA and jogador.retangulo.colliderect(porto.retangulo)
        if ganhou: break
        if fim(evento): break

        pygame.display.flip()
        clock.tick(FPS)
    retorno = tela_ganhou(TELA) if ganhou else 'Tela inicial'
    return retorno, ganhou


if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    TELA = Tela(info.current_w, info.current_h)
    print(fase1(TELA))
    pygame.quit()
