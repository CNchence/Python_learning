class counterlist(list):
    def __init__(self,*args):
        super(counterlist,self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(counterlist,self).__getitem__(index)
c1 = counterlist(range(0,10))
c1.reverse()
del c1[3:6]
c1[1]+c1[2]
c1[5]
print(c1.counter)