from cmath import sqrt
from PIL import Image, ImageTk
import tkinter as tk
import pyautogui as pt

# Get Screen Size
WIDTH, HEIGHT = pt.size()

# Create TK
root = tk.Tk()
# Set background color to black.
root.configure(bg='black')
# Make all black color transparent.
root.wm_attributes('-transparentcolor', 'black')
# Always on the front.
root.wm_attributes('-topmost', 1)
# Full Screen
root.wm_attributes('-fullscreen', 1)

# Read image and resize
img = ImageTk.PhotoImage(Image.open(".\YellowBean.png").resize(size=(100, 100)))

# Create button 1 and place it in the center of the screen
pX, pY = WIDTH/2-50, HEIGHT/2-50
button1 = tk.Button(root, image=img, bg='black', border=0,
                    activebackground='black')
button1.place(x=pX, y=pY)

# Create buttons
button2 = tk.Button(root, image=img, bg='black',
                    border=0, activebackground='black')

button3 = tk.Button(root, image=img, bg='black',
                    border=0, activebackground='black')

button4 = tk.Button(root, image=img, bg='black',
                    border=0, activebackground='black')

button5 = tk.Button(root, image=img, bg='black',
                    border=0, activebackground='black')


def relativePos(x, y):  # Get normalized vector from button 1 to mouse position
    mouseX, mouseY = pt.position()
    x, y = pX+50, pY+50
    distance = sqrt((mouseX-x)**2+(mouseY-y)**2).real
    if distance == 0:  # Avoid distance==0
        distance = 1
    nVector = (mouseX-x)/distance, (mouseY-y)/distance
    return nVector


def setPos():  # Set buttons position
    x, y = relativePos(pX, pY)
    button2.place(x=pX+x*300, y=pY+y*300)
    button3.place(x=pX-x*300, y=pY-y*300)
    button4.place(x=pX+y*300, y=pY-x*300)
    button5.place(x=pX-y*300, y=pY+x*300)
    # Update the image position every 1 ms
    root.after(1, setPos)


def checkActive(button):  # Check if button1 is active.
    if button['state'] == 'active':
        return 1

    else:
        return 0


# Initialize states for movePos()
clicked = False
vector = (0, 0)


def movePos(button):
    # Use global variables.
    global pX, pY, clicked, vector

    if checkActive(button=button) and clicked == 0:
        mouseX, mouseY = pt.position()
        vector = (mouseX-pX, mouseY-pY)
        clicked = 1
    elif not checkActive(button=button):
        clicked = 0

    if clicked == 1:
        mouseX, mouseY = pt.position()
        pX, pY = mouseX-vector[0], mouseY-vector[1]
        button1.place(x=pX, y=pY)

    root.after(1, lambda: movePos(button))


# Main
setPos()
movePos(button=button1)

root.mainloop()
