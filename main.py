from tkinter import *
from tkinter import scrolledtext
import random

window = Tk()
window.title("Notepad")

def Savee():
    textt = Tet.get("1.0", "end-1c")
    extension = fileEx.get("1.0", "end-1c")
    name = Name.get("1.0", "end-1c")

    try:
        with open(f"{name}.{extension}", "x") as f:
            f.write(textt)
    except:
        with open(f"{name}({str(random.randrange(1,1000))}).{extension}", "x") as f:
            f.write(textt)
    

Tet = Text(window, height=200, width=200, font=("Times New Roman", 10))
Tet.place(x=0,y=55)


Save = Button(window, text="Save As", fg="Red", font=("Times New Roman", 15), command=Savee)
Save.place(x=0, y=0)

fileEx = Text(window, height=1, width=25, font=("Times New Roman", 14))
fileEx.place(x=180,y=0)

Name = Text(window, height=1, width=25, font=("Times New Roman", 14))
Name.place(x=180, y=27)

window.attributes('-fullscreen', True)
window.mainloop()