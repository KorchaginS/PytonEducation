class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)

C = Callee()
C(1, 2, 3, x = 4, y = 5)

class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)

cb1 = Callback('blue')
cb2 = Callback('green')

#B1 = Button(command = cb1)
#B2 = Button(command = cb2)
