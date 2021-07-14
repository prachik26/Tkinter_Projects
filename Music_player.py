from tkinter import *
from tkinter import filedialog
import os
import pygame
import tkinter.messagebox

nw1=Tk()
nw1.title("Discover Music")
nw1.geometry("697x250+300+220")
nw1.resizable(False,False)

pygame.init()
#Initiating Pygame Mixer
pygame.mixer.init()
#Declaring track Variable
track=StringVar()
#Declaring Status Variable
status = StringVar()

#For playing,pausing and stopping of the song
def play():
    try:
        # Displaying Selected Song title
        track.set(playlist.get(ACTIVE))
        # Loading Selected Song
        pygame.mixer.music.load(playlist.get(ACTIVE))
    except:
        tkinter.messagebox.showerror("Error","Cannot play any song, not selected")
        pass
    
    track.set(playlist.get(ACTIVE))
    pygame.mixer.music.load(playlist.get(ACTIVE))
    # Displaying Status
    status.set("-Playing")
    
    
    # Playing Selected Song
    pygame.mixer.music.set_volume(0.1)
    #print(pygame.mixer.music.get_volume())
    pygame.mixer.music.play(-1)
    pausebtn['text'] = "PAUSE"

def pause():
    # pause
    unpause = True
    if(unpause):
        # Displaying Status
        status.set("-Paused")
        pausebtn['text'] = "PAUSED"
        # Paused Song
        pygame.mixer.music.pause()
        unpause = False

def stop():
    status.set("-Stopped")
    
    # Stopped Song
    pygame.mixer.music.stop()

def openl():
    path = filedialog.askdirectory()
    #Changing Directory for fetching Songs    

    try:
        os.chdir(path)
    except:
        tkinter.messagebox.showerror("Error","You didn't select any folder")

    #Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    playlist.delete(0,END)
    for track in songtracks:
        if track.endswith('.mp3'):
            playlist.insert(END, track)

            
# For frame
track_frame = LabelFrame(nw1,text="Song Track",font=("times new roman",15,"bold"),bg="blue",fg="white",bd=5,relief=GROOVE)    
track_frame.place(x=0,y=0,width=400,height=100)
   
songtrack = Label(track_frame, textvariable=track,width=23, font=("times new roman",15,"bold"),bg="blue", fg="gold")
songtrack.place(x=0,y=10)

# Inserting Status Label
trackstatus = Label(track_frame, textvariable=status,width=10, font=("times new roman", 15, "bold"), bg="blue",fg="gold")
trackstatus.place(x=280,y=10)

# Creating Button Frame
buttonframe = LabelFrame(nw1, text="Control Panel", font=("times new roman", 15, "bold"), bg="blue",fg="white", bd=5, relief=GROOVE)
buttonframe.place(x=0, y=100, width=400, height=150)

# Inserting Play Button
playbtn = Button(buttonframe, text="PLAY", command=play, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
playbtn.place(x=20,y=15)

# Inserting Pause Button
pausebtn = Button(buttonframe, text="PAUSE", command=pause, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
pausebtn.place(x=150,y=15)

# Inserting Stop Button
stopbtn = Button(buttonframe, text="STOP", command=stop, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
stopbtn.place(x=280,y=15)

#Inserting Open Button
openbtn=Button(buttonframe, text="Open",command=openl, width=8, height=1,font=("times new roman", 14, "bold"), fg="navyblue", bg="gold")
openbtn.place(x=142,y=70)

#Creating Playlist Frame
songsframe = LabelFrame(nw1, text="Song Playlist", font=("times new roman", 15, "bold"), bg="blue",fg="white", bd=5, relief=GROOVE)
songsframe.place(x=400, y=0, width=300, height=250)

#Inserting scrollbar
scrol_y=Scrollbar(songsframe, orient=VERTICAL)

#Inserting Playlist listbox
playlist=Listbox(songsframe,yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=("times new roman", 12, "bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

#Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)


nw1.mainloop()
