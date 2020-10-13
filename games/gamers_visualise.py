import random
import cv2 
import numpy as np 

class Item:
    def __init__(self, k, access, i, j, color):
        self.k = k
        self.access = access
        self.i = i
        self.j = j
        self.color = color


class Gamer:
    def __init__(self, allow, sum, number_of_cells, i ,j ):
        self.allow = allow
        self.sum = sum
        self.number_of_cells = number_of_cells
        self.i = i
        self.j = j


class CField:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.items = []
        for i in range(length):
            self.items.append([0] * width)
        for i in range(length):
            for j in range(width):
                self.items[i][j] = Item(0, 1, i, j, 0)
        self.t = 1


def Print_Field():
    for f in range(length):
        st = []
        for g in range(width):
            st.append(Field.items[f][g].k)
        print(st)
    for n in range(number_of_gamers):
        print("Sum of points gamer_",n+1,": ",Users[n].sum,". Number of cells gamer_",n+1,": ", Users[n].number_of_cells)

    print("Number of waves: ", wave)

def get_color(value):
    if value == 0:
        return (15, 40, 0)
    elif value == 1:
        return (255, 0, 0)
    elif value == 2:
        return (100, 0, 255)
    elif value == 3:
        return (255, 255, 0)
    else:
        return (255, 255, 255)



