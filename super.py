class C:
    def act(self):
        print('spam')

class D(C):
    def act(self):
        super().act()
        print('eggs')

# a = C()
# b = D()
# a.act()
# b.act()

class X: pass
class Y: pass

X.a = 1
X.b = 2
X.c = 3

Y.a = X.a + X.b + X.c

for X.i in range(Y.a) : print(X.i)

print(X.__dict__)