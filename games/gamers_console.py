import random
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


AList = []
Previous_waves = []
DList_1 = []
DList_2 = []
Users = []
Former_users = []

def Print_Field():
    for f in range(length):
        st = []
        for g in range(width):
            st.append(Field.items[f][g].k)
        print(st)
    for n in range(number_of_gamers):
        print("Sum of points gamer_",n+1,": ",Users[n].sum,". Number of cells gamer_",n+1,": ", Users[n].number_of_cells)

    print("Number of waves: ", wave)


def Add_count(i, j):
    #Print_Field()
    #print("ya v add_count", i, j)
    Field.items[i][j].k += 1
    Field.items[i][j].color = Main_User.allow
    Main_User.sum += 1
    if (Field.items[i][j].k - 1 == 0):
        Main_User.number_of_cells += 1
    #Print_Field()
    #print("ya v add_count posle number_of_cells + 1")
    if (Field.items[i][j].k > 3):
        Main_DList.append([i, j])


def Clear_Dis_List():
    #Print_Field()
    #print("ya v clear_dis_list")
    for c in range(len(Main_DList)):
        Disclosure(Main_DList[0][0], Main_DList[0][1])
        Main_DList.pop(0)

    #Print_Field()
    #print("ya v clear_dis_list posle cikla")
    if len(AList) > 0:
        Clear_Add_List()


def Clear_Add_List():
    if (Field.t == 1):
        Main_DList = DList_1
    else:
        Main_DList = DList_2

    #Print_Field()
    #print("ya v clear_add_list")
    for c in range(len(AList)):
        Add_count(AList[0][0], AList[0][1])
        AList.pop(0)
    Print_Field()
    #print("ya v clear_add_list posle cikla")

    Clear_Dis_List()
    if (Field.t == 1):
        Main_DList = DList_2
        Field.t = 2
    else:
        Main_DList = DList_1
        Field.t = 1


def Disclosure(i, j):
    #Print_Field()
    #print("ya v disclosure", i, j)
    Field.items[i][j].k -= 4
    if (Field.items[i][j].k ==0):
        Field.items[i][j].color = 0
    Main_User.sum-=4
    Main_User.number_of_cells-=1
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

length = int(input("Enter length: "))
width = int(input("Enter width: "))
Field = CField(length, width)
Main_DList = DList_1


start = [1,1,1,width -2 ,length -2 , 1,length-2,width -2 ]


number_of_gamers = int(input("Enter number of gamers"))
for n in range(number_of_gamers):
    Users.append(Gamer(n+1,3,1,start[2*n],start[2*n+1]))
    Field.items[start[2*n]][start[2*n+1]].k = 3
    Field.items[start[2 * n]][start[2 * n + 1]].color = Users[n].allow



player_error=True
Game = 1
wave = 1
Print_Field()
while Game:
    for n in range(number_of_gamers):
        if Users[n].sum != 0 and len(Former_users) < number_of_gamers-1:
            while player_error:
                Main_User=Users[n]
                print("Enter i",n+1,"user: ")
                i = int(input())
                print("Enter j", n + 1, "user: ")
                j = int(input())
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

print(Previous_waves)
#можно потом будет убрать чтобы ставилось обязательно только на свои cells