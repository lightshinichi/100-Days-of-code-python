
print('Welcome to treasure Island')
print('Your mission is to find the treasure')
direction = input('Youre at a cross road.Where do you want to go?, Type "left" or "right"')
if direction == 'left':
    act_1 = input('You come to a lake .There is an island in the middle of the lake. Type "wait" to wait for a '
                  'boat.Type "swim" to swim across.')
    if acts_1 == 'wait':
        print('Ok, waiting for ship')
        print('You have successfully reached the Island on a boat.')
        door=input('Select one among the 3 doors,yellow, blue or green')
        if door == 'yellow':
            print('the room is full of fire,Gameover')

        elif door== 'green':
            print('You have found the Treasure, You won')

        elif door == 'blue':
            print('the room is full of water,Gameover')

    if act_1 == 'swim':
        print('You have been swimming and got tired sank game over')

if direction== 'right':
    print('Deadend, Gameover')





