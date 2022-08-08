
class Set:
    def __init__(self,value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def len (self): return len(self.data) # len(self), если self истинно
    def __getitem__(self, key): return self.data[key] #self[i], self[i:j]
    def __and__(self, other): return self.intersect(other) # self & other
    def __or__(self, other): return self.union(other) # self I other
    def __repr__(self): return 'Set:' + repr(self.data) # print(self),.. .
    def __iter__(self) : return iter (self.data)


x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))
print(x | Set([1, 4, 6]))


