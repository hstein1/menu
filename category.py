from menu_item import *

class Category:
  def __init__(self, name):
    self.__name = name #(str)
    self.__items = [] #(list of MenuItems)
    

  def has_items(self):
    """Returns True/False for if there are any items in the category"""
    return len(self.__items) > 0


  def is_in_category(self, menu_item):
    """Returns True/False for if menu_item is in the category"""
    result = None
    for item in self.__items:
      if item.get_name() == menu_item:
        result = True
      else:
        result = False
    return result

  def get_name(self):
    """Returns the name of the category"""
    return self.__name

  def get_items(self):
    """Returns a list of menu items in the category"""
    return self.__items

  
  def get_items_list_str(self):
    """Returns the list of menu items formatted as strings"""
    items_list = ''
    for item in self.__items:
      items_list += str(item) + '\n'
    return items_list

  def add_item(self, item):
    """Adds an item to the category"""
    self.__items.append(item)

  def remove_item(self, item_name):
    """Removes an item from the category"""
    if self.is_in_category(item_name):
      for item in self.__items:
        if item.get_name() == item_name:
          self.__items.remove(item)


  def __str__(self):
    """Formats the category as a string"""
    if self.has_items():
      return(self.__name + ': \n' + self.get_items_list_str())
    else:
      return(self.__name + ' has no items.')
    
