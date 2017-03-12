def checkIndex(key):
    if not isinstance(key,int) : raise TypeError("索引类型必须为整型")
    if key<0 : raise IndexError("输入索引不能为负")

class ziran:
    def __init__(self,start = 0,step =1):
        self.start = start
        self.step = step
        self.change = {}
    def __getitem__(self, key):
        checkIndex(key)
        try: return(self.change[key])
        except KeyError:
            return self.start + self.step*key
    def __setitem__(self, key, value):
        checkIndex(key)
        self.change[key] = value

a= ziran(1,2)
print(a.change)
a[4] = 5
a[1.2]=7
print(a[4])