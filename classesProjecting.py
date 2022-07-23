class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary *= 1 + percent

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return 'Employee: name = %s, salary = %s' % (self.name, self.salary)


class Chief(Employee):
    def __init__(self, name):
        Employee.__init__(self,name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self,name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Chief):
    def __init__(self, name):
        Chief.__init__(self, name)

    def work(self):
        print(self.name, 'make pizza')

if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob); print()

    for klass in (Employee, Chief, Server, PizzaRobot):
        obj = klass(klass.__name__)
        obj.work()