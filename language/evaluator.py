from token import *

from language.token import *


class NodeEvaluator:
    def eval(self, node):
        method_name = 'eval_' + type(node).__name__
        evaluator = getattr(self, method_name, self.generic_eval)
        return evaluator(node)

    def generic_eval(self, node):
        raise Exception('No evaluate_{} method'.format(type(node).__name__))


class Interpreter(NodeEvaluator):
    def __init__(self, parser, game_controller):
        self.parser = parser
        self.game_controller = game_controller

    def eval_Command(self, node):
        if node.command_token.type == INFO:
            self.game_controller.print_info(node.arg_tokens[0].value)

    def interpret(self):
        tree = self.parser.parse()
        self.eval(tree)
