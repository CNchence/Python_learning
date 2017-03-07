class MuffleCal:
    muffle = False
    def calculate(self,jisuan):
        try:
            return eval(jisuan)
        except:
            if self.muffle:
                return("输入错误")
            else :
                raise

        '''
       except ZeroDivisionError:
            if self.muffle:
                return ("除法时，分母不能为0")
            else:
                raise
        except (NameError,TypeError,SyntaxError):
            if self.muffle:
                return("输入错误")
            else:
                raise
                '''

while True:
    cai = MuffleCal()
    cai.muffle = True
    car = input("请输入计算公式：")
    print(cai.calculate(car))