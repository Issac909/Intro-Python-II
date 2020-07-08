from room import Room
from player import Player 

import textwrap

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
print('I see you have chosen to start your adventure... I suppose that time comes for every child of light. My memory fails me at this time, please tell me, what is your name again?')
player_name = input('☼ ')
player1 = Player(f'{player_name}', room['outside'])
is_playing = True
# Write a loop that:
#   
# * Prints the current room name
print(f"Chapter 1: When one journey ends... \n{player1.current_room.log_name()}")
# * Prints the current description (the textwrap module might be useful here).
for line in textwrap.wrap(player1.current_room.get_description()):
    print(line)
    
while is_playing is True:
    print(f"Welcome {player1.name}. This is no normal cave, we are standing outside a seeker church, or as we say, 'Church of Traitors'. Just look around and see if you can find any clues. The greedy mongrols may have left some treasure behind as well, finders keepers!")
    player_input = input(f"Use [W, A, S, D] to navigate between rooms. Press W now to move into {room['foyer']}. You can quit any time pressing 'Q'")
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed
    position = player1.current_room
    error = print("Can't go any further in this direction")
    if player_input.upper() == 'Q':
        is_playing = False
    else:
        # Outside
        if position == room.keys()[0]:
            if player_input.upper() == 'W':
                position = room['outside'].n_to
            else:
                error
        # Foyer 
        elif position == room.keys()[1]:
            if player_input.upper() == 'W':
                position = room['foyer'].n_to
            elif player_input.upper() == 'S':
                position = room['foyer'].s_to
            elif player_input.upper() == 'D':
                position = room['foyer'].e_to
            else:
                error
        # Overlook    
        elif position == room.keys()[2]:
            if player_input.upper() == 'S':
                position = room['overlook'].s_to
            elif player_input.upper() == 'D':
                error
            else:
                error
        # Narrow        
        elif position == room.keys()[3]:
            if player_input.upper() == 'W':
                position = room['narrow'].n_to
            elif player_input.upper() == 'A':
                position = room['narrow'].w_to
            else:
                error
        # Treasure    
        elif position == room.keys()[4]:
            if player_input.upper() == 'S':
                position = room['treasure'].s_to
            else:
                error
        else:
            error

# If the user enters "q", quit the game.