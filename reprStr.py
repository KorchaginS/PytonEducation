class adder:
    def __init__(self, data):
        self.data = data
    def __add__(self, other):
        self.data += other

class addRepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


# x = addRepr(2)
# x + 1
# print(x)

class addStr(adder):
    def __str__(self):
        return '[Value %s]' % self.data

# x = addStr(3)
# x + 1
# print(x)

# print(str(x), repr(x))

class addboth(adder):
    def __str__(self):
        return '[Value %s]' % self.data

    def __repr__(self):
        return 'addboth(%s)' % self.data

