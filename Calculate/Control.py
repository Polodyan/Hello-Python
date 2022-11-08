import View,Model

def InitData():
    a=View.InputData('A')
    b=View.InputData('B')
    Model.set_first(a)
    Model.set_second(b)

def PrintValues():
    a=Model.get_first()
    b=Model.get_second()
    View.OutputData(a)
    View.OutputData(b)

#def PrintSum():
#    result=Model.SumData()
#    View.OutputResult(result)

#def InitOperaton():
#    operation=View.InputData('Введите оператор')

def solution():
    oper = View.InputOperation()
    Model.set_result(oper)
    result = Model.get_result()
    View.OutputResult(result)