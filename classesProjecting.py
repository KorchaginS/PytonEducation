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


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self,name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self,name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'make pizza')



# pizzaShop

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self,server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bakes(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.server.work()
        self.oven.bakes()
        customer.pay(self.server)


if __name__ == '__main__':

   pizzaShop = PizzaShop()
   pizzaShop.order('Will')

