from scratch import Person
from scratch import Manager

Bob = Person('Bob Smith')
Sue = Person('Sue Jones', job='dev', pay=100000)
Jimmy = Manager('Jimm Morrison', pay=10000)

import shelve

db = shelve.open('persondb')

for obj in (Bob, Sue, Jimmy):

    db[obj.name] = obj

db.close()
