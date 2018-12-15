from category import *
from menu_item import *
from menu import *

def main():
  appetizers = MenuCategory('Appetizers')
  apple = MenuItem('apple', 1.25, 35)
  appetizers.add_item(apple)
  banana = MenuItem('banana', 1.05, 30)
  appetizers.add_item(banana)
  
  entrees = MenuCategory('Entrees')
  steak = MenuItem('steak', 40.55, 200)
  entrees.add_item(steak)
  chicken = MenuItem('chicken', 20.56, 150)
  entrees.add_item(chicken)

  fruit_store = Menu('Fruit Store')
  fruit_store.add_category(appetizers)
  fruit_store.add_category(entrees)
  print(fruit_store)
  

main()
  
