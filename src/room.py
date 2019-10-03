# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = False
        self.e_to = False
        self.s_to = False
        self.w_to = False

    def __str__(self):
        result = f"{self.name}\n{self.description}\n"
        if self.n_to:
            result += f"N: {self.n_to.name}\n"
        if self.s_to:
            result += f"S: {self.s_to.name}\n"
        if self.e_to:
            result += f"E: {self.e_to.name}\n"
        if self.w_to:
            result += f"W: {self.w_to.name}\n"
        for item in self.items:
            result += f"{item.name}\n"
        return result

    def __repr__(self):
        return f"Room({repr(self.name)},{repr(self.description)})"

    def remove_item(self, item):
        self.items.remove(item)
