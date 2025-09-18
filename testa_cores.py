import pygame

def roda(cor):
    pygame.init()

    TAMANHO_TELA = (200, 200)
    TELA = pygame.display.set_mode(TAMANHO_TELA)
    pygame.display.set_caption("Mostra Cores")

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        TELA.fill((cor[0], cor[1], cor[2]))
        pygame.display.flip()

    pygame.quit()


def main():
    while True:
        cor = input()
        if cor == 'fim': break
        cor = [int(e) for e in cor.split(',')]
        roda(cor)

main()
