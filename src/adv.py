from room import Room
from player import Player
from item import Item

# Declare all the rooms

outside_items = [Item('sword', 'A holy relic'),
                 Item('torch', 'A simple torch')]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", outside_items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player = Player('Hero', room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.s

exit_game = False
print(f'Welcome, {player.name}! Enjoy your adventure.\n')

while not exit_game:

    print(player.current_room.__str__())
    user_input = input("Enter direction (N, S, E, W). Q to quit: ")
    user_input = user_input.lower().strip()

    if user_input == '':
        continue

    if user_input == 'q':
        exit_game = True

    # get first word and check 2nd word
    if len(user_input.split(' ')) == 2:
        verb = user_input.split(' ')[0]
        obj = user_input.split(' ')[1]
    else:
        verb = False
        obj = False

    if verb and obj:
        if verb == 'get':
            for item in player.current_room.items:
                if obj == item.name:
                    player.get_item(item)

    elif user_input == 'i' or user_input == 'inventory':
        player.check_inventory()

    elif user_input == 'n':
        player.move(user_input, player.current_room.n_to)

    elif user_input == 's':
        player.move(user_input, player.current_room.s_to)

    elif user_input == 'e':
        player.move(user_input, player.current_room.e_to)

    elif user_input == 'w':
        player.move(user_input, player.current_room.w_to)
    else:
        print('Invalid input. Try again!\n')
    print()

print('Goodbye!')
