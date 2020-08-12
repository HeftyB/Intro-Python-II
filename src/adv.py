from room import Room
from items import Item
from player import Player
import random


item1 = Item("Basic Sword", "A sword anyone can use!", "+1_attack"),
item2 = Item("Leather Armor", "Armor against light attacks", "+1_defense"),
item3 = Item("Wizard Staff", "Yer a wizard Harry!", "+1_attack +1_defense"),
item3 = Item("Health Potion", "Healing nectar", "restores health"),
item4 = Item("Knights Sword", "A sword for a more skilled user", "+2_attack"),
item5 = Item("Shield", "To block stuff", "+2_defense"),
items_list = [item1, item2, item3, item4, item5]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items_list[random.randint(0,4)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items_list[random.randint(0,4)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items_list[random.randint(0,4)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items_list[random.randint(0,4)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items_list[random.randint(0,4)]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Playe 1", room["outside"])

is_playing = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while is_playing:
    print(player1.location.name)
    print(player1.location.description)

    user_input = input(">>>ENTER A SINGLE COMMAND>>> ")

    if user_input == "q":
        break
    elif user_input == "n":
        if hasattr(player1.location, "n_to"):
            player1.location = player1.location.n_to
        else:
            print("No available path that way")
    elif user_input == "e":
        if hasattr(player1.location, "e_to"):
            player1.location = player1.location.e_to
        else:
           print("No available path that way")
    elif user_input == "s":
        if hasattr(player1.location, "s_to"):
            player1.location = player1.location.s_to
        else:
            print("No available path that way")
    elif user_input == "w":
        if hasattr(player1.locationn, "w_to"):
            player1.location = player1.location.w_to
        else:
            print("No available path that way")
    else:
        print("invalid input, try again....")


