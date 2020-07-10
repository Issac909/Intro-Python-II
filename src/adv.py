from room import Room
from player import Player 
from item import Item

import textwrap
import time
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#   
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
player1 = ''
no_room = "Can't go any further in this direction"
error = "Seems you found your way out of bounds. Please restart the game to continue."

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def intro():
    delay_print('I see you have chosen to start your adventure... I suppose that time comes for\nevery child of light. My memory fails me at this time, please tell me, what is \nyour name again?\n')

def scene1(name):    
    
    delay_print(f"\t\tChapter 1: When one journey ends... \n{player_name}\n{player1.current_room.room_name}\n")
    for line in textwrap.wrap(player1.current_room.description):
        delay_print(line)
    delay_print(f"\t\t\nWelcome {name}. This is no normal cave, we are standing outside a seeker church, \nor as we say, 'Church of Traitors'. Just look around and see if you can find\nany clues. The greedy mongrols may have left some treasure behind as well, \nfinders keepers!\n")
            
# Items
lantern = Item('lantern', 'This lantern seems like it was recently lit.\n')

# Room Items Spawn in
room['foyer'].item_spawn(lantern)

    # Intro
intro()
player_name = input('☼ ')
time.sleep(1)

# Scene 1  
player1 = Player(f'{player_name}', room['outside'])
scene1(player_name)
time.sleep(1)
player_input = input("Ready? (Y) or (Q)")
# Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed


while player_input.upper() != 'Q':
    player_input = input("\t\tControls: [W], [A], [S], [D] | Options: [I] [E] [R] [H] | Quit = [Q]\n")
    try:
        if player_input.upper()  == 'H':
            player_input = input(f"\nUse ['W'(North), 'A'(West), 'S'(South), 'D'(East)] to navigate between rooms. \nCheck room info with [R] and pick up items with [E]. You can quit any time \npressing 'Q'. For help, (to see this message again) press 'H'\nPress 'B' to go back to the game.\n")
            continue
        elif player_input.upper() == 'R':
            delay_print(f"{player1.current_room}")
            continue
        elif player_input.upper() == 'E':
            spawned_item = player1.current_room.items[0]
            player1.pick_up_item(spawned_item, delay_print)
            player1.current_room.items = []
            continue
        elif player_input.upper() == 'I':
            print(f"Inventory: {player1.items}")
            continue
        elif player_input.upper() == 'W' or 'A' or 'S' or 'D':
            # Outside
            if player1.current_room == room['outside']:
                if player_input.upper() == 'W':
                    player1.current_room = room['outside'].n_to
                    continue
            # Foyer 
            elif player1.current_room == room['foyer']:
                if player_input.upper() == 'W':
                    player1.current_room = room['foyer'].n_to
                    continue
                elif player_input.upper() == 'S':
                    player1.current_room = room['foyer'].s_to
                    continue
                elif player_input.upper() == 'D':
                    player1.current_room = room['foyer'].e_to
                    continue
            # Overlook    
            elif player1.current_room == room['overlook']:
                if player_input.upper() == 'S':
                    player1.current_room = room['overlook'].s_to
                    continue
            # Narrow        
            elif player1.current_room == room['narrow']:
                if player_input.upper() == 'W':
                    player1.current_room = room['narrow'].n_to
                    continue
                elif player_input.upper() == 'A':
                    player1.current_room = room['narrow'].w_to
                    continue
            # Treasure    
            elif player1.current_room == room['treasure']:
                if player_input.upper() == 'S':
                    player1.current_room = room['treasure'].s_to
                    continue
            else:
                delay_print(no_room)
                continue
        else:
            delay_print('Invalid input.') 
            continue
    except: 
        delay_print(error)
        time.sleep(1)
        break   
              
# If the user enters "q", quit the game.