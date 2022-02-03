from PPlay.window import *
from PPlay.sprite import *

janela = Window(800, 600)
janela.set_title("Pong")

velocidadeY = -250
velocidadeX = 350

bola = Sprite("bolinha.png", 1)
bola.set_sequence_time(0, 1, 0, True)

while True:
    time = int(janela.time_elapsed() / 1000)

    bola.x += velocidadeX * janela.delta_time()
    bola.y += velocidadeY * janela.delta_time()

    if (bola.x > janela.width) or (bola.x < 0):
        bola.x = janela.width / 2
        bola.y = janela.height / 2
        velocidadeX *= -1
    if (bola.y >= janela.height - bola.height) or (bola.y < 0):
        velocidadeY *= -1

    bola.update()

    janela.set_background_color((0, 0, 0))
    bola.draw()
    janela.update()