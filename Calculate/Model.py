import Control


def CalcData():
    pass


a=0
b=0
charO=''

# listOperator=['*' , '/' , '-']
listOperator={'*':'MultiData' , '/':'DivisionData', '-':'SubData' , '+':'SumData'}

def InitA(number:int):
    global a
    a = number

def InitB(number:int):
    global b
    b = number

def InitCharO(charOp: str):
    global charO
    charO = charOp

def GetA():
        global a
        return a
    
def GetB():
        global b
        return b

def SumData():
    global a
    global b
    return a + b

def MultiData():
    global a
    global b
    return a*b

def SubData():
    global a
    global b
    return a - b

def DivisionData():
    global a
    global b
    return int(a/b)

def OperatorChoice():
    global a
    global b
    global charO
    