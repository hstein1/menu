from tkinter import *
import menu_item
import category
import menu

class MenuGUI:
  def __init__(self):
    """Constructor method for the GUI"""
    self.__window = Tk() #Create main window

    self.__menu_frame = Frame(self.__window) #Create menu frame
    self.__meal_frame = Frame(self.__window) #Create meal frame

    

    self.__menu = menu.Menu("Megan and Hank's Restaurant") #Create Menu
    
    # Create Menu Label
    self.__menu_label = Label(self.__menu_frame, text=self.__menu.get_name()\
                              )
    self.__menu_label.config(font=("Helvetica", 20), bg="red")
    self.__menu_label.pack(side='top')
    
#----- Create Salads Category ------------------------------------------------
    self.__salads = category.Category(name="Salads")
    self.__green_salad = menu_item.MenuItem("Green Salad", 4.00, 15)
    self.__caesar_salad = menu_item.MenuItem("Caesar Salad", 5.00, 94)
    self.__greek_salad = menu_item.MenuItem("Greek Salad", 5.00, 179)

    self.__salads.add_item(self.__green_salad)
    self.__salads.add_item(self.__caesar_salad)
    self.__salads.add_item(self.__greek_salad)

#----- Create Soups Category --------------------------------------------------
    self.__soups = category.Category("Soups")
    self.__chicken_soup = menu_item.MenuItem("Chicken Soup", 3.50, 168)
    self.__vegetable_soup = menu_item.MenuItem("Vegetable Soup", 3.50, 159)
    self.__tomato_soup = menu_item.MenuItem("Tomato Soup", 3.50, 170)
    self.__butternut_squash_soup = menu_item.MenuItem("Butternut Squash Soup"\
                                                      , 3.75, 220)

    self.__soups.add_item(self.__chicken_soup)
    self.__soups.add_item(self.__vegetable_soup)
    self.__soups.add_item(self.__tomato_soup)
    self.__soups.add_item(self.__butternut_squash_soup)

#----- Create Entree Category ------------------------------------------------
    self.__entrees = category.Category("Entrees")
    self.__steak = menu_item.MenuItem("Steak (8 oz.)", 8.00, 614)
    self.__chicken = menu_item.MenuItem("Chicken", 6.00, 498)
    self.__salmon = menu_item.MenuItem("Salmon", 6.00, 468)
    self.__ravioli = menu_item.MenuItem("Spinach Ravioli", 7.50, 290)

    self.__entrees.add_item(self.__steak)
    self.__entrees.add_item(self.__chicken)
    self.__entrees.add_item(self.__salmon)
    self.__entrees.add_item(self.__ravioli)

#----- Create Dessert Category -----------------------------------------------
    self.__desserts = category.Category("Desserts")
    self.__chocolate_cake = menu_item.MenuItem("Chocolate Cake", 3.00, 424)
    self.__apple_pie = menu_item.MenuItem("Apple Pie", 3.00, 296)
    self.__fruit_salad = menu_item.MenuItem("Fruit Salad", 2.50, 97)

    self.__desserts.add_item(self.__chocolate_cake)
    self.__desserts.add_item(self.__apple_pie)
    self.__desserts.add_item(self.__fruit_salad)
    
                                                      
#----- Add Categories to Menu ------------------------------------------------
    self.__menu.add_category(self.__salads)
    self.__menu.add_category(self.__soups)
    self.__menu.add_category(self.__entrees)
    self.__menu.add_category(self.__desserts)

    
#----- Salad Category Display ------------------------------------------------
    self.__salads_label = Label(self.__menu_frame,\
                                text=self.__salads.get_name(),\
                                )
    self.__salads_label.config(font=("Arial Bold", 18), bg="light green")
    self.__salads_label.pack(side='top')

    self.__green_salad_label = Label(self.__menu_frame,\
                                     text=self.__green_salad.get_name(),\
                                     )
    self.__caesar_salad_label = Label(self.__menu_frame,\
                                     text=self.__caesar_salad.get_name(),\
                                     )
    self.__greek_salad_label = Label(self.__menu_frame,\
                                     text=self.__greek_salad.get_name(),\
                                     )

    self.__green_salad_label.pack(side='top')
    self.__caesar_salad_label.pack(side='top')
    self.__greek_salad_label.pack(side='top')

#----- Soup Category Display -------------------------------------------------
    self.__soups_label = Label(self.__menu_frame,\
                                text=self.__soups.get_name(),\
                                )
    self.__soups_label.config(font=("Arial Bold", 18), bg="light blue")
    self.__soups_label.pack(side='top')

    self.__chicken_soup_label = Label(self.__menu_frame,\
                                     text=self.__chicken_soup.get_name(),\
                                     )
    self.__vegetable_soup_label = Label(self.__menu_frame,\
                                     text=self.__vegetable_soup.get_name(),\
                                     )
    self.__tomato_soup_label = Label(self.__menu_frame,\
                                     text=self.__tomato_soup.get_name(),\
                                     )
    self.__butternut_squash_soup_label = Label(self.__menu_frame,\
                              text=self.__butternut_squash_soup.get_name(),\
                                     )

    self.__chicken_soup_label.pack(side='top')
    self.__vegetable_soup_label.pack(side='top')
    self.__tomato_soup_label.pack(side='top')
    self.__butternut_squash_soup_label.pack(side='top')

