
class StoreManager:
    def __init__(self):
        pass


class Item:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def get_attribute(self, attr_name):
        match attr_name.upper():
            case 'NAME':
                return self.name
            case 'PRICE':
                return self.price
            case 'DESCRIPTION':
                return self.description


class Inventory:
    def __init__(self):
        self.inventory = dict()

    def add_item(self, item):
        # add item name and item class to dictionary
        pass

    def get_item(self, item):
        # search dictionary for item name and return item if it exists
        pass


class Warehouse:
    def __init__(self):
        self.stock = dict()

    def add_inventory(self):
        """ Add an inventory to the warehouse's stock. """
        pass

    def update_inventory(self):
        """ Add or remove an item from one of the warehouse's inventories. """
        pass

    def get_inventory(self):
        """ Get an inventory from the warehouse's stock. """
        pass


class User:
    def __init__(self, name, password, initial_balance):
        self.name = name
        self.password = password
        self.balance = initial_balance

    def update_password(self):
        pass

    def check_password(self):
        pass

    def update_balance(self):
        pass


class UserActions:
    def __init__(self):
        pass

    def buy_item(self):
        pass

    def return_item(self):
        pass

    def change_password(self):
        pass


class UserInventory(Inventory):
    def __init__(self):
        Inventory.__init__(self)

    def view_purchased_items(self):
        pass


class ShoppingCart:
    def __init__(self):
        pass

    def view_shopping_cart(self):
        pass

    def update_shopping_cart(self):
        pass
