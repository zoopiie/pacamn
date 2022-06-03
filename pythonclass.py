from tkinter import *
from threading import Timer
import keyboard
from random import *
from time import sleep
import copy

levelthree = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

leveltwo = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

levelone = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

leveltest = [[0 for i in range(25)] for j in range(15)]

width = 0
height = 0
point = 0
level = 1
cellsize = 50
x, y = 0, 0
matrix = 0
check = 0
timeghost = 1
refreshtime = 0.001
changepac = 0.03
multiplicator = 1
life = 3
x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0
y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
ghostbreak = 0
mvtcount = 0
invicible = 0
cheatingvar = 0
anticheatvar = 0
varpac = 0.04
aux1 = 0
cir = 10
playermode = 0


class Character:

    def get_new_coord(self, dir):
        if dir == 'up':
            y = self.y - 1
            x = self.x
        elif dir == 'down':
            y = self.y + 1
            x = self.x
        elif dir == 'left':
            y = self.y
            x = self.x - 1
        elif dir == 'right':
            y = self.y
            x = self.x + 1
        else:
            x = self.x
            y = self.y
        return x, y


    def can_move(new_x, new_y):
        if matrix[new_y][new_x] == 0 or matrix[new_y][new_x] == 2:
            return 1
        return 0
    
    can_move = staticmethod(can_move)

    def confrontation():
        if invicible == 0:
            if (pacman.x == Blinky.x and pacman.y == Blinky.y) or (pacman.x == Inky.x and pacman.y == Inky.y)\
                or (pacman.y == Clyde.y and pacman.x == Clyde.x) or (pacman.x == Pinky.x and pacman.y == Pinky.y):
                return 1
        return 0
    confrontation = staticmethod(confrontation)


class Ghost(Character):
    timeghost = 1

    def __init__(self, x, y, dir, name):
        Character.__init__(self)
        self.y = y
        self.x = x
        self.dir = dir
        self.name = name

        
    def move(self, dir):
        while True:
            randir = randint(0, 4)
            sleep(0.01)
            if randir == 1 and dir != 'down' and self.y > 0:
                self.dirtest('up')

            if randir == 2 and dir != 'up' and self.y < len(matrix) - 1:
                self.dirtest('down')

            if randir == 3 and dir != 'left' and self.x < len(matrix[0]) - 1:
                self.dirtest('right')

            if randir == 4 and dir != 'right' and self.x > 0:
                self.dirtest('left')
                            

    def nextlevelcoord(self, x, y):
        self.y = y
        self.x = x


    def ghostdisplay(self , new_x , new_y):
        can.delete("rect")
        can.create_rectangle(self.x * cellsize, self.y * cellsize, (self.x + 1) * cellsize,
                             (self.y + 1) * cellsize, fill='black', tags="rect")
        if matrix[new_y][new_x] == 2:
            create_circle((self.x * cellsize + cellsize / 2), (self.y * cellsize + cellsize / 2), cir, can)
        can.delete("image")
        can.create_image(new_x * cellsize + cellsize / 2, new_y * cellsize + cellsize / 2,
                         image=self.name, tags="image")


    def dirtest(self, dir):
        x, y = Character.get_new_coord(self, dir)
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            if Character.can_move(x, y) == 1:
                self.ghostdisplay(x, y)
                self.x = x
                self.y = y
                if ghostbreak == 0:
                    if Character.confrontation() == 1:
                        pacman.loselife()
                        if pacman.life == 0:
                            pacman.death()
                    Timer(timeghost, self.move, args=([dir])).start()


