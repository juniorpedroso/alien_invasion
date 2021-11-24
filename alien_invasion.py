import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)

    # Carrega a imagem de um fundo de tela
    #background = pygame.image.load('images/City Night.png')

    # Inicia o laço principal do jogo
    while True:
        # Verifica se há entradas do jogador
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            # Atualiza a posição da espaçonave
            ship.update()
            # Atualiza os projéteis
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # Atualiza os aliens
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Desenha uma nova tela
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)


run_game()
