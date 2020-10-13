import random
import numpy as np
import cv2

class Item:
    def __init__(self,i, j, deep):
        self.i = i
        self.j = j
        self.deep = deep

class Gamer:
    def __init__(self, color, side, i, j):
        self.color = color
        self.side = side
        self.i = i
        self.j = j


class CField:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.items = []
        for i in range(length):
            self.items.append([1] * width)
        for i in range(length):
            for j in range(width):
                self.items[i][j] = Item(i, j, random.randint(1, 3))

def get_color(value):
    if value == 0:
        return (50, 0, 0)
    elif value == 1:
        return (105, 0, 0)
    elif value == 2:
        return (150, 0, 0)
    elif value == 3:
        return (205, 0, 0)
    else:
        return (0, 0, 0)

def get_user_color(value):
    if value == 0:
        return (0, 100, 100)
    elif value == 1:
        return (0, 200, 50)
    elif value == 2:
        return (0, 255, 0)
    elif value == 3:
        return (0, 0, 255)
    else:
        return (255, 255, 255)

def Print_Field(G_1):
    for f in range(length):
        st = []
        for g in range(width):
            st.append(Field.items[f][g].deep)
        print(st)
    print('position: ', G_1.i -1 , G_1.j -1 )
    # print("Position gamer_1: ", Gamer_1.i+1,Gamer_1.j+1,"Depth position gamer_1: ", Field.items[Gamer_1.i][Gamer_1.j].depth," . Position gamer_2: ",Gamer_2.i+1,Gamer_2.j+1,". Depth position gamer_2: ", Field.items[Gamer_2.i][Gamer_2.j].depth )

def Move(i,j):
    G_1.side = definition_side(i,j)
    for k in range(len(Aviable_sides)):
        if (G_1.side == Aviable_sides(k)):
            if(i==G_2.i) and (j==G_2.j):
                attack(i,j)
            if (Field.items[G_2.i][G_2.j].deep == 0):
                Game = 0
            else:
                aviable_sides(G_1.i, G_1.j)

    aviable_sides(G_1.i,G_1.j)





def attack(i,j):
        #  if (G_2.i==length-1)and   если она находится на границе
        G_1.i=G_2.i
        G_1.j=G_2.j
        G_1.side = definition_side(i, j)
        # прибавляем г_2 +1 в и либо ж
        if G_1.side == "up":
            G_2.i+=1
        if G_1.side == "down":
            G_2.i -= 1
        if G_1.side == "left":
            G_2.j -= 1
        if G_1.side == "right":
            G_2.j += 1





def definition_side(G_1, i,j):
    if (G_1.i < i) and (G_1.j == j):
        return "up"
    if (G_1.i == i) and (G_1.j < j):
        return "right"
    if (G_1.i > i) and (G_1.j == j):
        return "down"
    if (G_1.i == i) and (G_1.j > j):
        return "left"
    if (G_1.i == i) and (G_1.j == j):
        return "yourself"
    else:
        return False



def aviable_sides(i,j):
    if (G_1.i+1==length):
    #запоминать все прошлые ходы и если он нажал сам на себя то давать право ходить в любую сторону
        G_1.side = definition_side(i,j)
    if G_1.side == "yourself":
        Aviable_sides=All_sides
    else:
        Aviable_sides.remove(G_1.side)
def corner_side(i, j, length, width):
    left, up, right, down = True, True, True, True
    if i==length-1:
        down = False
    elif i == 0:
        up = False
    if j == width-1:
        right = False
    elif j == 0:
        left = False
    return up, right, down, left


