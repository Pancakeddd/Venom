class Function():
    def __init__(self, name,arguments,pythoncode):
        self.name = name
        self.args = arguments
        self.pyc = pythoncode
class DynamicFunction():
    def __init__(self, tokens,pythoncode):
        self.tokens = token
        self.pyc = pythoncode


functions = {}
dynfunctions = []

def createfunction(func):
    functions[func.name] = func
def createdynamicfunction(func):
    dynfunctions.append(func)

createfunction(Function("println",1,"print({0})"))
createfunction(Function("create",3,"def {0}({1}):\n{2}"))
