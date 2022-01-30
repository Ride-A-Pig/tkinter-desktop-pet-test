import tkinter as tk
import pyautogui as pt
import random

# Get main screen resolution
WIDTH, HEIGHT = pt.size()
# Height of your task bar.
taskbarHeight = 40
# Gifs' width and height.
imgWidth, imgHeight = 500, 370
# The initial position of the window.
posX, posY = int(WIDTH/2-imgWidth/2), 0

# Create TK.
root = tk.Tk()
# Set window's size and position
root.geometry(str(int(imgWidth))+'x'+str(int(imgHeight))+'+' +
              str(posX)+'+'+str(posY))
root.overrideredirect(1)
# Set background color to black.
root.configure(bg='black')
# Hide all black colors (including gifs and all components)
root.wm_attributes('-transparentcolor', 'black')
# Always on the top.
root.wm_attributes('-topmost', 1)

# Read images.
idleRight = [tk.PhotoImage(file='./Gif/IdleRight.gif',
                           format='gif -index %i' % (i)) for i in range(4)]
idleLeft = [tk.PhotoImage(file='./Gif/IdleLeft.gif',
                          format='gif -index %i' % (i)) for i in range(4)]
runRight = [tk.PhotoImage(file='./Gif/RunRight.gif',
                          format='gif -index %i' % (i)) for i in range(6)]
runLeft = [tk.PhotoImage(file='./Gif/RunLeft.gif',
                         format='gif -index %i' % (i)) for i in range(6)]
fall = [tk.PhotoImage(file='./Gif/Fall.gif',
                      format='gif -index %i' % (i)) for i in range(2)]

# Set status dictionary.
status = {0: fall,
          1: idleRight,
          2: idleLeft,
          3: runRight,
          4: runLeft}
# Initialize current status
status_num = 0

# Create label object
player = tk.Label(root, image=idleLeft[0],
                  bg='black', bd=0)


def changeStatus():  # Change the status of the character.
    global status_num
    status_num = random.randint(1, 4)
    # Loop every random ms.
    root.after(random.randint(1000, 5000), changeStatus)


def falling():  # Falling status. It should in front of other functions.
    global status_num, posX, posY
    # Change status if character is falling
    if root.winfo_y()+imgHeight < HEIGHT-taskbarHeight:
        status_num = 0
        posY += 1
        root.geometry(str(int(imgWidth))+'x'+str(int(imgHeight))+'+' +
                      str(posX)+'+'+str(posY))
    # On the ground
    elif root.winfo_y()+imgHeight >= HEIGHT-taskbarHeight and status_num == 0:
        status_num = 1
    root.after(1, falling)


def moving():  # Moving the window based on character's status.
    global status_num, posX
    if status_num == 3 and root.winfo_x()+imgWidth-100 < WIDTH:
        posX += 1
        root.geometry(str(int(imgWidth))+'x'+str(int(imgHeight))+'+' +
                      str(posX)+'+'+str(posY))
    elif status_num == 3 and root.winfo_x()+imgWidth-100 >= WIDTH:
        status_num = 1

    if status_num == 4 and root.winfo_x()+100 > 0:
        posX -= 1
        root.geometry(str(int(imgWidth))+'x'+str(int(imgHeight))+'+' +
                      str(posX)+'+'+str(posY))
    elif status_num == 4 and root.winfo_x()+100 <= 0:
        status_num = 2
    root.after(3, moving)


def Anim(num, rate, character): # Make animations work.
    if num < len(status[status_num])-1:
        num += 1
    else:
        num = 0
    character = tk.Label(root, image=status[status_num][num],
                         bg='black', bd=0)
    character.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.after(rate, lambda: Anim(num, rate, character))


changeStatus()
falling()
moving()
Anim(0, 150, player)
root.mainloop()
