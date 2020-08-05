# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, room_items):
        self.name = name
        self.description = description
        self.room_items = room_items
    


    @property
    def get_room_items(self):
        return self.room_items

    # @property
    # def get_room_mob(self):
        # return self.room_mob
    