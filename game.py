from logic.controllers import GameController
from logic.village import Town
from language.lexer import *
from language.parser import *
from language.evaluator import *


class Game:

    def __init__(self):
        self.objects =[]
        self.town = Town("Hulalu")
        self.objects.append(self.town)
        self.game_controller = GameController(self)

    def get_object(self, object_name):
        for obj in self.objects:
            if obj.object_name == object_name.lower():
                return obj
        return None

    def print_game_state(self):
        print(self.town.info())

    def update_game_screen(self, log):
        self.print_game_state()
        print(log)

    def start_game(self):
        self.print_game_state()

    def run_command(self,text):
        Interpreter(Parser(Lexer(text)), self.game_controller).interpret()
