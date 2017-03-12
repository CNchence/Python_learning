class bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("饿了就要吃")
            self.hungry = False
        else:
            print("吃饱了")

class songbird(bird):
    def __init__(self):
        super(songbird,self).__init__()
        self.sound = "lalalala"
    def sing(self):
        print(self.sound)

song = songbird()
song.sing()
song.eat()
