#button with event handling
from tkinter import *
def clickFun(event):
    print(f"you clicked at position ({event.x},{event.y})")
    b1.place(x=300,y=200)
root=Tk()
root.title("Event in Tkinter")
root.geometry("1000x800")
b1=Button(root,text="Click me")
b1.pack()
b1.bind('<Button-1>',clickFun)
b1.bind('Double-Button-1>',quit)
root.mainloop()
