import shelve

db = shelve.open('persondb')

print(len(db))

print(list(db.keys()))

bob = db['Bob Smith']

print(bob.lastName())