from menu_item import *

def main():
  apple = MenuItem('apple', 1.00, 'Fruit', 35)

  print(apple)

  print(apple.get_name())
  print(apple.get_price())
  print(apple.get_category())
  print(apple.get_calories())

  

main()
