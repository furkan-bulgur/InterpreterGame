class GameController:
    def __init__(self, game):
        self._game = game

    def print_info(self, obj_name):
        log = self._game.get_object(obj_name).info()
        self._game.update_game_screen(log)