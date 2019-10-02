# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def __str__(self):
        return f"The player, located in {self.current_room}"

    def move(self, direction, room):
        if direction.lower() == 'n' and room.n_to == True:
            self.current_room = room
        elif direction.lower() == 's' and room.s_to == True:
            self.current_room = room
        elif direction.lower() == 'e' and room.e_to == True:
            self.current_room = room
        elif direction.lower() == 'w' and room.w_to == True:
            self.current_room = room
        else:
            print('No path in that direction.')
