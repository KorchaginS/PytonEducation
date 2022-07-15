
# Использование assert

class Super:
    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'

#x = Super()
#x.delegate()

# Использование исключения NotImplementedError


class Super:

    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError('action must be defined')

#x = Super()
#x.delegate()

# С подклассами

class Sub(Super): pass

#x = Sub()
#x.delegate()

# Работает

class Sub(Super):
    def action(self): print('spam')

x = Sub()
x.delegate()