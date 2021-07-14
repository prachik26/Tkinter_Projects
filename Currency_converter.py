from tkinter import * #Import whole module


root=Tk()  #Create application window
root.title("Currency Converter")   #Add title to the window
root.geometry("450x300")   #Give geometry
root.configure(bg="yellow")   #Apply background color to window

#Creating Labels
Label(root,text="Currency Converter",font="Times 17 bold",bg="yellow").place(x=120,y=10)
Label(root,text="Amount to convert ",font="Helvetica 12 bold",bg="yellow").place(x=10, y=60)
Label(root,text="Conversion rate ",font="Helvetica 12 bold",bg="yellow").place(x=10, y=100)
Label(root,text="Converted amount ",font="Helvetica 12 bold",bg="yellow").place(x=10, y=140)

#Creating entry functions
amt_convert=IntVar()
amt_convert.set("")
Entry(root,textvariable=amt_convert).place(x=190,y=60)

cversion_rate=DoubleVar()
cversion_rate.set("")
Entry(root,textvariable=cversion_rate).place(x=190,y=100)

cnverted_amt=StringVar()
l1=Label(root,textvariable=cnverted_amt,bg="yellow",font="Helvetica 12 bold").place(x=190,y=140)

#Definind the function of buttons(commands)
def Converted():
    a=float(cversion_rate.get())
    b=amt_convert.get()
    cnverted_amt=a*b
    return format(cnverted_amt,'10.2f')
    
    #cnverted_amt.set(format(cnverted_amt,'10.2f'))

def Clear():
    amt_convert.set("")
    cversion_rate.set("")
    cnverted_amt.set("")
    
#Create buttons :convert and clear
b1=Button(root,text="Convert",fg="white",bg="blue",font="Helvetica 12 bold",command=lambda: cnverted_amt.set(Converted()))
b1.place(x=170,y=190)

b2=Button(root,text="Clear",fg="white",bg="blue",font="Helvetica 12 bold",command=Clear)
b2.place(x=270,y=190,width=80)

root.mainloop()