#----- Entree Category Display -----------------------------------------------
    self.__entrees_label = Label(self.__menu_frame,\
                                text=self.__entrees.get_name(),\
                                )
    self.__entrees_label.config(font=("Arial Bold", 18), bg="orange")
    self.__entrees_label.pack(side='top')

    self.__steak_label = Label(self.__menu_frame,\
                                     text=self.__steak.get_name(),\
                                     )
    self.__chicken_label = Label(self.__menu_frame,\
                                     text=self.__chicken.get_name(),\
                                     )
    self.__salmon_label = Label(self.__menu_frame,\
                                     text=self.__salmon.get_name(),\
                                     )
    self.__ravioli_label = Label(self.__menu_frame,\
                                     text=self.__ravioli.get_name(),\
                                     )

    self.__steak_label.pack(side='top')
    self.__chicken_label.pack(side='top')
    self.__salmon_label.pack(side='top')
    self.__ravioli_label.pack(side='top')

#----- Dessert Category Display ----------------------------------------------
    self.__desserts_label = Label(self.__menu_frame,\
                                text=self.__desserts.get_name(),\
                                )
    self.__desserts_label.config(font=("Arial Bold", 18), bg="pink")
    self.__desserts_label.pack(side='top')

    self.__chocolate_cake_label = Label(self.__menu_frame,\
                                     text=self.__chocolate_cake.get_name(),\
                                     )
    self.__apple_pie_label = Label(self.__menu_frame,\
                                     text=self.__apple_pie.get_name(),\
                                     )
    self.__fruit_salad_label = Label(self.__menu_frame,\
                                     text=self.__fruit_salad.get_name(),\
                                     )

    self.__chocolate_cake_label.pack(side='top')
    self.__apple_pie_label.pack(side='top')
    self.__fruit_salad_label.pack(side='top')

#----- Create Meal Interface -------------------------------------------------
    self.__meal_label = Label(self.__meal_frame, text="Your Meal")
    self.__meal_label.config(font = ("Helvetica", 20), bg='red')
    self.__meal_label.pack(side='top')

#----- Create Salads Pulldown Menu -------------------------------------------
    self.__salads_meal_label = Label(self.__meal_frame,\
                                text=self.__salads.get_name(),\
                                )
    self.__salads_meal_label.config(font=("Arial Bold", 18), bg="light green")
    self.__salads_meal_label.pack(side='top')

    
    self.__salads_stringVar = StringVar()
    self.__salads_list = self.__salads.get_items_list()
    self.__salads_stringVar.set(self.__salads_list[0])
    
    self.__salads_popup = OptionMenu(self.__meal_frame,\
                                     self.__salads_stringVar,\
                                     *self.__salads_list)
    self.__salads_popup.pack(side='top')

#----- Create Soups Pulldown Menu --------------------------------------------
    self.__soups_meal_label = Label(self.__meal_frame,\
                                text=self.__soups.get_name(),\
                                )
    self.__soups_meal_label.config(font=("Arial Bold", 18), bg="light blue")
    self.__soups_meal_label.pack(side='top')

    
    self.__soups_stringVar = StringVar()
    self.__soups_list = self.__soups.get_items_list()
    self.__soups_stringVar.set(self.__soups_list[0])
    self.__soups_popup = OptionMenu(self.__meal_frame,\
                                     self.__soups_stringVar,\
                                     *self.__soups_list)
    self.__soups_popup.pack(side='top')

#----- Create Entrees Pulldwon Menu ------------------------------------------
    self.__entrees_meal_label = Label(self.__meal_frame,\
                                text=self.__entrees.get_name(),\
                                )
    self.__entrees_meal_label.config(font=("Arial Bold", 18), bg="orange")
    self.__entrees_meal_label.pack(side='top')

    
    self.__entrees_stringVar = StringVar()
    self.__entrees_list = self.__entrees.get_items_list()
    self.__entrees_stringVar.set(self.__entrees_list[0])
    self.__entrees_popup = OptionMenu(self.__meal_frame,\
                                     self.__entrees_stringVar,\
                                     *self.__entrees_list)
    self.__entrees_popup.pack(side='top')

