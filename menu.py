from menu_item import *
from category import *

class Menu:
  def __init__(self, name):
    self.__name = name #(str)
    self.__categories = []

  def has_categories(self):
    """Returns True/False for if there are any categories in the menu"""
    return len(self.__categories) > 0

  def is_in_menu_item(self, menu_item):
    """Returns True/False for if the item is in the menu"""
    for category in self.__categories:
      return category.is_in_category(menu_item)

  def is_in_menu_category(self, category_name):
    """Returns True/False for if the category is in the menu"""
    result = None
    for category in self.__categories:
      if category.get_name() == category_name:
        result = True
      else:
        result = False
    return result

  def get_name(self):
    """Returns the name of the menu"""
    return self.__name

  def get_category_list_str(self):
    """Returns a list of the categories in the menu formatted as strings"""
    category_list = ''
    for category in self.__categories:
      category_list += str(category)
    return category_list

  def add_category(self, category):
    """Adds a category to the menu"""
    self.__categories.append(category)

  def remove_category(self, category_name):
    """Removes a category from the menu"""
    if self.is_in_menu_category(category_name):
      for category in self.__categories:
        if category.get_name() == category_name:
          self.__categories.remove(category)

  def __str__(self):
    """Formats the menu as a string"""
    if self.has_categories():
      return(self.__name + ': \n' + self.get_category_list_str())
    else:
      return(self.__name + ' has no items.')
