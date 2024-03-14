#Connect4.py
import turtle
import threading

turtle.bgcolor('black')

c = turtle.Pen()
c.speed(0)
c.hideturtle()
c.penup()

b = turtle.Pen()
b.speed(0)
b.hideturtle()

u = turtle.Pen()
u.speed(0)
u.hideturtle()
u.penup()
screen = turtle.Screen()
board = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O']]
counter=0
stop = False
winner = 'none'

def build_board():
    b.penup()
    b.setpos(-215, 185)
    b.pendown
    b.fillcolor("blue")
    b.begin_fill()
    for _ in range(2):
        b.forward(430)
        b.right(90)
        b.forward(370)
        b.right(90)
    b.end_fill()

    yc = 150
    b.penup()
    b.setpos(-215, yc)
    i = 0
    for r in board:
        i+=1
        for c in r:
            b.forward(35)
            b.dot(50, "white")
            b.forward(25)        
        b.forward(35)
        yc-=60
        b.setpos(-215, yc)
    b.forward(35)
    b.color('white')
    for f in range(7):
        b.write(f+1, font=("Arial", 16, "normal"))
        b.forward(60)

def check_win():
    global board, stop, winner
    for g in range(3):
        for h in range(7):
            if board[g+3][h]==board[g+2][h]==board[g+1][h]==board[g][h]!='O':
                print(str(board[g+3][h])+" WINS!")
                winner = str(board[g+3][h]).upper()
                stop = True
    if stop==False:
        for g in range(4):
            for h in range(6):
                if board[h][g+3]==board[h][g+2]==board[h][g+1]==board[h][g]!='O':
                    print(str(board[h][g+3])+" WINS!")
                    winner = str(board[h][g+3]).upper()
                    stop = True
    if stop==False:
        for g in range(3):
            for h in range(4):
                if board[(g+3)][(h+3)]==board[(g+3)-1][(h+3)-1]==board[(g+3)-2][(h+3)-2]==board[(g+3)-3][(h+3)-3]!='O':
                    print(str(board[g+3][h+4])+" WINS!")
                    winner = str(board[g+3][h+4]).upper()
                    stop = True
                elif board[(g+3)][h]==board[(g+3)-1][h+1]==board[(g+3)-2][h+2]==board[(g+3)-3][h+3]!='O':
                    print(str(board[g+3][h])+" WINS!")
                    winner = str(board[g+3][h]).upper()
                    stop = True               

def add_chip(color, message):
    global board, stop
    try:
        col = int(screen.textinput("Connect4","Which column " + message + " ?"))
        col-=1
        i = 1
        while board[i][col]=='O':
            i+=1
            if i==6:
                break
        if i==1 and board[0][col] != 'O':
            print("can't place there")
            call_back(color, message)
        else:
            board[i-1][col] = color
            thread = threading.Thread(target = check_win, args = ())
            thread.start()
        animate(-180+(col*60), 150-(60*(i-1)), color, 50)
    except:
        print("DID NOT TYPE VAILD NUMBER")
        clos = screen.textinput("Connect4", "Quit?")
        if clos=="yes":
            turtle.done()
            stop = True
            screen.exitonclick()
        else:
            call_back(color, message)

def call_back(color, message):
    add_chip(color, message)

def animate(x, y, color, diam):
    global board
    rx = x
    ry = int((150-y)/60)
    for f in range(ry):
        c.setpos(x, (150-(f*60)))
        c.dot(diam, color)
        c.dot(diam, "white")
    c.setpos(x, y)
    c.dot(diam, color)

    
def start():
    global counter, stop
    while stop==False:
        if counter==0:
            add_chip('red', "Player One")
            u.clear()
            u.setpos(-77, (200))
            u.color('yellow')
            u.write("Player Two Turn", font=("Arial", 16, "normal"))
            counter+=1
        else:
            add_chip('yellow', "Player Two")
            u.clear()
            u.setpos(-77, (200))
            u.color('red')
            u.write("Player One Turn", font=("Arial", 16, "normal"))
            counter=0
    u.clear()
    u.setpos(-77, (200))
    u.color('White')
    u.write(winner + " is the WINNER", font=("Arial", 16, "normal"))

build_board()
start()
print("Terminated process")
turtle.done()
