class MenuItem:
  def __init__(self, name, price, calories = None):
    self.__name = name #(str)
    self.__price = price #(float)
    self.__calories = calories #(int)

  def has_nutritional_facts(self):
    """Returns True/False for if the item has a calory count"""
    return bool(self.__calories)

  def get_name(self):
    """Returns the name of the item"""
    return self.__name

  def get_price(self):
    """Returns the price of the item"""
    return self.__price

  def get_calories(self):
    """Returns the calories of the item"""
    if self.has_nutritional_facts():
      return self.__calories

  def update_price(self, price):
    """Updates the price of the item"""
    self.__price = price

  def update_calories(self, calories):
    """Updates the calories of the item"""
    self.__calories = calories

  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__price < other.__price

  def __gt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__price == other.__price

  def __eq__(self, other):
    return self is other or \
          (type(self) == type(other) and self.__title == other.__title)

  def __str__(self):
    if self.has_nutritional_facts():
      return(self.__name + ' costs $%.2f and has %d calories'\
             %(self.__price, self.__calories))
    else:
      return(self.__name + ' costs $%.2f' + self.__price)








  
