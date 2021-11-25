class GameStats():
    """[Armazena dados estatísticos da Invasão Alienígena]"""

    def __init__(self, ai_settings):
        """[Inicializa os dados estatísticos]"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0
        
        # Inicia a Invasão Allienígena em um estado inativo
        self.game_active = False
        

    def reset_stats(self):
        """[Inicializa os dados estatísticos que podem mudar durante o jogo]"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
