import importlib
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

# sobject = Sum(2)
# pobject = Product(3)
# actions = [square, sobject, pobject.method, Negate]
#
# for act in actions:
#     print(act(5))

# ПОДМЕШИВАЕМЫЕ КЛАССЫ


class ListInstance:

    def __attrnames(self):
        return ''.join('\t % s = % s\n' % (attr, self.__dict__[attr])
            for attr in sorted(self.__dict__))

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>'%(self.__class__.__name__, id(self), self.__attrnames())


class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'


class ListInherited():

    def __attrnames(self, indent = ' '*4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)

        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of %s, adress %s: \n %s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )


def tester(listerclass, sept=False):

    class Super:
        def __init__ (self):
            self.data1 = 'spam'

        def ham(self):
            pass


    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__ (self)
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


def testByNames(modename, classname, sept=False):
    modobject = importlib.import_module('classesProjecting2')

    listerclass = getattr(modobject, classname)

    tester(listerclass, sept)

if __name__ == '__main__':
     # testByNames('listinstance', 'ListInstance', True)
    # testByNames('listinherited', 'Listlnherited', True)
    # testByNames('listtree', 'ListTree', False)
    tester(ListInherited)






