import pygame

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 400
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colisão Triângulo x Retângulo")

clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Triângulo (lista de 3 pontos)
triangulo = [(300, 100), (200, 300), (400, 300)]

# Retângulo
ret_w, ret_h = 50, 50
ret_x, ret_y = 50, 50
vel = 5
retangulo = pygame.Rect(ret_x, ret_y, ret_w, ret_h)

# Função para verificar se ponto está dentro do triângulo
def ponto_no_triangulo(p, a, b, c):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

    A = area(*a, *b, *c)
    A1 = area(*p, *b, *c)
    A2 = area(*a, *p, *c)
    A3 = area(*a, *b, *p)

    return A == A1 + A2 + A3

# Função para verificar colisão do retângulo com triângulo
def colidiu(tri, rect):
    # Testa os 4 cantos do retângulo
    cantos = [
        rect.topleft,
        rect.topright,
        rect.bottomleft,
        rect.bottomright
    ]
    for ponto in cantos:
        if ponto_no_triangulo(ponto, *tri):
            return True
    return False

# Loop principal
rodando = True
while rodando:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do retângulo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        retangulo.x -= vel
    if keys[pygame.K_RIGHT]:
        retangulo.x += vel
    if keys[pygame.K_UP]:
        retangulo.y -= vel
    if keys[pygame.K_DOWN]:
        retangulo.y += vel

    # Verifica colisão
    bateu = colidiu(triangulo, retangulo)

    # Desenho
    tela.fill(BRANCO)
    pygame.draw.polygon(tela, VERMELHO, triangulo)
    pygame.draw.rect(tela, AZUL if not bateu else VERDE, retangulo)

    pygame.display.flip()

pygame.quit()

