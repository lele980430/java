from  threading import Thread
import time
boxs = 0
class box(Thread):
    chuzi = ''
    count = 0
    gongzi = 0
    def run(self) -> None:
        global boxs
        while True:
            boxs = boxs + 1
            if boxs > 0 and boxs < 501 :
                self.count = self.count + 1
                print(self.chuzi,"做了一个蛋挞",'已经做了',boxs,'个')
            else:
                print(self.chuzi,'总共做了',self.count,'蛋挞！')
                time.sleep(3)
                self.gongzi = self.gongzi+(self.count*1.5)
                print(self.chuzi,'的工资为',self.gongzi)
                break
class guke(Thread):
    guke = ''
    koudai = 0
    qianbao = 30000
    boxs1 = boxs
    def run(self) -> None:
        while True:
            self.qianbao = self.qianbao - 3
            self.boxs1 = self.boxs1 - 1
            self.koudai = self.koudai + 1
            if self.qianbao == 0:
                print(self.guke,'已经没有钱了','购买了',self.koudai,'个')
                break
            elif self.boxs1 > 0 and self.boxs1 < 501:
                print(self.guke,'购买了',self.koudai,'个','剩余余额:',self.qianbao)
                continue





p1=box()
p2=box()
p3=box()

p1.chuzi ='贾强'
p2.chuzi ='贾强1'
p3.chuzi ='贾强2'

p1.start()
p2.start()
p3.start()

g1=guke()
g2=guke()
g3=guke()

g1.guke='顾客1'
g2.guke='顾客2'
g3.guke='顾客3'

g1.start()
g2.start()
g3.start()









