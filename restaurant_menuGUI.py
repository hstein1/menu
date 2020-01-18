import tkinter as tk
import tkinter.ttk as ttk
import menu_item
import category as cg
import menu

class MainGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.__restaurant = None

        self.frames = {}

        for F in [NameMenu, Menu, AddCategory, AddItem]:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nswe")

        if(self.__restaurant == None):
            self.show_frame(NameMenu)
        else:
            self.show_frame(Menu)

        

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def name_restaurant(self, name):
        self.__restaurant = menu.Menu(name)
        print("Restaurant has been named: ", name)
        print(self.__restaurant.get_name())

    def get_restaurant(self):
        return self.__restaurant

    def get_restaurant_name(self):
        return self.__restaurant.get_name()

    def add_category(self, categoryName):
        self.__restaurant.add_category(categoryName)
        print("%s has been added as a category", categoryName)
        print(self.__restaurant.get_categories())

    def add_item(self, category, item, calories, price):
        self.__restaurant.add_tem(category, item, price, calories)

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

class NameMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Name your restaurant")
        title.pack(pady=10, padx=10)

        entry_field = tk.Entry(self)
        entry_field.pack(pady=5, padx=5)

        submit = tk.Button(self, text="submit", command=lambda: controller.combine_funcs(controller.name_restaurant(entry_field.get()),
                                                              controller.show_frame(Menu)))
        submit.pack(pady=5)

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.menu_frame = tk.Frame(self) #Create menu frame
        self.meal_frame = tk.Frame(self) #Create meal frame
        
        self.__restaurant_name = 'Sample'
        if(controller.get_restaurant() != None):
            print("controller found a restaurant")
            self.__restaurant_name = controller.get_restaurant_name()
            restaurant_label = tk.Label(self.__menu_frame, text=self.__restaurant_name)
            restaurant_label.pack(side="top")
        else:
            print("No restaurant")

        add_category_button = tk.Button(self.menu_frame, text="Add Category",
                                     command=lambda: self.show_frame(AddCategory))
        add_category_button.pack(side="top")

        if (controller.get_restaurant() != None and controller.get_restaurant().has_categories()):
            add_item_button = tk.Button(self.menu_frame, text="Add Item",
                                         command=lambda: self.show_frame(AddItem))
            add_item_button.pack(side="top")

        entrees = cg.Category('entrees')
        
        restaurant_categories = [entrees]
        if(controller.get_restaurant() != None and controller.get_restaurant().has_categories()):
            restaurant_categories = controller.get_restaurant().get_categories()
        category_tree = ttk.Treeview(self.menu_frame)
        category_tree.pack()
        

        self.menu_frame.pack(side="left")
        self.meal_frame.pack(side="left")

    def refresh(self):
        self.category_tree.insert('', 'end', restaurant_categories[-1].get_name(),
                                      text=restaurant_categories[-1].get_name())
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class AddCategory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__frame = tk.Frame(self)

        self.__title = tk.Label(self.__frame, text="Add Category")
        self.__title.pack(side="top")

        self.__text_field = tk.Entry(self.__frame)
        self.__text_field.insert(0, 'Name the category')
        self.__text_field.pack(side="top")

        self.__add_button = tk.Button(self.__frame, text="Add Category", command=lambda: controller.combine_funcs(controller.add_category(self.__text_field.get()),
                                                                                                                  controller.refresh(controller), controller.show_frame(Menu)))
        self.__add_button.pack()

        self.__frame.pack()
       
class AddItem(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self)

        title = tk.Label(frame, text="Add Item")
        title.pack()

        category_selector_stringVar = tk.StringVar()
        categories = []
        if(controller.get_restaurant() != None and controller.get_restaurant().has_categories()):
            categories = controller.get_restaurant().get_categories_list_str()
        if(len(categories) > 0):
            category_selector_stringVar.set(categories[0])
        else:
            category_selector_stringVar.set("No categories")
        categories_popup = tk.OptionMenu(frame, "Categories", category_selector_stringVar, *categories)
        categories_popup.pack()

        name_text_field = tk.Entry(frame)
        name_text_field.insert(0, "Name your item")
        name_text_field.pack()

        calories_text_field = tk.Entry(frame)
        calories_text_field.insert(0, "How many calories does it have?")
        calories_text_field.pack()

        price_text_field = tk.Entry(frame)
        price_text_field.insert(0, "Price")
        price_text_field.pack()

        add_button = tk.Button(frame, text="Add Item", command=lambda: controller.combine_funcs(controller.add_item(category_selector_stringVar.get(),
                                                                                         name_text_field.get(),
                                                                                         calories_text_field.get(),
                                                                                         price_text_field.get()),
                                                                     controller.show_frame(Menu)))
        add_button.pack()

        frame.pack()

        

        
app = MainGUI()
app.mainloop()
