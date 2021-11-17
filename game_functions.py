import sys

import pygame


def check_events():
    """[Responde a eventos de pressionamento de teclas e mouse]
    """
    # Observa eventos de teclado e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    # Exibe a espaçonave
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
