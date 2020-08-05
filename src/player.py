# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.health = 100
        # self.inventory = []
    
    # @property
    # def add_inventory_item(item):
    #     self.inventory.append(item)
    
    # @property
    # def get_inventory:
    #     return self.inventory