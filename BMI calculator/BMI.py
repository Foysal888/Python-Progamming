from tkinter import *
from tkinter import ttk
import tkinter.messagebox







class firstpage:
    def __init__(self,root):
        self.root=root
        self.root.title("BMI Calculation")
        self.root.geometry("500x550")
        self.root.config(bg="#0a3d62")

        self.photo = PhotoImage(file="pic1.png",)
        self.photo1 = PhotoImage(file="q.png", )


        labelforphoto = Label(self.root, text="BMI",image=self.photo,anchor=W,bg="#0a3d62")
        labelforphoto.pack(fill=X)

        b1=Button(self.root,text="Start",bd=5,command=self.open,font=("Old English Text MT",20,"bold"),bg="#60a3bc",relief=RAISED)
        b1.pack(fill=X)



        labelforphoto1 = Label(self.root, text="BMI", image=self.photo1, bg="#0a3d62")
        labelforphoto1.pack(fill=BOTH)



        linfo=Label(self.root,bd=3,bg="#7f8c8d",font=("Comic Sans MS",12,"bold"),relief=RIDGE,text="\n Commonly accepted BMI ranges are--  \n \n Underweight==(Under 18.5 kg/m2), \n Normal Weight==(18.5 to 25), \n Overweight==(25 to 30), \n Obese==(Over 30).",)
        linfo.pack(fill=BOTH,side=BOTTOM)
        l1=Label(self.root,text="Body Mess Index(BMI)",relief=RIDGE,bd=1,font=("Comic Sans MS",12,"bold"),bg="#079992")
        l1.pack(fill=X,side=BOTTOM)

    def open(self):
        self.app=bmi (Toplevel())







