from tkinter import *
import instaloader
import os
from tkinter import filedialog

root=Tk()
root.title("Instagram Photo Downloader")
root.geometry("350x350")

Label(root,text="Photo Downloader",font="Candara 18 bold").pack() #The heading
Label(root,text="Login Details: ",font="arial 13 bold").place(x=20,y=60)
Label(root,text="Username ",font="Candara 11").place(x=40,y=110) #The username used for logging in private accounts
Label(root,text="Password ",font="Candara 11").place(x=40,y=155) #The password for logging in
Label(root,text="Account ",font="Candara 11").place(x=40,y=200) #The photos of the account(username) you want to download

e1=Entry(root)
e1.place(x=150,y=110,width=155)
e2=Entry(root,show="*")
e2.place(x=150,y=155,width=155)
e3=Entry(root)
e3.place(x=150,y=200,width=155)

mod=instaloader.Instaloader()

def download(): #Function called for downloading the pictures
    user=str(e1.get())
    passw=str(e2.get())
    acc=str(e3.get())
    mod.login(user,passw) #Logging into the private account
    path=filedialog.askdirectory() #The path where the photos will be downloaded
    os.chdir(path) #Changing directory to the path
    mod.download_profile(acc,profile_pic_only=False)
    
def clear(): #Function called for clearing all the text fields
    e1.delete("0",END)
    e2.delete("0",END)
    e3.delete("0",END)
    
def exit(): #Function for exiting the window
    root.destroy()
    
b1=Button(root,text="Download",font="Arial 9",command=download) #Button for download command
b1.place(x=35,y=270,width=80)
b2=Button(root,text="Clear", font="Arial 9",command=clear) #Button for clearing all the fields
b2.place(x=135,y=270,width=80)
b3=Button(root,text="Exit",font="Arial 9",command=exit)
b3.place(x=235,y=270,width=80)

root.mainloop()

