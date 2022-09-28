class Pizza():
    def __init__(self, name, price):
        self.Name = name
        self.Price = price

    def GetPrice(self):
        return self.Price    

    def GetName(self):
        return self.Name

    def __str__(self):
        return f'Pizza name: {self.Name} Price: {self.Price}'    
