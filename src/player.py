# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"The player, located in {self.current_room}"

    def move(self, direction, room):
        if direction.lower() == 'n' and self.current_room.n_to:
            self.current_room = room
        elif direction.lower() == 's' and self.current_room.s_to:
            self.current_room = room
        elif direction.lower() == 'e' and self.current_room.e_to:
            self.current_room = room
        elif direction.lower() == 'w' and self.current_room.w_to:
            self.current_room = room
        else:
            print('No path in that direction.\n')

    def get_item(self, item):
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.remove_item(item)
        else:
            print('\nThat item does not exist!')

    def check_inventory(self):
        print()
        print(f"{self.name}'s inventory:")
        for item in self.inventory:
            print(item.name)
        print()
