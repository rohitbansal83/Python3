import random

class Player(object):
    def __init__(self,bankroll=0):
        self.bankroll = bankroll
        self.cards = []
        self.burststatus = 0
        self.betamount =0
        self.total = 0
        self.hasblackjack = 0
    def initiatenewgame(self):
        self.cards = []
        self.burststatus = 0
        self.betamount =0
        self.total = 0
        self.hasblackjack = 0
        
    def updatebankroll(self,amount):
        self.bankroll +=amount
    def bet(self):
        while (True):
            try:
                self.betamount = int(input("Enter the bet amount:"))
                
            except:
                print("not a valid number")
                continue
            else:
                if self.betamount<=self.bankroll:
                    self.bankroll -=self.betamount
                    break
                else:
                    print("you dont have enough money in bankroll. The money in your bankroll is: "+str(self.bankroll))
                    continue
    def hit(self, d): 
        while True:
            y=0
            for x in d.cardpack:
                y+=d.cardpack[x]
            if y==312:                
                d.resetcardpack()
            p = random.randint(1,13)
            if p in d.cardpack:
                if d.cardpack[p]<24:
                    d.cardpack[p]+=1
                    break
                else:
                    continue
            else:
                d.cardpack[p] = 1
                break
        self.cards.append(p)
        print("Your cards:")
        for i in self.cards:
            print(Dealer.standardcardpack[i])
    
    def checkburst(self):
        self.playertotal()           
        if self.total>21:
            print("You have been Bursted!")
            self.burststatus = 1
        
    def stand(self):
        pass
    def playermove(self, d):
        if self.hasblackjack ==1:
            d.dealermove(self)
            return
        while True:
            x = input("do you want to Hit or Stand? H/S").upper()
            if x=='H':
                self.hit(d)
                self.checkburst()
                if self.burststatus == 0:
                    continue
                else:
                    break
            elif x=='S':
                self.stand()
                break
            else:
                print("Wrong Input")
        if self.burststatus == 1:
            print("You Lost!")           
        else:
            d.dealermove(self)
    def tie(self):
        self.updatebankroll(self.betamount)
    def won(self):
        self.updatebankroll(self.betamount*2)
    def playertotal(self):
        self.total=0
        for i in self.cards:
            if (i>10):
                self.total+=10
            else:
                self.total+=i
            if i==1 and self.total<=11:
                self.total+=10

    
class Dealer(object):
    standardcardpack = {1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
    
    def __init__(self):
        self.cards = []
        self.burststatus = 0
        self.cardpack = {0:0}
        self.total = 0
        self.hasace = 0
        
    def initiatenewgame(self):
        self.cards = []
        self.burststatus = 0
        self.total = 0
        self.hasace = 0
        
    def resetcardpack(self):
        self.cardpack = {0:0}
    
    def deal(self, p):        
        while True:
            y=0
            for x in self.cardpack:
                y+=self.cardpack[x]
            if y==312:                
                resetcardpack()
            p1 = random.randint(1,13)
            if p1 in self.cardpack:
                if self.cardpack[p1]<24:
                    self.cardpack[p1]+=1
                    break
                else:
                    continue
            else:
                self.cardpack[p1] = 1
                break
        while True:
            y=0
            for x in self.cardpack:
                y+=self.cardpack[x]
            if y==312:                
                resetcardpack()
            p2 = random.randint(1,13)
            if p2 in self.cardpack:
                if self.cardpack[p2]<24:
                    self.cardpack[p2]+=1
                    break
                else:
                    continue
            else:
                self.cardpack[p2] = 1 
                break
        while True:
            y=0
            for x in self.cardpack:
                y+=self.cardpack[x]
            if y==312:                
                resetcardpack()
            d = random.randint(1,13)
            if d in self.cardpack:
                if self.cardpack[d]<24:
                    self.cardpack[d]+=1
                    break
                else:
                    continue
            else:
                self.cardpack[d] = 1 
                break
        p.cards = [p1,p2]
        self.cards.append(d)
        p.playertotal()
        total = p.total
        if total ==21:
            p.hasblackjeck = 1
        print("Dealer card:")
        print(Dealer.standardcardpack[d])
        print("Your cards:")
        print(Dealer.standardcardpack[p1])
        print(Dealer.standardcardpack[p2])
        
        
        
    def dealertotal(self):
        self.total = 0
        for i in self.cards:
            if (i>10):
                self.total+=10
            else:
                self.total+=i
            if i==1 and self.total<=11:
                self.total+=10
                self.hasace = 1
                
    def hit(self): 
        while True:
            y=0
            for x in self.cardpack:
                y+=self.cardpack[x]
            if y==312:                
                resetcardpack()
            p = random.randint(1,13)
            if p in self.cardpack:
                if self.cardpack[p]<24:
                    self.cardpack[p]+=1
                    break
                else:
                    continue
            else:
                self.cardpack[p] = 1
                break
        self.cards.append(p)
        print("Dealer cards:")
        for i in self.cards:
            print(Dealer.standardcardpack[i])
            
    def checkburst(self):
        self.dealertotal()           
        if self.total>21:
            print("Dealer have been Bursted!")
            self.burststatus = 1
        
    def stand(self):
        pass
    def dealermove(self, p):
        p.playertotal()
        ptotal = p.total
        self.hit()
        self.dealertotal()
        dtotal = self.total
        if p.hasblackjack == 1:
            if dtotal ==21:
                print("Its a Tie:")
                p.tie()
            else:
                print("You Won!")
                p.won()
            print("Dealer cards:")
            for i in self.cards:
                print(Dealer.standardcardpack[i])
            print("Your cards:")
            for i in p.cards:
                print(Dealer.standardcardpack[i])
            return
        
        while  (dtotal<ptotal or dtotal<17):
            print("Dealer have chosen to hit")
            self.hit()
            self.dealertotal()
            dtotal = self.total
            
        self.checkburst()
        if self.burststatus==1:
            print("You won!")
            p.won()
        else:            
            if dtotal>ptotal :
                print("You lost!")
            elif (dtotal == ptotal ):
                print("It's a Tie!")
                p.tie()
            else:
                print("You won!")
                p.won()
        print("Dealer cards:")
        for i in self.cards:
            print(Dealer.standardcardpack[i])
        print("Your cards:")
        for i in p.cards:
            print(Dealer.standardcardpack[i])
            
def playgame():
    sam = Dealer()
    rohit = Player()
    while True:
        
        try:
            amount = int(input("how much money you want to play with:"))
                
        except:
            print("not a valid number")
            continue
        else:
            rohit.bankroll = amount 
            break
            
    while True:       
            rohit.initiatenewgame()
            sam.initiatenewgame()
            rohit.bet()
            sam.deal(rohit)
            rohit.playermove(sam)
            playmore = input( "Do you want to play more?Y/N: ").upper()
            if playmore =='N':
                print("your balance amount is:" + str(rohit.bankroll))
                break
            
                
playgame()       
