INFO, STRING, INTEGER, ILLEGAL, EOF = "info", "string", "integer", "illegal", "eof"

class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self,level=0):
        leveled_tab = "\t" * level
        return '{leveled_tab}Token({type}, {value})'.format(
            type=self.type.upper(),
            value=repr(self.value),
            leveled_tab=leveled_tab
        )

    def __repr__(self):
        return self.__str__()

