import View,Model

def start():
    a = View.InputData('A')
    Model.set_first(a)
    while True:
        oper = View.InputOperation()
        if oper == '=': break
        b = View.InputData('B')
        Model.set_second(b)
        Model.set_result(oper)
        result = Model.get_result()
        if result == None:
            View.division_by_zero()
            break
        first = Model.get_first()
        second = Model.get_second()
        View.OutputResult(first, second, oper, result)
        Model.set_first(result)
        

#def PrintValues():
#    a=Model.get_first()
#    b=Model.get_second()
#    View.OutputData(a)
#    View.OutputData(b)

#def PrintSum():
#    result=Model.SumData()
#    View.OutputResult(result)

#def InitOperaton():
#    operation=View.InputData('Введите оператор')

#def solution():
#    oper = View.InputOperation()
#    Model.set_result(oper)
#    result = Model.get_result()
#    View.OutputResult(result)