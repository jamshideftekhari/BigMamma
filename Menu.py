class Menu(): 
    def __init__(self):
        self.MenuKort=[]

    def AddPizza(self, pizza):
        self.MenuKort.append(pizza)    

    def ShowMenu(self):
        for p in self.MenuKort:
           # print(p.GetName())
           # print(p.GetPrice())
           print(p)
