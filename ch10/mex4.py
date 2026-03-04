# mex4.py
class Cvalue:
    def __init__(self):
        self.lista = []
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

def plus(a,b):
    c = a+b
    return c


print(__name__) # mex4에서 실행할 경우 __main__, 임폴트 할 경우 mex4
if __name__ == "__main__": # mex4를 직접 실행할 경우만 True -> import할 경우 실행 안됨
    p1 = Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()
