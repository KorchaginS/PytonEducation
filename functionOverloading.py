class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

x = Number(5)
Y = x-2
# print(Y.data)

class Indexer:

    def __getitem__(self, index):
        return index ** 2

x = Indexer()
# print(x[2])

# for i in range(5):
#     print(x[i])

class Indexer:

    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
            return self.data[index]
        else:
            print('slicing', index.start, index.stop, index.step)

x = Indexer()

# print(x[0])
# print(x[3])
# print(x[-1])
# print(x[2:4])

class StepperIndex:

    def __getitem__(self, i):
        return self.data[i]

x = StepperIndex()
x.data = 'spam'

print(x[2])

for item in x:
    print(item)