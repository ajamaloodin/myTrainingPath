import pygame
import random
import math
from pygame import mixer

# Inicializar pygame
pygame.init()

# Definir dimensiones de la pantalla del juego
pantalla = pygame.display.set_mode((800, 600))

# Título del juego en la pantalla
pygame.display.set_caption("Invasión Espacial")

# Icono
icono = pygame.image.load("ufo.png")
pygame.display.set_icon(icono)

#Imagen de fondo espacial
fondo = pygame.image.load("Fondo.jpg")

# musica de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load("cohete.png")

jugador_x = 368  # 400-32(la mitad de 64px) = 368
jugador_y = 500
jugador_x_cambio = 0

# Enemigo

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for ene in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(1.5)
    enemigo_y_cambio.append(50)

# Bala (disparo)
img_bala = pygame.image.load("bala.png")

bala_x = 0
bala_y = 500  # A la altura del jugador
bala_x_cambio = 0
bala_y_cambio = 5
bala_visible = False

# Explosion
img_explosion = pygame.image.load("explode.png")
explosion_x = 0
explosion_y = 500


puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font("freesansbold.ttf", 45)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (250,250))

# funcion para montrar el puntaje
def mostrar_puntaje (x, y):
    texto = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def jugador(x, y):

    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, e):

    pantalla.blit(img_enemigo[e], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))  # Se agrega 16 y 10 para que aparezca en el centro de la nave

# Funcion para detectar colisiones


def hay_colison(x_1, y_1, x_2, y_2):

    distancia = math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

    if distancia < 27:
        return True
    else:
        return False


se_ejecuta = True

# Loop del Juego
while se_ejecuta:

    # Color de fondo de la pantalla
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:  # Equivalente a Left
                jugador_x_cambio = -1.5
            if evento.key == pygame.K_d:  # Equivalente a right
                jugador_x_cambio = 1.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador_x_cambio = 0

# Posicionamiento del jugador
    jugador_x += jugador_x_cambio

    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

# Posicionamiento del enemigo
    for ene in range(cantidad_enemigos):

        # FIN DE JUEGO
        if enemigo_y[ene] > 474 and enemigo_x[ene] > jugador_x:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000   # efecto de hacer desaparecer a todas los enemigos
            texto_final()
            mixer.music.stop()
            break

        enemigo_x[ene] += enemigo_x_cambio[ene]

        if enemigo_x[ene] <= 0:
            enemigo_x_cambio[ene] = 1.5
            enemigo_y[ene] += enemigo_y_cambio[ene]
        elif enemigo_x[ene] >= 736:
            enemigo_x_cambio[ene] = -1.5
            enemigo_y[ene] += enemigo_y_cambio[ene]
        # Colison

        colision = hay_colison(enemigo_x[ene], enemigo_y[ene], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Big Explosion Cut Off.mp3")
            sonido_colision.play()
            pantalla.blit(img_explosion, (enemigo_x[ene], enemigo_y[ene]))
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[ene] = random.randint(0, 736)
            enemigo_y[ene] = random.randint(50, 200)

        enemigo(enemigo_x[ene], enemigo_y[ene], ene)

# Movimiento  de la bala
    if bala_y <= 64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)
    pygame.display.update()
