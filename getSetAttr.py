class Empty:
    def __getattr__(self, item):

        if item == 'age':
            return 40
        else:
            raise AttributeError(item)

# x = Empty()
# print(x.age)
# print(x.name)

class Acesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value + 10

        else:
            raise AttributeError(key + 'not allowed')

x = Acesscontrol()
x.age = 40
print(x.age)
#x.name = 'Bob'

# Эмуляция защиты атрибутов экземпляра


class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, key, value):

        if key in self.privates:
            raise PrivateExc(key, self)

        else:
            self.__dict__[key] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'
    y.name = 'Sue'
    print(x.name)

    y.age = 30
    # x.age = 20
    print(y.age)