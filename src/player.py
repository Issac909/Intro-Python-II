# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def __str__(self):
        return f"☼ Player Info: {self.name}, {self.current_room.name}"
    
    def move_to(self, next_room):
        self.current_room = next_room
        
    def pick_up_item(self, item, delay_print):
        if item:
            self.items.append(item)
            return delay_print(f"Picked up {item}.")
        else:
            return delay_print("No items were found.")
        
    def item_check(self, item):
        for x in self.items:
            if x.name == item:
                return True
            
        return False
        