class bmi:
    def __init__(self,form):
        self.form=form
        self.form.title("BMI calculation")
        self.form.geometry("700x600")



        def about_bmi():
            tkinter.messagebox.showinfo("What is BMI?","Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is universally expressed in units of kg/m2, resulting from mass in kilograms and height in metres. \n \n Commonly accepted BMI ranges are--  \n \n Underweight (under 18.5 kg/m2), \n Normal weight (18.5 to 25), \n Overweight (25 to 30), and \n Obese (over 30).")

        manubar = Menu(form,bg="blue")
        form.config(menu=manubar)
        subMenu = Menu(manubar,tearoff=0,font=("Comic Sans MS",11,"bold"))

        manubar.add_cascade(label="File", men=subMenu,)
        subMenu.add_command(label="About BMI",command=about_bmi)
        subMenu.add_command(label="Exit",)



        height1=StringVar()
        height2=StringVar()
        weight1=StringVar()
        weight2=StringVar()
        result1=StringVar()
        result2=StringVar()

        framwhy=Frame(self.form)
        framwhy.pack(expand=3,fill='both')

        mygreen = "#7f8c8d"
        myred = "#badc58"

        style = ttk.Style()

        style.theme_create("yummy", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [5, 1], "background": myred},
                              "map": {"background": [("selected", mygreen)],
                                      "expand": [("selected", [1, 1, 1, 0])]}}})

        style.theme_use("yummy")

        forr=ttk.Notebook(framwhy)

        tab1=Frame(forr,bg="#34495e")
        forr.add(tab1, text="Standard", )

        tab2=Frame(forr,bg="#60a3bc")
        forr.add(tab2,text="Normal")
        forr.pack(expand=3,fill='both')

        L1=Label(tab1,text="Standard Format Of BMI Calculation",bg="gray",anchor=E,font=("Comic Sans MS",13,"bold"))
        L1.pack(fill=X)
        mainframe=Frame(tab1,bg="blue")
        mainframe.pack()
        frame1 = Frame(mainframe,)
        frame1.pack(fill=X)

        labe1=Label(frame1,text="Enter Height In Feet:",bd=5,fg="#2d3436",bg="#b2bec3",font=("Comic Sans MS",15,"bold"))
        labe1.grid(row=0,column=0,sticky="we")
        entry1=Entry(frame1,textvariable=height1,bd=10,fg="#2d3436",bg="#b2bec3",font=("Comic Sans MS",12,"bold"))
        entry1.grid(row=0,column=1)

        labe2 = Label(frame1, text="Enter Weight In KG:",bd=5,fg="#2d3436",bg="#b2bec3",font=("Comic Sans MS",15,"bold"))
        labe2.grid(row=1, column=0,sticky="we")
        entry2 = Entry(frame1, textvariable=weight1,bd=10,fg="#2d3436",bg="#b2bec3",font=("Comic Sans MS",12,"bold"))
        entry2.grid(row=1, column=1)

        labelresult=Label(tab1,text="Welcome To BMI Calculator",font=("Algerian", 16, "bold"),anchor=W,bg="#82ccdd",relief=FLAT )
        labelresult.pack(side=BOTTOM,fill=X)
        suggestion = Label(tab1, text="", font=("Algerian", 18, "bold"), anchor=W, bg="#34495e")
        suggestion.pack(side=BOTTOM, fill=X)
        resultshow = Entry(tab1, textvariable=result1, justify='center', bd=0, fg="Black",font=("Comic Sans MS", 30, "bold"), bg="#34495e")
        resultshow.pack(side=BOTTOM,fill=X)

        pic1=PhotoImage(file="pic1.png")

        def add1():
            try:
                if height1.get()!=0 :
                    h=float(height1.get())*0.3048
                    w=float(weight1.get())
                    r=w/(h**2)
                    result1.set("%.3f"%r)

                    if r<=18.5:
                        lr=18.5*(h**2)
                        ur=(h**2)*24.9
                        suggestion['text']=("Your Weight should be   "+str("%.2f"%lr)+"  KG " +"    to    "+str("%.2f"%ur)+"  KG")
                        suggestion['relief']=RIDGE
                        suggestion['bg']='#bdc3c7'
                        labelresult['fg']="#d35400"
                        labelresult['text'] = ("You are underweight.")

                    elif 18.5<= r <=24.9:
                        lr = (h ** 2) * 18.5
                        ur = (h ** 2) * 24.9
                        suggestion['text'] = ("Your Weight should be   " + str("%.2f" % lr) + "  KG " + "    to    " + str(
                            "%.2f" % ur) + "  KG")
                        suggestion['relief'] = RIDGE
                        suggestion['bg'] = '#bdc3c7'
                        labelresult['fg'] = "#d35400"
                        labelresult['text'] = "You are OK!!"
                        labelresult['fg'] = "green"
                    elif 25<=r<=29.9:
                        lr = (h ** 2) * 18.5
                        ur = (h ** 2) * 24.9
                        suggestion['text'] = ("Your Weight should be   " + str("%.2f" % lr) + "  KG " + "    to    " + str(
                            "%.2f" % ur) + "  KG")
                        suggestion['relief'] = RIDGE
                        suggestion['bg'] = '#bdc3c7'
                        labelresult['fg'] = "#d35400"
                        labelresult["text"] = "You are Overweight "
                        labelresult['fg'] = "#e55039"
                    else:
                        lr = (h ** 2) * 18.5
                        ur = (h ** 2) * 24.9
                        suggestion['text'] = ("Your Weight should be   " + str("%.2f" % lr) + "  KG " + "    to    " + str(
                            "%.2f" % ur) + "  KG")
                        suggestion['relief'] = RIDGE
                        suggestion['bg'] = '#bdc3c7'
                        labelresult['fg'] = "#d35400"
                        labelresult["text"] = "You are Vary Fat (Obesity) "
                        labelresult['fg'] = "#eb2f06"


            except:
                    tkinter.messagebox.showerror("Error","Please Enter All information")
        def clear():
            height1.set("")
            weight1.set("")
            result1.set("")
            labelresult['text']='Welcome to BMI-Calculator'
            suggestion['text']=""
            suggestion['bg']="#34495e"
            suggestion['relief']=FLAT



            tkinter.messagebox.showinfo("Reset","Data Reset")





        butt1=Button(tab1,text="B.M.I",command=add1,font=("Bernard MT Condensed",18,""),bg="#d63031")
        butt1.pack(fill=X)
        butt2=Button(tab1,text="Re-set",command=clear,font=("Bernard MT Condensed",18,""),bg="#ff7675")
        butt2.pack(fill=X)












        L2 = Label(tab2, text="Normal Format Of BMI Calculation", bg="#b8e994", anchor=E,font=("Comic Sans MS", 13, "bold"))
        L2.pack(fill=X)

        mainframe2 = Frame(tab2, bg="#60a3bc")
        mainframe2.pack()
        frame2 = Frame(mainframe2, )
        frame2.pack(fill=X)

        labe1 = Label(frame2, text="Enter Height In Feet:", bd=10, fg="#2d3436", bg="#b2bec3",font=("Comic Sans MS", 15, "bold"))
        labe1.grid(row=0, column=0, sticky="we")
        entry1 = Entry(frame2, textvariable=height2, bd=10, fg="#2d3436", bg="#b2bec3",font=("Comic Sans MS", 12, "bold"))
        entry1.grid(row=0, column=1)

        labe2 = Label(frame2, text="Enter Weight In Pound:", bd=10, fg="#2d3436", bg="#b2bec3",font=("Comic Sans MS", 15, "bold"))
        labe2.grid(row=1, column=0, sticky="we")
        entry2 = Entry(frame2, textvariable=weight2, bd=10, fg="#2d3436", bg="#b2bec3",font=("Comic Sans MS", 12, "bold"))
        entry2.grid(row=1, column=1)

        labelresult1 = Label(tab2, text="This is result", font=("Algerian", 16, "bold"), anchor=W, bg="#079992",relief=FLAT)
        labelresult1.pack(side=BOTTOM, fill=X)
        suggestion1 = Label(tab2, text="", font=("Algerian", 16, "bold"), anchor=W, bg="#60a3bc")
        suggestion1.pack(side=BOTTOM, fill=X)
        resultshow = Entry(tab2, textvariable=result2, justify='center', bd=0, fg="Black",font=("Comic Sans MS", 30, "bold"), bg="#60a3bc")
        resultshow.pack(side=BOTTOM, fill=X)



        def add2():
            try:
                if height2.get() != 0:
                    h = float(height2.get()) * 0.3048
                    w = float(weight2.get())*0.453592
                    r = w / (h ** 2)
                    result2.set("%.3f" % r)

                    if r <= 18.5:
                        lr = (18.5 * (h ** 2))*2.20462
                        ur = ((h ** 2) * 24.9)*2.20462
                        suggestion1['text'] = (
                                    "Your Weight should be   " + str("%.2f" % lr) + "  Pound " + "    to    " + str(
                                "%.2f" % ur) + "  Pound")
                        suggestion1['relief'] = RIDGE
                        suggestion1['bg'] = '#bdc3c7'
                        labelresult1['fg'] = "#d35400"
                        labelresult1['text'] = ("You are underweight.")

                    elif 18.5 <= r <= 24.9:
                        lr = ((h ** 2) * 18.5)*2.20462
                        ur = ((h ** 2) * 24.9)*2.20462
                        suggestion1['text'] = (
                                    "Your Weight should be   " + str("%.2f" % lr) + "  Pound " + "    to    " + str(
                                "%.2f" % ur) + "  Pound")
                        suggestion1['relief'] = RIDGE
                        suggestion1['bg'] = '#bdc3c7'
                        labelresult1['fg'] = "#d35400"
                        labelresult1['text'] = "You are OK"
                        labelresult1['fg'] = "#27ae60"
                    elif 25 <= r <= 29.9:
                        lr = ((h ** 2) * 18.5)*2.20462
                        ur = ((h ** 2) * 24.9)*2.20462
                        suggestion1['text'] = (
                                    "Your Weight should be   " + str("%.2f" % lr) + "  Pound " + "    to    " + str(
                                "%.2f" % ur) + "  Pound")
                        suggestion1['relief'] = RIDGE
                        suggestion1['bg'] = '#bdc3c7'
                        labelresult1['fg'] = "#d35400"
                        labelresult1["text"] = "You are Overweight "
                        labelresult1['fg'] = "#e55039"
                    else:
                        lr = ((h ** 2) * 18.5)*2.20462
                        ur = ((h ** 2) * 24.9)*2.20462
                        suggestion1['text'] = (
                                    "Your Weight should be   " + str("%.2f" % lr) + "  Pound " + "    to    " + str(
                                "%.2f" % ur) + "  Pound")
                        suggestion1['relief'] = RIDGE
                        suggestion1['bg'] = '#bdc3c7'
                        labelresult1['fg'] = "#d35400"
                        labelresult1["text"] = "You are Vary Fat (Obesity) "
                        labelresult1['fg'] = "#eb2f06"


            except:
                tkinter.messagebox.showerror("Error", "Please Enter All information")

        def clear2():
            height2.set("")
            weight2.set("")
            result2.set("")
            labelresult1['text'] = 'Welcome to BMI-Calculator'
            suggestion1['text'] = ""
            suggestion1['bg'] = "#60a3bc"
            suggestion1['relief'] = FLAT

        butt1 = Button(tab2, text="B.M.I", command=add2, font=("Bernard MT Condensed", 18, ""), bg="#0a3d62")
        butt1.pack(fill=X)
        butt2 = Button(tab2, text="Re-set", command=clear2, font=("Bernard MT Condensed", 18, ""), bg="#3c6382")
        butt2.pack(fill=X)


def main():
    root=Tk()
    app=firstpage(root)
    root.mainloop()

if __name__ == '__main__':
    main()