def Visualise_Field():
    cv_image = np.zeros((600, 500, 3), np.uint8)
    cv_image[:, :] = (15, 40, 0)
    counter = 0
    for f in range(length):
        for g in range(width):
            # color = get_color(Field.items[f][g].k)
            color = get_color(Field.items[f][g].color)
            cv_image[int(500*f/length):int(500*(f+1)/length), int(500*g/width):int(500*(g+1)/width)] = color
            
    for f in range(length):
        for g in range(width):
            cv2.putText(cv_image, str(Field.items[f][g].k), (int(500*(g+0.35)/width),  int(500*(f+0.6)/length)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 4)
    for i in range(length+1):
        cv2.line(cv_image,(0, int(i*500/length)),(500, int(i*500/length)),(100,100,100), 3)
    for j in range(width+1):
        cv2.line(cv_image,(int(j*500/width), 0),(int(j*500/width), 500),(100,100,100), 3)

    return cv_image

def aviable_sides(i, j, length, width):
    left, up, right, down = True, True, True, True
    if i==length-1:
        down = False
    elif i == 0:
        up = False
    if j == width-1:
        right = False
    elif j == 0:
        left = False
    return left, up, right, down


def Visual_Disclosure(i, j):
    
    for frame in range(10):
        cv_image = np.zeros((600, 500, 3), np.uint8)
        cv_image[:, :] = (15, 40, 0)
        cv_image = Visualise_Field()
        for f in range(length):
            for g in range(width):
                if i==f and j==g:
                    color = get_color(Field.items[i][j].color)
                    addition_1 = 500*frame/10/length
                    addition_2 = 500*frame/10/width
                    left, up, right, down = aviable_sides(i, j, length, width)
                    if right:
                        cv_image[int((500)*f/length):int(500*(f+1)/length), int((500)*g/width+addition_2):int((500)*(g+1)/width+addition_2)] = color
                    if down:
                        cv_image[int((500)*f/length+addition_1):int(500*(f+1)/length+addition_1), int((500)*g/width):int((500)*(g+1)/width)] = color
                    if up:
                        cv_image[int((500)*f/length-addition_1):int(500*(f+1)/length-addition_1), int((500)*g/width):int((500)*(g+1)/width)] = color
                    if left:
                        cv_image[int((500)*f/length):int(500*(f+1)/length), int((500)*g/width-addition_2):int((500)*(g+1)/width-addition_2)] = color

        cv2.imshow('hsv', cv_image)
        cv2.waitKey(10)

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


def Add_count(i, j):

    Field.items[i][j].k += 1
    Field.items[i][j].color = Main_User.allow
    Main_User.sum += 1
    if (Field.items[i][j].k - 1 == 0):
        Main_User.number_of_cells += 1

    if (Field.items[i][j].k > 3):
        Main_DList.append([i, j])


def Clear_Dis_List():

    for c in range(len(Main_DList)):
        result = Disclosure(Main_DList[0][0], Main_DList[0][1])
        print(result)
        Main_DList.pop(0)

    if len(AList) > 0:
        Clear_Add_List()


def Clear_Add_List():
    for c in range(len(AList)):
        Add_count(AList[0][0], AList[0][1])
        AList.pop(0)

    Clear_Dis_List()

def Disclosure(i, j):

    Field.items[i][j].k -= 4
    if Field.items[i][j].k < 0:
        Field.items[i][j].k += 4
        return False

    Visual_Disclosure(i,j)
    if Field.items[i][j].k == 0:
        Field.items[i][j].color = 0
        Main_User.number_of_cells-=1
    Main_User.sum-=4
    for c in [-1, 1]:
        if (i + c < length) and (i + c >= 0):
            AList.append([i + c, j])

            for n in range(number_of_gamers):
                if Field.items[i + c][j].color == Users[n].allow and Users[n]!=Main_User:
                        Main_User.number_of_cells += 1
                        Users[n].number_of_cells -= 1
                        Main_User.sum += Field.items[i + c][j].k
                        Users[n].sum -= Field.items[i + c][j].k
            Field.items[i + c][j].color = Main_User.allow
        if (j + c < width) and (j + c >= 0):
            AList.append([i, j + c])
            for n in range(number_of_gamers):
                if Field.items[i][j+c].color == Users[n].allow and Users[n] != Main_User:
                    Main_User.number_of_cells += 1
                    Users[n].number_of_cells -= 1
                    Main_User.sum += Field.items[i ][j+c].k
                    Users[n].sum -= Field.items[i ][j+c].k
            Field.items[i][j+c].color = Main_User.allow
    return True
AList = []
Previous_waves = []
DList_1 = []

Users = []
Former_users = []

length = int(input("Enter length: "))
width = int(input("Enter width: "))
Field = CField(length, width)
Main_DList = DList_1


start = [1,1,1,width -2 ,length -2 , 1,length-2,width -2 ]


number_of_gamers = int(input("Enter number of gamers: "))
for n in range(number_of_gamers):
    Users.append(Gamer(n+1,3,1,start[2*n],start[2*n+1]))
    Field.items[start[2*n]][start[2*n+1]].k = 3
    Field.items[start[2 * n]][start[2 * n + 1]].color = Users[n].allow

player_error=True
Game = 1
wave = 1


start = 0


Visualise_Field()

while Game:
    for n in range(number_of_gamers):
        if Users[n].sum != 0 and len(Former_users) < number_of_gamers-1:
            while player_error:
                cv_image = Visualise_Field()
                # cv2.imshow('hsv', cv_image)
                for user in range(number_of_gamers):
                    cv2.putText(cv_image, 'sum '+str(user+1) + ' user = ' + str(Users[user].sum), (int(50),  int(530+user*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)
                cv2.putText(cv_image, 'Player ' + str(Users[n].allow) + ' move', (int(250),  int(530)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 4)
                cv2.putText(cv_image, 'wave: ' + str(wave), (int(250),  int(560)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 4)
                cv2.namedWindow('hsv')
                Main_User=Users[n]
                cv2.setMouseCallback('hsv', pick_color)
                cv2.imshow('hsv', cv_image)
                cv2.waitKey(10)
                if start == 0:
                    cv2.waitKey(100)
                    continue
                # print('positionnnnnn', position_x, position_y, int(position_x*width/500), int(position_y*length/500))
                i, j = int(position_y*length/500), int(position_x*width/500) 
                # print('color user', Field.items[i][j].color)
                if Field.items[i][j].color==Users[n].allow :
                    player_error=False
                else:
                    player_error=True
            player_error=True
            AList.append([i, j])
            Clear_Add_List()
        else:
            if not(Users[n].allow in Former_users):
                Former_users.append(Users[n].allow)
        if len(Former_users) == number_of_gamers-1:
            Game = 0
            if Users[n].sum!=0:
                print("Game over. Gamer",n+1," won!!!")
        Previous_waves.append(Field.items)
    wave+=1
