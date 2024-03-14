#Pentago
import turtle

Gs = 590
Bs = 280

turtle.bgcolor('gray')
Gt = turtle.Pen()
Gt.hideturtle()
Gt.speed(0)

Bt = turtle.Pen()
Bt.hideturtle()
Bt.speed(0)
Bt.penup()

p = turtle.Pen()
p.hideturtle()
p.speed(0)
p.penup()

w = turtle.Pen()
w.hideturtle()
w.speed(0)
w.penup()

screen = turtle.Screen()

d = 'dark red'
p1 = 'black'
p2 = 'white'
shiftC = 105
ds = 50

b1y = 250
b1x = -b1y
b1 = [[b1x, b1y],
      [b1x+(shiftC), b1y],
      [b1x+(shiftC*2), b1y],
      [b1x, b1y-(shiftC)],
      [b1x+(shiftC), b1y-(shiftC)],
      [b1x+(shiftC*2), b1y-(shiftC)],
      [b1x, b1y-(shiftC*2)],
      [b1x+(shiftC*1), b1y-(shiftC*2)],
      [b1x+(shiftC*2), b1y-(shiftC*2)]]
b1C = [d,d,d,d,d,d,d,d,d]

b2x = 40
#b2y = b1yy
b2 = [[b2x, b1y],
      [b2x+(shiftC), b1y],
      [b2x+(shiftC*2), b1y],
      [b2x, b1y-(shiftC)],
      [b2x+(shiftC), b1y-(shiftC)],
      [b2x+(shiftC*2), b1y-(shiftC)],
      [b2x, b1y-(shiftC*2)],
      [b2x+(shiftC*1), b1y-(shiftC*2)],
      [b2x+(shiftC*2), b1y-(shiftC*2)]]
b2C = [d,d,d,d,d,d,d,d,d]

#b3x = b1x
b3y = -b2x
b3 = [[b1x, b3y],
      [b1x+(shiftC), b3y],
      [b1x+(shiftC*2), b3y],
      [b1x, b3y-(shiftC)],
      [b1x+(shiftC), b3y-(shiftC)],
      [b1x+(shiftC*2), b3y-(shiftC)],
      [b1x, b3y-(shiftC*2)],
      [b1x+(shiftC*1), b3y-(shiftC*2)],
      [b1x+(shiftC*2), b3y-(shiftC*2)]]
b3C = [d,d,d,d,d,d,d,d,d]

#b4y = b3y
b4x = b2x
b4 = [[b4x, b3y],
      [b4x+(shiftC), b3y],
      [b4x+(shiftC*2), b3y],
      [b4x, b3y-(shiftC)],
      [b4x+(shiftC), b3y-(shiftC)],
      [b4x+(shiftC*2), b3y-(shiftC)],
      [b4x, b3y-(shiftC*2)],
      [b4x+(shiftC*1), b3y-(shiftC*2)],
      [b4x+(shiftC*2), b3y-(shiftC*2)]]
b4C = [d,d,d,d,d,d,d,d,d]

pmb = 0
pmp = 0
tb = 0
td = 'l'

i = 1

winner = 'none'
stage = False
def print_board():
    global Gs
    Gt.setpos(-(Gs/2), Gs/2)
    Gt.fillcolor('white')
    Gt.begin_fill()
    for _ in range(4):
        Gt.forward(Gs)
        Gt.right(90)
    Gt.end_fill()

    Gt.penup()
    Gt.forward(10)
    Gt.right(90)
    Gt.forward(10)
    Gt.left(90)
    
    Gt.fillcolor('red')
    for f in range(2):
        Gt.begin_fill()
        for _ in range(4):
            Gt.forward(Bs)
            Gt.right(90)
        Gt.end_fill()
        Gt.forward(Bs+10)
    Gt.backward(Bs+10)
    Gt.backward(Bs+10)
    Gt.right(90)
    Gt.forward(Bs+10)
    Gt.left(90)
    for f in range(2):
        Gt.begin_fill()
        for _ in range(4):
            Gt.forward(Bs)
            Gt.right(90)
        Gt.end_fill()
        Gt.forward(Bs+10)
    
def check_win(player):
    global p1, p2, winner, b1C, b2C, b3C, b4C
    color = p1 if player=='one' else p2
    g = [[b1C[0], b1C[1], b1C[2], b2C[0], b2C[1], b2C[2]], 
         [b1C[3], b1C[4], b1C[5], b2C[3], b2C[4], b2C[5]],
         [b1C[6], b1C[7], b1C[8], b2C[6], b2C[7], b2C[8]],
         [b3C[0], b3C[1], b3C[2], b4C[0], b4C[1], b4C[2]],
         [b3C[3], b3C[4], b3C[5], b4C[3], b4C[4], b4C[5]],
         [b3C[6], b3C[7], b3C[8], b4C[6], b4C[7], b4C[8]]]
    for _ in range(2):
        for a in range(6):
            if g[_][a]==g[_+1][a]==g[_+2][a]==g[_+3][a]==g[_+4][a]==color:
                winner = player
                print("win")
                break
            elif g[a][_]==g[a][_+1]==g[a][_+2]==g[a][_+3]==g[a][_+4]==color:
                winner = player
                print("win")
                break
        for a in range(2):
            if g[_][a]==g[_+1][a+1]==g[_+2][a+2]==g[_+3][a+3]==g[_+4][a+4]==color:
                winner = player
                print("win")
                break
            elif g[_][a+4]==g[_+1][a+3]==g[_+2][a+2]==g[_+3][a+1]==g[_+4][a]==color:
                winner = player
                print("win")
                break

