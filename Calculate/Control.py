import View,Model

def InitData():
    a=View.InputData('A')
    b=View.InputData('B')
    Model.InitA(a)
    Model.InitB(b)

def PrintValues():
    a=Model.GetA()
    b=Model.GetB()
    View.OutputData(a)
    View.OutputData(b)

def PrintSum():
    result=Model.SumData()
    View.OutputData(result)