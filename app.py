from customtkinter import *
from tkinter import *
import pyqrcode

class App(CTk):
    def __init__(self):
        super().__init__()
        self.main()
        
    def main(self):
        self.title("QR Code Generator")
        self.geometry('450x550')
        self.lbl = CTkLabel(self , text = 'QR Code Generator' , font = ('comic sans ms',20,'bold'))
        self.lbl.pack()
        self.user_input = StringVar()
        self.entry = CTkEntry(self , font = ('ariel',15) , width=350 
                   , corner_radius=10,textvariable=self.user_input)
        self.entry.place(x = 47 , y = 100)
        self.btn = CTkButton(self , text = 'Generate' , corner_radius=10 ,command = self.show)
        self.btn.place(x=150 , y = 150)

       
    def show(self):
        self.imlbl = False
        code = pyqrcode.create(self.user_input.get())

        img  = BitmapImage(data=code.xbm(scale = 3))
        self.imlbl = CTkLabel(self , text="",image=img )
        self.imlbl.place(x = 100 , y = 200)
        

if __name__ =='__main__':
    app = App()
    app.mainloop()