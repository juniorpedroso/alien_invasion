class GameStats():
    """[Armazena dados estatísticos da Invasão Alienígena]"""

    def __init__(self, ai_settings):
        """[Inicializa os dados estatísticos]"""
        self.ai_settings = ai_settings
        # Inicia a Invasão Allienígena em um estado ativo
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """[Inicializa os dados estatísticos que podem mudar durante o jogo]"""
        self.ships_left = self.ai_settings.ship_limit
