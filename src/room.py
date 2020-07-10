# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from random import *

class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        
    def __str__(self):
        if len(self.items) > 0:
            return f"Room Info: {self.room_name}\n{self.description} \nItem: {self.items[0]}"
        else:
            return f"Room Info: {self.room_name}\n{self.description} \nItem: None"
            
    def item_spawn(self, spawn):
        return self.items.append(spawn)
    
    def picked_up(self, spawn):
        del self.items[spawn]
            
                  
                      
                   