#----- Create Desserts Pulldown Menu -----------------------------------------
    self.__desserts_meal_label = Label(self.__meal_frame,\
                                text=self.__desserts.get_name(),\
                                )
    self.__desserts_meal_label.config(font=("Arial Bold", 18), bg="pink")
    self.__desserts_meal_label.pack(side='top')

    
    self.__desserts_stringVar = StringVar()
    self.__desserts_list = self.__desserts.get_items_list()
    self.__desserts_stringVar.set(self.__desserts_list[0])
    self.__desserts_popup = OptionMenu(self.__meal_frame,\
                                     self.__desserts_stringVar,\
                                     *self.__desserts_list)
    self.__desserts_popup.pack(side='top')

#----- Create Totals Labels --------------------------------------------------
    self.__total_price = StringVar()
    #self.__total_price.set(self.
    self.__total_price_label = Label(self.__meal_frame,\
                                     text=('Your total price is:'))
    self.__total_price_label.pack(side='top')

    self.__display_price = Label(self.__meal_frame,\
                                 textvariable = self.__total_price)
    self.__display_price.pack(side='top')
                                           
                                     

    self.__total_calories = StringVar()
    #self.__total_calories.set(
    self.__total_calories_label = Label(self.__meal_frame,\
                                        text=("Your meal's calorie count:"))
    self.__total_calories_label.pack(side='top')

    self.__calories_display = Label(self.__meal_frame,\
                                    textvariable = self.__total_calories)
    self.__calories_display.pack(side='top')


    # create buttons

    self.create = Button(self.__meal_frame, text="CREATE MEAL", \
                            command=self.create_meal)
    self.create.pack(side='top')

    self.__menu_frame.pack(side='left') #Pack menu frame
    self.__meal_frame.pack(side='left') #Pack meal frame



                                        



    mainloop()

  def salad_price(self):
    """Calculates the price of the salad"""
    salad_choice = self.__salads_stringVar.get()
    price_index = int(salad_choice.index('$'))
    salad_price = salad_choice[(price_index + 1) : (price_index + 4)]
    return float(salad_price)
    

  def soup_price(self):
    """Calculates the price of the soup"""
    soup_choice = self.__soups_stringVar.get()
    price_index = int(soup_choice.index('$'))
    soup_price = soup_choice[(price_index + 1):(price_index + 4)]
    return float(soup_price)

  def entree_price(self):
    """Calculates the price of the entree"""
    entree_choice = self.__entrees_stringVar.get()
    price_index = int(entree_choice.index('$'))
    entree_price = entree_choice[(price_index + 1):(price_index + 4)]
    return float(entree_price)

  def dessert_price(self):
    """Calculates the price of the dessert"""
    dessert_choice = self.__desserts_stringVar.get()
    price_index = int(dessert_choice.index('$'))
    dessert_price = dessert_choice[(price_index + 1):(price_index + 4)]
    return float(dessert_price)

  def salad_calories(self):
    """Calculates the calories in the salad"""
    salad_choice = self.__salads_stringVar.get()
    calories_index_start = int(salad_choice.index('has'))
    calories_index_end = int(salad_choice.index(' calories'))
    salad_calories = salad_choice[(calories_index_start + 4) :\
                                  calories_index_end]
    return int(salad_calories)

  def soup_calories(self):
    """Calculates the calories in the soup"""
    soup_choice = self.__soups_stringVar.get()
    calories_index_start = int(soup_choice.index('has'))
    calories_index_end = int(soup_choice.index(' calories'))
    soup_calories = soup_choice[(calories_index_start + 4) :\
                                  calories_index_end]
    return int(soup_calories)

  def entree_calories(self):
    """Calculates the calories in the entree"""
    entree_choice = self.__entrees_stringVar.get()
    calories_index_start = int(entree_choice.index('has'))
    calories_index_end = int(entree_choice.index(' calories'))
    entree_calories = entree_choice[(calories_index_start + 4) :\
                                  calories_index_end]
    return int(entree_calories)

  def dessert_calories(self):
    """Calculates the calories in the dessert"""
    dessert_choice = self.__desserts_stringVar.get()
    calories_index_start = int(dessert_choice.index('has'))
    calories_index_end = int(dessert_choice.index(' calories'))
    dessert_calories = dessert_choice[(calories_index_start + 4) :\
                                  calories_index_end]
    return int(dessert_calories)
                         

  def set_total_price(self):
    """Sets the price label to the total price of the meal"""
    price = self.salad_price() + self.soup_price() +\
            self.entree_price() + self.dessert_price()
    self.__total_price.set(price)

  def set_total_calories(self):
    """Sets the calories label to the total calories of the meal"""
    calories = self.salad_calories() + self.soup_calories() +\
               self.entree_calories() + self.dessert_calories()
    self.__total_calories.set(calories)

  def create_meal(self):
    """Sets the price and calories when CREATE MEAL button is pressed"""
    self.set_total_price()
    self.set_total_calories()
    print("New meal created.\nTotal Price: %.2f\nTotal calories: %d" %\
          (float(self.__total_price.get()), int(self.__total_calories.get())))

    

MenuGUI()
