from tkinter import *

State=0

def Test(event):
    global State
    if State==1:
        winbtntest.config(image=winbtn0)
        winbtntestdirection.set("Inactively")
        State=0

    else:
        winbtntest.config(image=winbtn1)
        winbtntestdirection.set("Active")
        State=1

app=Tk()

winbtn0=PhotoImage(file="b3.png")
winbtn1=PhotoImage(file="b1.png")

winbtntestdirection=StringVar()
winbtntestdirection.set("Inactively")
winbtntestdirectionb1=Label(app,font="Consoles 12",textvariable=winbtntestdirection)
winbtntestdirectionb1.pack()

winbtntest=Label(app,image=winbtn0)
winbtntest.bind("<Button-1>",Test)
winbtntest.pack()

app.title("BUtton test")
app.geometry("500x700")
app.resizable(0,0)
app.mainloop()
