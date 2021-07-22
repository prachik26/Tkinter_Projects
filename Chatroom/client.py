import socket
import threading
from tkinter import * 

PORT=51268
SERVER="192.168.56.1"
ADDRESS=(SERVER,PORT)
FORMAT="utf-8"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)

class chatbox:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        
        #Creating a Label
        self.label=Label(self.login,text="Please login to continue",justify=CENTER,font="Arial 14 bold")
        self.label.place(relheight=0.15,relx=0.2,rely=0.07)

        #Creating a Label
        self.labelName=Label(self.login,text="Name: ",font="Arial 12")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)

        #Creating a Entry box
        self.entryName=Entry(self.login,font="Arial 14")
        self.entryName.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)

        #Set the focus on the cursor
        self.entryName.focus()

        #Create a Continue button
        self.go=Button(self.login,text="CONTINUE",font="Arial 14 bold",command=lambda: self.toChatWindow(self.entryName.get()))
        self.go.place(relx=0.4,rely=0.55)
        self.Window.mainloop()

    def toChatWindow(self,name):
        self.login.destroy()
        self.layout(name)

        rcv=threading.Thread(target=self.recieve)
        rcv.start()

    def layout(self,name):
        self.name=name
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,height=False)
        self.Window.configure(width=470,height=550,bg="#17202A")
        
        self.labelHead=Label(self.Window,bg="#17202A",fg="#EAECEE",text=self.name,font="helvetica 13 bold",pady=5)
        self.labelHead.place(relwidth=1)
        
        self.line=Label(self.Window,width=450,bg="#ABB2B9")
        self.line.place(relwidth=1,rely=0.07,relheight=0.012)

        self.textCons=Text(self.Window,width=20,height=2,bg="#17202A",fg="#EAECEE",font="Helvetica 14",padx=5,pady=5)
        self.textCons.place(relheight=0.745,relwidth=1,rely=0.08)

        self.labelBottom=Label(self.Window,bg="#ABB2B9",height=80)
        self.labelBottom.place(relwidth=1,rely=0.825)

        self.entryMsg=Entry(self.labelBottom,bg="#2C3E50",fg="#EAECEE",font="Helvetica 13")
        self.entryMsg.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.entryMsg.focus()

        self.buttonMsg=Button(self.labelBottom,text="Send",font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda:self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
        self.textCons.config(cursor="arrow")

        #Creating a srcoll bar
        scrollbar=Scrollbar(self.textCons)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=DISABLED)

    #function to start the thread for sending messages
    def sendButton(self,msg):
        self.textCons.config(state=DISABLED)
        self.msg=msg
        self.entryMsg.delete(0,END)
        snd=threading.Thread(target=self.sendMessage)
        snd.start()

    #function to recieve messages
    def recieve(self):
        while True:
            try:
                message=client.recv(1024).decode(FORMAT)
                if message=="NAME":
                    client.send(self.name.encode(FORMAT))
                else:
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END,message+"\n\n")
                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                print("An error occured!")
                client.close()
                break
    
    #function to send messages
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message=(f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

g=chatbox()