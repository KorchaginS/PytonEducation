class Adder:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        return self.data + other

A = Adder(10)
#print(A + 20)
#print(20 + A) # Ошибка


class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        self.val += other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

    def __str__(self):
        return str(self.val)

# x = Commuter1(88)
# y = Commuter1(99)
# x + 1
# print(x)
# y = 1 + y
# print(y)
# z = y + x
# print(z)


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)


class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self+other

class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__
