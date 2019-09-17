''' Use x and y variables to track were the user is.
    Use statemensts to move the user where he chooses.
    Print out where the user is, so he can move according to wich tile he is on.
    Winner tile is (3,1) and then Winner is printed
'''

print("You can travel: (N)orth.")
direction = input('Direction: ')
x=1
y=1

while True:
    # (1,1)
    if x == 1 and y == 1:
       if direction == "n" or direction == "N":
           y += 1
           print("You can travel: (N)orth or (E)ast or (S)outh.")
       else:
          print("Not a valid direction!")
       direction =  input('Direction: ')

    # (1,2)
    if x == 1 and y == 2:
        if direction == "n" or direction == "N":
            y += 1
            print('You can travel: (E)ast or (S)outh.')
        elif direction == "s" or direction == "S":
            y -= 1
            print("You can travel: (N)orth.")
        elif direction == "e" or direction == "E":
            x += 1
            print("You can travel: (S)outh or (W)est.")
        else:
            print("Not a valid direction!")
        direction =  input('Direction: ')
    #(1,3)
    if x == 1 and y == 3:
        if direction == "e" or direction == "E":
            x += 1
            print("You can travel: (E)ast or (W)est.")
        elif direction == "s" or direction == "S":
            y -= 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else: 
            print("Not a valid direction!")
        direction =  input('Direction: ')
    # (2,1)
    if x == 2 and y == 1:
        if direction == "n" or direction == "N":
            y += 1
            print("You can travel: (S)outh or (W)est.")
        else: 
            print("Not a valid direction!")
        direction =  input('Direction: ')
    # (2,2)
    if x == 2 and y == 2:
        if direction == "w" or direction == "W":
            x -= 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif direction == "s" or direction == "S":
            y-= 1
            print("You can travel: (N)orth.")
        else:
            print("Not a valid direction!")
        direction =  input('Direction: ')
    #Tile 2,3
    if x==2 and y==3:
        if direction == 'e' or direction == 'E':
            x+=1
            print("You can travel: (S)outh or (W)est.")
        elif direction == 'w' or direction == 'W':
            x-=1
            print("You can travel: (S)outh or (E)ast.")
        else: 
            print('Not a valid direction!')
        direction =  input('Direction: ')
    #Tile 3,2
    if x==3 and y==2:
        if direction == 'n' or direction=='N':
            y+=1
            print("You can travel: (S)outh or (W)est.")
        elif direction == 's' or direction == 'S':
            y-=1
            break
        else: 
            print('Not a valid direction!')
        direction =  input('Direction: ')
    # Tiles 3,3
    if x==3 and y==3:
         if direction == 'w' or direction == 'W':
              x -= 1
              print("You can travel: (E)ast or (W)est.")
         elif direction == 's' or direction == 'S':
             y-=1
             print("You can travel: (N)orth or (S)outh.")
         else:
             print('Not a valid direction')
         direction =  input('Direction: ')
    if x==3 and y==1:
        break    
print('Victory!')