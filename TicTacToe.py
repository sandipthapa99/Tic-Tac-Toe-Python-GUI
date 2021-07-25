# Python program to create a GUI Tic Tac TOe

# Importing Tkinter module
from tkinter import *
import tkinter.messagebox

# Driver code
if __name__ == '__main__':
    bgcolor = '#282C35'

# ===========================================================================================================
    # creating GUI window
    root = Tk()

    # window title
    root.title("Tic Tac Toe")

    # window size
    root.geometry("1100x500")
    # root.resizable(0,0)
# ===========================================================================================================
    # Creating Frames for the widgets
    MainFrame = Frame(root, bg=bgcolor, bd=10, padx=2, pady=2, width=1350, height=600, relief=RIDGE)
    MainFrame.grid(row=0,column=0)

    LeftFrame = Frame(MainFrame, bg=bgcolor, bd=10, padx=10, pady=2, width=750, height=500, relief=RIDGE)
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(MainFrame, bg=bgcolor, bd=10, padx=20, pady=2, width=560, height=500, relief=RIDGE)
    RightFrame.pack(side=RIGHT)

    RightFrame1 = Frame(RightFrame, bg=bgcolor, bd=10, padx=10, pady=2, width=560, height=200, relief=RIDGE)
    RightFrame1.grid(row=0,column=0,padx=6,pady=20)

    RightFrame2 = Frame(RightFrame, bg=bgcolor, bd=10, padx=10, pady=2, width=560, height=400, relief=RIDGE)
    RightFrame2.grid(row=1,column=0,padx=6,pady=20)
# ===========================================================================================================
    # Variables
    

    root.mainloop()