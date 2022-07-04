"""
Регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую.
"""
from classtools import AttrDisplay


class Person(AttrDisplay):

    """
    Обрабатывает и создает записи о людях

    """

    def __init__(self, name, job=None, pay=0):

        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1 + percent)

    #def __repr__(self):
        #return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):

    """
        Настроенная версия Person co специальными требованиями

    """

    def __init__(self, name, pay):
        self.person = Person(name, 'mrg', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    #def __getattr__(self, attr):
    #    return getattr(self.person, attr)

    #def __repr__(self):
    #    return str(self.person)

"""
class Department:

    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)
"""

if __name__ == '__main__':

    Bob = Person('Bob Smith')
    Sue = Person('Sue Jones', job='dev', pay=100000)
    print(Bob)
    print(Sue)
    print(Bob.lastName(), Sue.lastName())
    Sue.giveRaise(.10)
    print(Sue)
    Jimmy = Manager('Jimm Morrison', pay=10000)
    Jimmy.giveRaise(.10)
    print(Jimmy.lastName())
    print(Jimmy)
    #development = Department(Jimmy)
    #development.giveRaises(.10)
    #development.showAll()




