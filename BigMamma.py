from Pizza import Pizza
from Menu import Menu

p1 = Pizza('Maegaritta', 40)
p2 = Pizza('Hawwai', 50)
p3 = Pizza('Peperoni', 50)

#print(p1.GetName())
#print(p1.GetPrice())

#print(p2.GetName())
#print(p2.GetPrice())

myMenu = Menu()
myMenu.AddPizza(p1)
myMenu.AddPizza(p2)
myMenu.AddPizza(p3)

myMenu.ShowMenu()

