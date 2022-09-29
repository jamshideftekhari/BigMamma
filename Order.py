class Order():
    def __init__(self):
        self.OrderList=[]
        self.TotalPrice

    def Add2Order(self, pizza):
        self.OrderList.append(pizza)    

    def CalculatePrice(self):
        for p in self.OrderList:
            self.TotalPrice = self.TotalPrice+p.Price 

