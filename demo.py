#!/usr/bin/python3

from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Decryptor")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        self.quitButton = Button(self, text="Press Me", command=self.showText())

        # placing the button on my window
        self.quitButton.place(x=150, y=200)

    def pressed(self):
        self.quitButton["text"] = 'pressed'

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

if __name__ == '__main__':

    root = Tk()

    # size of the window
    root.geometry("400x300")

    app = Window(root)
    root.mainloop()