class Pacman(Character):


    def __init__(self):
        Character.__init__(self)
        self.x = 0
        self.y = 0
        self.life = 3
        self.mvtcount = 0
        self.point = 0

    def move(self, dir):
        if self.mvtcount == 4:
            Blinky.move('')
        if self.mvtcount == 6:
            Inky.move('')
        if self.mvtcount == 8:
            Pinky.move('')
        if self.mvtcount == 10:
            Clyde.move('')
        if self.mvtcount <= 12:
            self.mvtcount += 1
        if 0 <= self.x < width and 0 <= self.y < height:
            x, y = Character.get_new_coord(self, dir)
            if 0 <= x < width and 0 <= y < height:
                if Character.can_move(x, y) == 1:
                    old_x = self.x
                    old_y = self.y
                    self.x = x
                    self.y = y
                    if matrix[self.y][self.x] == 2 or matrix[self.y][self.x] == 0:
                        if 0 <= y < (len(matrix)) and 0 <= x < (len(matrix[0])):
                            if dir == 'up':
                                pm = pmup
                                pmo = pmopenup
                            if dir == 'down':
                                pm = pmdown
                                pmo = pmopendown
                            if dir == 'right':
                                pm = pmright
                                pmo = pmopenright
                            if dir == 'left':
                                pm = pmleft
                                pmo = pmopenleft
                            pacman.pacamandisplay(old_x, old_y, pm, pmo)
                            if matrix[self.y][self.x] == 2:
                                pacman.pointadd()
        if Character.confrontation() == 1:
            pacman.loselife()
            if pacman.life == 0:
                pacman.death()
        pacman.clearleververif()                       
        

    def pacamandisplay(self, old_x, old_y, pm, pmo):
        #can.delete("rectp")
        can.create_rectangle(old_x * cellsize, old_y * cellsize, (old_x + 1) * cellsize,
                             (old_y + 1) * cellsize, fill='black', tags="rectp")
        can.create_image(self.x * cellsize + cellsize / 2, self.y * cellsize + cellsize / 2, image=pm, tags='imagep')
        sleep(changepac)
        can.delete("imagep")
        sleep(refreshtime)
        can.create_image(self.x * cellsize + cellsize / 2, self.y * cellsize + cellsize / 2, image=pmo, tags='imagep')
        sleep(changepac)
        can.delete("imagep")
        sleep(refreshtime)
        can.create_image(self.x * cellsize + cellsize / 2, self.y * cellsize + cellsize / 2, image=pm, tags='imagep')
        sleep(changepac)
        can.delete("imagep")
        sleep(refreshtime)
        can.create_image(self.x * cellsize + cellsize / 2, self.y * cellsize + cellsize / 2, image=pmo, tags='imagep')
        sleep(changepac)
        
    
    def loselife(self):
        self.x = 0
        self.y = 0
        pacman.life = pacman.life - 1
        countlife.config(text="il vous reste {} vie".format(pacman.life))
        sleep(1)
        can.delete("rectp")
        can.create_rectangle(self.x * cellsize, self.y * cellsize, (self.x + 1) * cellsize, (self.y + 1) * cellsize,
                             fill='black', tags="rectp")
        can.delete("imagep")
        can.create_image(cellsize / 2, cellsize / 2, image=pmopenright, tags="imagep")
    
    
    def death(self):
        ghostbreak = 1
        victoryevent.config(text='defeat !!!!')
        defeatevent()
        
            
    def clearleververif(self):
        if matrix == check:
            victoryevent.config(text="next level")
            ghostbreak = 1
            sleep(4)
            victoryevent.config(text="")
            changelevel()
            
            
    def pointadd(self):
        self.point += multiplicator
        self.point = int(self.point)
        countpoint.config(text=self.point)
        matrix[self.y][self.x] = 0
        
        



def ghostbreaker():
    global ghostbreak
    ghostbreak = 1 - ghostbreak
    if ghostbreak == 0:
        Blinky.move('')
        Inky.move('')
        Pinky.move('')
        Clyde.move('')


def create_circle(x, y, r, canvasName):########### cest transmis
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvasName.create_oval(x0, y0, x1, y1, fill='yellow', tags='circle')


def init():########### cest transmis
    global width, height, matrix, check
    if level == 1:
        width = len(levelone[0])
        height = len(levelone)
        check = copy.deepcopy(levelone)
        print('level one ok')
        matrix = copy.deepcopy(levelone)
    if level == 2:
        width = len(leveltwo[0])
        height = len(leveltwo)
        matrix = copy.deepcopy(leveltwo)
        check = copy.deepcopy(leveltwo)
        print("level two ok")
    if level == 3:
        width = len(levelthree[0])
        height = len(levelthree)
        matrix = copy.deepcopy(levelthree)
        check = copy.deepcopy(levelthree)
        print("level three ok")


