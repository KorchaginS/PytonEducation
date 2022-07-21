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
        return self.val

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

#Распространение типа класса на результат

class Commuter5:

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):

            other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val

# x = Commuter5(88)
# y = Commuter5(99)
# print(x + 10)
# print(10 + y)
#
# z = x + y
#
# print(z)
# print(z + 10)
# print(z + z)
# print(z + z + 1)

# if __name__ == '__main__':
#     for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
#         print('-' * 60)
#         x = klass(88)
#         y = klass(99)
#         print(x + 1)
#         print(1 + y)
#         print(x + y)


# Изменение на месте

class Number:

    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self

    def __str__(self):
        return str(self.val)

x = Number(5)
x+=1
x+=1
print(x)









