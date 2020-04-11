from tkinter import *
from PIL import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_winsdow()

    def init_window(self):

        self.master.tittle("GUI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = "Save")
        file.add_(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)

        edit = Menu(menu)
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showTxt)
        menu.add_cascada(label = "Edit", menu = edit)
        
    def showImg(self):
        load = Image.open("pic.png")
        render = imageTK.PhotoImagine(load)

        img = Label(self, Image = render)
        img.image = render
        img.place(x=0,y=0)