def create(matrix1):    ############ a moitié fait
    global matrix, check, multiplicator, level
    init()
    can.delete("all")
    multiplicator = ((level / 10) + 1) * 10
    matrix = matrix1
    if level != 1:
        Blinky.nextlevelcoord(len(matrix[0]) - 1, len(matrix) - 1)
        Inky.nextlevelcoord(len(matrix[0]) - 1, len(matrix) - 1)
        Pinky.nextlevelcoord(len(matrix[0]) - 1, len(matrix) - 1)
        Clyde.nextlevelcoord(len(matrix[0]) - 1, len(matrix) - 1)
    can.config(width=len(matrix1[0])*cellsize, height=len(matrix1)*cellsize)
    for i in range(len(matrix1[0])):
        for j in range(len(matrix1)):
            if matrix[j][i] == 1:
                can.create_rectangle(i * cellsize, j * cellsize, (i+1) * cellsize, (j+1) * cellsize, fill='#002eee')
            if matrix[j][i] == 0:
                can.create_rectangle(i * cellsize, j * cellsize, (i + 1) * cellsize, (j + 1) * cellsize, fill='black')
                create_circle((i*cellsize+cellsize/2), (j*cellsize+cellsize/2), cir, can)
    can.create_image(cellsize/2, cellsize/2, image=pmopenright, tags='imagep')
    matmodif()


def matmodif():     ########## cest fait
    global matrix, check
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                matrix[j][i] = 2
    matrix[0][0] = 0


def changelevel():      ########### cest fait
    global level, x, y, matrix, ghostbreak, mvtcount, timeghost
    Ghost.mvtcount = 0
    ghostbreak = 0
    level += 1
    Ghost.x, Ghost.y = 0, 0
    Pacman.x, Pacman.y = 0, 0
    if anticheatvar == 0:
        if level == 2:
            Ghost.timeghost = Ghost.timeghost - 0.1
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(leveltwo)
            create(leveltwo)
        if level == 3:
            Ghost.timeghost = 0.3
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(levelthree)
            create(levelthree)
        if level > 3:
            if Ghost.timeghost <= 0.2:
                Ghost.timeghost = Ghost.timeghost/2
            else:
                Ghost.timeghost = Ghost.timeghost - 0.1
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(levelthree)
            create(levelthree)
    else:
        defeatevent()


def inviciblemode():########### cest transmis
    global invicible, cheatingvar, pmup, pmleft, pmdown, pmright, \
        pmopenup, pmopendown, pmopenleft, pmopenright, anticheatvar
    invicible = 1 - invicible
    cheatingvar += 1
    if invicible == 1:
        pmopenright = chompright
        pmopendown = chompdown
        pmopenleft = chompleft
        pmopenup = chompup
        pmup = greycircle
        pmdown = greycircle
        pmleft = greycircle
        pmright = greycircle
    anticheatvar = 1
    if invicible == 0:
        pmopenright = pmopenright1
        pmopendown = pmopendown1
        pmopenleft = pmopenleft1
        pmopenup = pmopenup1
        pmup = pmup1
        pmdown = pmdown1
        pmleft = pmleft1
        pmright = pmright1


def tricheplus(): ########### cest transmis
    global anticheatvar

    anticheatvar = 0

def discret():########### cest transmis
    global cheatingvar
    cheatingvar = 0


def pointplus():########### cest transmis
    global point
    pacman.point = pacman.point + 1523


def morelive():########### cest transmis
    global life, cheatingvar, anticheatvar
    pacman.life += 1
    cheatingvar += 1
    countlife.config(text="il te reste {} vie".format(pacman.life))
    anticheatvar = 1


