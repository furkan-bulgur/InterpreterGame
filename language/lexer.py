from language.token import *

class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.buffered_token = None
        self.eof_flag = True

    def reset_lexer(self):
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.buffered_token = None
        self.eof_flag = True

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return result

    def string(self):
        result = ""
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result

    def commands(self, str):
        if str == INFO:
            return Token(INFO,str)
        else:
            return Token(STRING, str)


    def next_token(self):
        if self.buffered_token is not None:
            token = self.buffered_token
            self.buffered_token = None
            return token

        while self.current_char is not None:
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char.isalpha():
                return self.commands(self.string())
            elif self.current_char.isspace():
                self.skip_whitespace()
            else:
                return Token(ILLEGAL, None)

        return Token(EOF, None)


    def has_next(self):
        self.buffered_token = self.next_token()
        if self.buffered_token.type == EOF and not self.eof_flag:
            return False
        elif self.buffered_token.type == EOF and self.eof_flag:
            self.eof_flag = False
            return True
        else:
            return True

    def token_list(self):
        token_list = []
        while self.has_next():
            token_list.append(self.next_token())
        self.reset_lexer()
        return token_list

if __name__ == '__main__':
    print(Lexer("info town").token_list())