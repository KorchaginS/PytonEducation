class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)


class Methods(object):

    def imeth(self, x):
        print(self, x)

    @staticmethod
    def smeth(x):
        print([x])

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__

# a = Spam()
# b = Spam()
# c = Spam()
#
# Spam.printNumInstances()
# c.printNumInstances()

# obj = Methods()
# obj.imeth(1)
# obj.smeth(2)
# obj.cmeth(3)
# print(obj.name)

class Tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):

       self.calls += 1
       print('call %s to %s' % (self.calls, self.func.__name__))
       return self.func(*args)

@Tracer
def spam(a,b,c):
    return a + b + c

# print(spam(1,2,3))
# print(spam('a', 'b', 'c'))


def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)

    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a, b, c): return a + b + c

x = C()
print(x.spam(1,2,3))
print(x.spam('a', 'b', 'c'))