def defeatevent():########### cest transmis
    can.delete('all')
    root.geometry('0x0')
    can.config(width=0, height=0)
    rt = Toplevel()
    rt.config(bg='black')
    score = "%s%s" % ("ton score est de : ", point)
    lab = Label(rt, text=score, fg='#00eeee', bg='black', font=('', 40, 'bold')).pack()
    if cheatingvar != 0:
        label = Label(rt, text='je sais que tu as triché....', fg='#00eeee', bg='black', font=('', 20, 'bold')).pack()


def test():
    create(leveltest)

root = Tk()
root.title('pacman')
root.config(bg='black')


greycircle = PhotoImage(file='greycircle.png')
chompright = PhotoImage(file='chompdroite.png')
chompleft= PhotoImage(file='chompgauche.png')
chompdown = PhotoImage(file='chompbas.png')
chompup = PhotoImage(file='chomphaut.png')
blinky = PhotoImage(file='blinky2.png')
inky = PhotoImage(file='inky2.png')
pinky = PhotoImage(file='pinky2.png')
clyde = PhotoImage(file='clyde2.png')
pmopenup = PhotoImage(file='pacmanopenhaut.png')
pmopendown = PhotoImage(file='pacmanopenbas.png')
pmopenleft = PhotoImage(file='pacmanopengauche.png')
pmopenright = PhotoImage(file='pacmanopendroite.png')
pmup = PhotoImage(file='pacmanhaut.png')
pmdown = PhotoImage(file='pacmanbas.png')
pmleft = PhotoImage(file='pacmangauche.png')
pmright = PhotoImage(file='pacmandroite.png')
pmopenup1 = PhotoImage(file='pacmanopenhaut.png')
pmopendown1 = PhotoImage(file='pacmanopenbas.png')
pmopenleft1 = PhotoImage(file='pacmanopengauche.png')
pmopenright1 = PhotoImage(file='pacmanopendroite.png')
pmup1 = PhotoImage(file='pacmanhaut.png')
pmdown1 = PhotoImage(file='pacmanbas.png')
pmleft1 = PhotoImage(file='pacmangauche.png')
pmright1 = PhotoImage(file='pacmandroite.png')


leveldisplay = "%s%s" % ("level ", level)

countlevel = Label(root, text=leveldisplay, bg='black', fg='#00eeee', font=30)
countlevel.pack(side=LEFT, anchor=NW)
countpoint = Label(root, text=point, bg='black', fg='#00eeee', font=30)
countpoint.pack(side=TOP, anchor=N)
victoryevent = Label(root, text="", bg='black', fg='#00eeee', font=30)
victoryevent.pack(side=RIGHT, anchor=NW)
countlife = Label(root, text="il te reste {} vie".format(life), bg='black', fg='#00eeee', font=30)
countlife.pack(side=LEFT, anchor=NW)

can = Canvas(root, width=0, height=0, bg='black')
can.pack(side=LEFT)


create(levelone)

Blinky = Ghost((len(matrix[0]) - 1), (len(matrix) - 1), '', blinky)
Inky = Ghost((len(matrix[0]) - 1), (len(matrix) - 1), '', inky)
Pinky = Ghost((len(matrix[0]) - 1), (len(matrix) - 1), '', pinky)
Clyde = Ghost((len(matrix[0]) - 1), (len(matrix) - 1), '', clyde)
pacman = Pacman()

keyboard.on_press_key("space", lambda _: changelevel())
keyboard.on_press_key("enter", lambda _: inviciblemode())
keyboard.on_press_key("up", lambda _: pacman.move('up'))
keyboard.on_press_key("left", lambda _: pacman.move('left'))
keyboard.on_press_key("down", lambda _: pacman.move('down'))
keyboard.on_press_key("right", lambda _: pacman.move('right'))
keyboard.on_press_key("0", lambda _: ghostbreaker())
keyboard.on_press_key("tab", lambda _: morelive())
keyboard.on_press_key("ctrl", lambda _: defeatevent())
keyboard.on_press_key("F1", lambda _: tricheplus())
keyboard.on_press_key("F3", lambda _: pointplus())
keyboard.on_press_key("F2", lambda _: discret())
keyboard.on_press_key("F12", lambda _: test())


root.mainloop()
