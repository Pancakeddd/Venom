import variable
import parser
pg = parser.pg
@pg.production('expression : variablenam setsym number')
@pg.production('expression : variablenam setsym string')
@pg.production('expression : variablenam setsym variablenam')
def expression_createnewvar(p):
    print(p[2].gettokentype())
    if(p[2].gettokentype() == "number"):
        print("yes")
    elif(p[2].gettokentype() == "string"):
        print("str {0}".format(p[2].getstr()))
