class Cal:
    def calculate(self,expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print("计算结果为:"+str(self.value))
class Talkcal(Cal,Talker):
    pass

tc = Talkcal()
tc.calculate('3+2*3')
tc.talk()
