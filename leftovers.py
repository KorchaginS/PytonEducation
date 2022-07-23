#Сравнения

class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()

print(X > 'ham')
print(X < 'ham')

#Булево

class Truth:
    def __bool__(self): return True

X = Truth()
if X: print('yes!')

class Truth:
    def __bool__(self): return False

X = Truth()
print(bool(X))

#Удаление

class Life:

    def __init__(self, name = 'unknown'):
        self.name = name
        print('Hello ' + name + '!')

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)

Brian = Life('Brian')

Brian.live()

Brian.__del__()