def Visualise_Field():
    cv_image = np.zeros((600, 500, 3), np.uint8)
    cv_image[:, :] = (15, 40, 0)
    counter = 0
    for f in range(length):
        for g in range(width):
            # color = get_color(Field.items[f][g].k)
            color = get_color(Field.items[f][g].deep)
            cv_image[int(500*f/length):int(500*(f+1)/length), int(500*g/width):int(500*(g+1)/width)] = color
            
    for k in range(num_gamers):
        if not Game_over[k]:
            f, g = Gamers[k].i, Gamers[k].j
            user_color = get_user_color(Gamers[k].color)
            cv_image[int(500*(f+0.3)/length):int(500*(f+0.7)/length), int(500*(g+0.3)/width):int(500*(g+0.7)/width)] = user_color
    for i in range(length+1):
        cv2.line(cv_image,(0, int(i*500/length)),(500, int(i*500/length)),(100,100,100), 3)
    for j in range(width+1):
        cv2.line(cv_image,(int(j*500/width), 0),(int(j*500/width), 500),(100,100,100), 3)

    return cv_image
def give_x_y(x,y):
    global position_x, position_y
    position_x, position_y = x, y

def pick_color(event,x,y,flags,param):
    global start
    if event == cv2.EVENT_LBUTTONDOWN:
        # pixel = image_hsv[y,x]
        start = 1
        # print(x,y)
        give_x_y(x,y)

# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
length = 10
width = 10
Field = CField(length, width)
# Main_DList = DList_1
Position_error=True
while Position_error:
    Gamer_1 = Gamer(1, "yourself", random.randint(0,length),random.randint(0,width))
    Gamer_2 = Gamer(2, "yourself",random.randint(0,length),random.randint(0,width))
    if (Gamer_1.i==Gamer_2.i) and (Gamer_1.j==Gamer_2.j):
        Position_error=True
    else:
        Position_error=False
Gamers = []
Gamers.append(Gamer_1)
Gamers.append(Gamer_2)

player_error=True
second_player_error=True
Game = 1
wave=1

num_gamers = 2

Game_over = np.zeros(num_gamers, np.uint8)
print(Game_over)


start = 0
Aviable_sides_1=["up", "right", "down", "left", "yourself"]
Aviable_sides_2=["up", "right", "down", "left", "yourself"]
All_sides=["up", "right", "down", "left", "yourself"]
Aviable_sides_arr = []
Aviable_sides_arr.append(Aviable_sides_1)
Aviable_sides_arr.append(Aviable_sides_2)
while Game:
    for gamer in range(num_gamers):
        G_1 = Gamers[gamer]
        player_error = True
        while player_error:
            # Print_Field(G_1)
            cv_image = Visualise_Field()
                # cv2.imshow('hsv', cv_image)
            cv2.putText(cv_image, 'Player ' + str(gamer+1) + ' move', (int(250),  int(530)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (255, 255, 255), 4)
            cv2.namedWindow('hsv')
            cv2.setMouseCallback('hsv', pick_color)
            cv2.imshow('hsv', cv_image)
            cv2.waitKey(10)
            if start == 0:
                cv2.waitKey(100)
                continue
            print(position_x, position_y)
            i_1, j_1 = int(position_y*length/500), int(position_x*width/500) 
            def_side = definition_side(G_1, i_1, j_1)
            print('def_side: ', def_side)
            if (def_side in Aviable_sides_arr[gamer]) and (Field.items[i_1][j_1].deep>0):
                Field.items[i_1][j_1].deep -= 1
                Gamers[gamer].i, Gamers[gamer].j = i_1, j_1
                if def_side == 'yourself':
                    if Field.items[i_1][j_1].deep == 0:
                        print('Game_over for '+ str(gamer+1))
                        Game_over[gamer] = 1
                        continue
                    Aviable_sides_arr[gamer] = All_sides
                else: 
                    arr = []
                    arr = corner_side(i_1, j_1, length, width)
                    for side in range(4):
                        if not arr[side]:
                            Aviable_sides_arr[gamer].remove(All_sides[side])
                    Aviable_sides_arr[gamer].remove(def_side)
                player_error = False
            # else:
            #     print('AGAIN')

    # if Game_over.all == 1 and (wave > 1):
    #     Game = 0
    #     print('Game is over')
        # if (G_1.sum == 0):
        #     print("Game over. Gamer_2 win!!!")
        # else:
        #     print("Game over. Gamer_1 win!!!")
    
    wave +=1