def update_block(block):
    global b1, b2, b3, b4, b1C, b2C, b3C, b4C, ds
    if block == 1:
        for a in range(9):
            Bt.setpos(b1[a][0], b1[a][1])
            Bt.dot(ds, b1C[a])
    elif block == 2:
        for a in range(9):
            Bt.setpos(b2[a][0], b2[a][1])
            Bt.dot(ds, b2C[a])
    elif block == 3:
        for a in range(9):
            Bt.setpos(b3[a][0], b3[a][1])
            Bt.dot(ds, b3C[a])
    elif block == 4:
        for a in range(9):
            Bt.setpos(b4[a][0], b4[a][1])
            Bt.dot(ds, b4C[a])

def place_marble(block, pos, player):
    global p1, p2, b1C, b2C, b3C, b4C, Stage1
    color = p1 if player=='one' else p2
    if block==1:
        b1C[pos] = color
    elif block==2:
        b2C[pos] = color
    elif block==3:
        b3C[pos] = color
    elif block==4:
        b4C[pos] = color
    update_block(block)
    Stage1 = False

def turn_block(block, LorR):
    global b1C, b2C, b3C, b4C
    if block==1:
        turn(b1C, LorR)
    elif block==2:
        turn(b2C, LorR)
    elif block==3:
        turn(b3C, LorR)
    elif block==4:
        turn(b4C, LorR)
    update_block(block)
    
def turn(bCarr, LorR):
    if LorR == 'r':
        temp = bCarr[0]
        temp1 = bCarr[1]
        bCarr[0] = bCarr[6]
        bCarr[6] = bCarr[8]
        bCarr[8] = bCarr[2]
        bCarr[2] = temp
        bCarr[1] = bCarr[3]
        bCarr[3] = bCarr[7]
        bCarr[7] = bCarr[5]
        bCarr[5] = temp1
    elif LorR == 'l':
        temp = bCarr[0]
        temp1 = bCarr[1]
        bCarr[0] = bCarr[2]
        bCarr[2] = bCarr[8]
        bCarr[8] = bCarr[6]
        bCarr[6] = temp
        bCarr[1] = bCarr[5]
        bCarr[5] = bCarr[7]
        bCarr[7] = bCarr[3]
        bCarr[3] = temp1

def get_marblepos():
    global b1, b2, b3, b4, ds, pmb, pmp
    x = p.xcor()
    y = p.ycor()
    b = 0
    posB = []
    pos = 0
    dss = ds/2
    if x < 0 and y < 0:
        b = 3
    elif x < 0 and y > 0:
        b = 1
    elif x > 0 and y > 0:
        b = 2
    elif x > 0 and y < 0:
        b = 4

    posB = b1 if b==1 else(b2 if b==2 else(b3 if b==3 else b4))

    for _ in range(9):
        if (posB[_][0]-ds) < x < (posB[_][0]+ds) and (posB[_][1]-ds) < y < (posB[_][1]+ds):
            pos = _
            break
    pmb = b
    pmp = pos

def get_turnblock():
    global b1, b2, b3, b4, tb, td
    b = 0
    x = p.xcor()
    y = p.ycor()
    direc = 'n'
    arr = []
    if x < 0 and y < 0:
        b = 3
    elif x < 0 and y > 0:
        b = 1
    elif x > 0 and y > 0:
        b = 2
    elif x > 0 and y < 0:
        b = 4

    LorR = screen.textinput("Direction", "<- Left or Right ->")
    if LorR.startswith("l") or LorR.startswith("L"):
        direc = 'l'
    else:
        direc = 'r'
    td = direc
    tb = b

def print_message(message):
    w.clear()
    w.setpos(-149, 335)
    w.write(message, font=("Arial", 16, "normal"))


def play(x, y):
    global i, pmb, pmp, tb, td, winner, stage
    p.setpos(x, y)
    if stage == False and winner == 'none':
        if i==1:
            stage = True
            get_marblepos()
            place_marble(pmb, pmp, 'one')
            print_message("Player One Turn: Turn Block")
            i+=1
            stage = False
        elif i==2:
            stage = True
            get_turnblock()
            turn_block(tb, td)
            i+=1
            print_message("Player Two Turn: Place Marble")
            check_win('one')
            stage = False
        elif i==3:
            stage = True
            get_marblepos()
            place_marble(pmb, pmp, 'two')
            i+=1
            print_message("Player Two Turn: Turn Block")
            stage = False
        elif i==4:
            stage = True
            get_turnblock()
            turn_block(tb, td)
            i = 1
            print_message("Player One Turn: Place Marble")
            check_win('two')
            stage = False
    elif winner!='none':
        w.clear()
        w.setpos(-149, 335)
        w.write("THE WINNER IS " + winner.upper(), font=("Arial", 16, "normal"))
    

print_board()
update_block(1)
update_block(2)
update_block(3)
update_block(4)
turtle.onscreenclick(play)
turtle.listen()