from tkinter import filedialog
from tkinter import*
import pygame
import os

window=Tk()
window.title("Music Player")
window.geometry("500x500")

pygame.mixer.init()

menubar=Menu(window)
window.config(menu=menubar)

songs=[]
cur_song=""
paused=False
 
def load_music():
    global curr_song
    window.directory=filedialog.askdirectory()

    for song in os.listdir(window.directory):
        name , ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
    for song in songs:
        songlist.insert("end", song) 
        songlist.selection_set(0)     
        curr_song=songs[songlist.curselection()[0]]

org_menu=Menu(menubar, tearoff=False)
org_menu.add_command(label="Select Songs Folder", command=load_music)
menubar.add_cascade(label="Click Me", menu=org_menu)
 



def play_music():
    global curr_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory, curr_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False

def pause_music():
    global pause   
    pygame.mixer.music.pause()
    paused=True

def next_music():
    global curr_song, paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(curr_song)+1)
        curr_song=songs[songlist.curselection()[0]]

        play_music()
    except:
          pass

def pre_music():
    global curr_song, paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(curr_song)-1)
        curr_song=songs[songlist.curselection()[0]]
        play_music()
    except:
          pass



songlist=Listbox(window, bg="Black", fg="white", width=100, height=15)
songlist.pack()

play_button_img=PhotoImage(file="play.png")
pause_button_img=PhotoImage(file="pause.png")
next_button_img=PhotoImage(file="next.png")
prev_button_img=PhotoImage(file="previous.png")

con_frame=Frame(window)
con_frame.pack()

play_button=Button(con_frame, image=play_button_img,borderwidth=0, command=play_music)
pause_button=Button(con_frame, image=pause_button_img, borderwidth=0, command=pause_music)
next_button=Button(con_frame, image=next_button_img, borderwidth=0, command=next_music)
prev_button=Button(con_frame, image=prev_button_img, borderwidth=0,command=pre_music)



play_button.grid(row=0, column=2, padx=7, pady=10)
pause_button.grid(row=0,column=1, padx=7, pady=10)
next_button.grid(row=0,column=3, padx=7, pady=10)
prev_button.grid(row=0,column=0, padx=7, pady=10)



window.mainloop()