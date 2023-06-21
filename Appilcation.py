
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
        self.stock = dict()

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
        pass

    def update_inventory(self):
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

