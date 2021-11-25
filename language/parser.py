from language.lexer import *


class AST:
    pass



class Command(AST):
    def __init__(self, command_token, *arg_tokens):
        self.command_token = command_token
        self.arg_tokens = arg_tokens

    def __str__(self, level=0):
        leveled_tab = "\t" * level
        indent_leaf = "\n" + leveled_tab
        str = ""
        str += '{leveled_tab}{class_name}('.format(class_name=type(self).__name__,
                                                    token=self.command_token, leveled_tab=leveled_tab)
        str += "{indent_leaf}> {token}".format(token=self.command_token, indent_leaf=indent_leaf)
        for arg_token in self.arg_tokens:
            str += "{indent_leaf}> {token}".format(token=arg_token, indent_leaf=indent_leaf)
        str += "\n{leveled_tab})".format(leveled_tab=leveled_tab)
        return str

    def __repr__(self):
        return self.__str__()


class Parser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token() if self.lexer.has_next() else None

    def reset_parser(self):
        self.lexer.reset_lexer()
        self.current_token = self.lexer.next_token() if self.lexer.has_next() else None

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token() if self.lexer.has_next() else None
        else:
            raise Exception("Invalid token")

    def info_exp(self):
        # info-exp : INFO STRING
        token = self.current_token
        if token.type == INFO:
            self.eat(INFO)
            arg_token = self.current_token
            if arg_token.type == STRING:
                self.eat(STRING)
                return Command(token, arg_token)

    def expr(self):
        return self.info_exp()

    def parse(self):
        return self.expr()

if __name__ == '__main__':
    print(Parser(Lexer("info town")).parse())
