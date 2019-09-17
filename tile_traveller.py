''' Use x and y variables to track were the user is.
    use functions to move the user where he chooses.
    Print out where the user is, so he can move according to wich tile he is on.
    Winner tile is (3,1) and then Winner is printed
'''
''' 
function for tile 3,3 and 2,2
def upp_right(x,y):

'''
direction = input('Direction: ')
x=3
y=3

while True:
    #Tile 2,3
    if x==2 and y==3:
        if direction == 'e' or direction == 'E':
            x+=1
        elif direction == 'w' or direction == 'W':
            x-=1
        else: 
            print('Not a valid direction!')
    #Tile 3,2
    if x==3 and y==2:
        if direction == 'n' or direction=='N':
            x+=1
        elif direction == 's' or direction == 'S':
            y -=1
        else: 
            print('Not a valid direction!')
        
    # Tiles 3,3 and 2,2
    if x==3 and y==3 or x==2 and y==2:
         if direction == 'e' or direction == 'E':
             x -= 1
         elif direction == 's' or direction == 'S':
             y-=1
         else:
             print('Not a valid direction')

    if x==3 and y==1:
        break
    print(x,y)    
    direction =  input('Direction: ')
    print("hallo")
    
print('Victory!')