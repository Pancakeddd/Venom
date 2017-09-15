import re
from rply import LexerGenerator

token_knownfunctions = []

def create_tokenfunction(name,arguments):
    token_knownfunctions.append([name,arguments])

create_tokenfunction("print",1)
create_tokenfunction("foobar",0)


lg = LexerGenerator()


lg.add('number', r'\-?[0-9]+')
lg.add('floatnumber', r'[0-9]+\.[0-9]+')
lg.add('mathsym', r'\+|\-|\/|\*')
lg.add('variabledec', r'int|string|long')
lg.add('setsym', r'\=')
lg.add('variablenam', r'[A-Za-z]+')
lg.add('string', r'"[A-Za-z]+"')
lg.ignore(r'\s+')

l = lg.build()




#def evaluate_text(text):
    #if()

def getpbrackets(text):
    return re.findall(r'\(([^()]+)\)', text)

def parsetext(text):
    tokenreturn = []
    for token in l.lex(text):
        tokenreturn.append(token)
    return tokenreturn
