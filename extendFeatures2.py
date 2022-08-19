# class Spam:
#     numInstances = 0
#
#     def __init__(self):
#         Spam.numInstances += 1
#
#     def printNumInstances():
#         print("Number of instances: %s" % Spam.numInstances)
#
#     printNumInstances = staticmethod(printNumInstances)


class Spam2:
    numInstances = 0

    def __init__(self):
        Spam2.numInstances += 1

    def printNumInstances(cls):
        print("Number of instances: %s" % cls.numInstances)

    printNumInstances = classmethod(printNumInstances)

class Sub(Spam2):
    def printNumInstances(cls):
        print('Extra stuff...', cls)
        Spam2.printNumInstances()

    printNumInstances = classmethod(printNumInstances)

class Other(Spam2): pass

x = Sub()
y = Spam2()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()
z = Other()
z.printNumInstances()