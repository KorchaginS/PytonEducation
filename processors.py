class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())


Uppercase(open('trispam.txt'), HTMLize()).process()

# import pickle

# object = SomeClassO
# file = open(filename, 'wb')
# pickle.dump(object, file)
# Создать внешний файл
# Сохранить объект в файле
# import pickle
# file = open(filename, 'rb')
# object = pickle.load(file) # # Извлечь объект в более позднее время
#
#
# import shelve
# object = SomeClassO
# dbase = shelve.open(filename)
# dbase ['key'] = object # Сохранить под ключом
# import shelve
# dbase = shelve.open(filename)
# object = dbase[’key'] # Извлечь объект в более позднее время


from classesProjecting import PizzaShop

shop = PizzaShop()

import pickle

pickle.dump(shop, open('shopfile.pk1', 'wb'))

obj = pickle.load(open('shopfile.pk1', 'rb'))

print(obj.server, obj.chef)

obj.order('LSP')
