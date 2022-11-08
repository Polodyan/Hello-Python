def CalcData():
    pass

a=0
b=0

def InitA(number:int):
    global a
    a=number

def InitB(number:int):
    global b
    b=number

    def GetA():
        global a
        return a
    
    def GetB():
        global b
        return b