from category import *
from menu_item import *

def main():
  appetizers = MenuCategory('Appetizers')

  print(appetizers)
  apple = MenuItem('apple', 1.25, 35)
  appetizers.add_item(apple)
  print(appetizers)
  banana = MenuItem('banana', 1.05, 30)
  appetizers.add_item(banana)
  print(appetizers)

main()
