class Rec:
    def __init__(self):
        self.wid = 0
        self.hei = 0
    def setSize(self,size):
        self.wid = size
        self.hei = size
    def getSize(self):
        return self.wid,self.hei
    size = property(getSize,setSize)                     #注意 property里的函数不要加括号

r = Rec()
r.wid = 10
r.hei = 5
r.size = 12
print(r.size)