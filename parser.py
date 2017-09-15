import lexer as lexr
from rply.token import BaseBox
from rply import ParserGenerator

#lexed = lex.parsetext("string = 10")
def getifint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Float(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


pg = ParserGenerator(
    ['number', 'floatnumber', 'variabledec',
     'setsym', 'variablenam','string'
    ]
)

@pg.production("main : expression")
def main(p):
    return p[0]


@pg.error
def error_handler(token):
    raise ValueError("Unexpected {0}, {1}".format(token.gettokentype(),token))





def parsetxt(text):
    parser = pg.build()
    parser.parse(lexr.l.lex(text))
