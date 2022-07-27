class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)


class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)

class C3(C1, C2): pass

# I = C3()
#
# I.meth1(); I.metha()
# print(I.__dict__)
# I.meth2(), I.methb()

def square (arg) :
    return arg ** 2

class Sum:
    def __init__ (self, val) :
        self.val = val

    def __call__ (self, arg) :
        return self.val + arg


class Product:
    def __init__ (self, val) :
        self.val = val
    def method (self, arg) :
        return self.val * arg

class Negate:
    def __init__(self, val):
        self.val= - val

    def __repr__(self):
        return str(self.val)

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method, Negate]

for act in actions:
    print(act(5))






