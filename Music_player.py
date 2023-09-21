import tkinter as tk
import fnmatch
import os
from pygame import mixer


canvas =tk.Tk()
canvas.title("music player")
canvas.geometry("600x450")
canvas.config(bg="black")

rootpath = ".\playlist"
pattern = "*.mp3"

mixer.init()


prev_image=tk.PhotoImage(file="prev_img.png")
stop_image=tk.PhotoImage(file="stop_img.png")
play_image=tk.PhotoImage(file="play_img.png")
pause_image=tk.PhotoImage(file="pause_img.png")
next_image=tk.PhotoImage(file="next_img.png")
next_song='x'
def select():
    global t,next_song
    try:
     tes=next_song[0]
     label.config(text= listbox.get("anchor"))
     mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    except:
        try:
         next_song=listbox.curselection()
         next_song=next_song[0]
        except:
            next_song=0
        next_song_name=listbox.get(next_song)
        label.config(text= next_song_name)
        mixer.music.load(rootpath + "\\" + next_song_name)
        listbox.select_set(next_song)
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    global t,next_song
    try:
     next_song=listbox.curselection()
     next_song=next_song[0]+1
     if next_song==t:
        next_song=0
    except:
        next_song=0
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0,"end")
    listbox.activate(next_song)
    listbox.selection_set(next_song)

def play_prev():
    global t,next_song
    try:
     next_song=listbox.curselection()
     next_song=next_song[0]-1
     if next_song==-1:
        next_song=t-1
    except:
        next_song=0
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0,"end")
    listbox.activate(next_song)
    listbox.selection_set(next_song)
def pause_song():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"




listbox = tk.Listbox(canvas,bg="cyan",width=100)
listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text="",bg="black",fg="yellow")
label.pack(pady=15)

top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor="center")

prevButton = tk.Button(canvas,text="prev",image= prev_image,bg='black',borderwidth=0,command=play_prev)
prevButton.pack(pady=10,padx=10,in_=top,side="left")

stopButton = tk.Button(canvas,text="stop",image= stop_image,bg='black',borderwidth=0,command=stop)
stopButton.pack(pady=10,padx=10,in_=top,side="left")

playButton = tk.Button(canvas,text="play",image= play_image,bg='black',borderwidth=0,command=select)
playButton.pack(pady=10,padx=10,in_=top,side="left")

pauseButton = tk.Button(canvas,text="pause",image= pause_image,bg='black',borderwidth=0,command=pause_song)
pauseButton.pack(pady=10,padx=10,in_=top,side="left")

nextButton = tk.Button(canvas,text="next",image= next_image,bg='black',borderwidth=0,command=play_next)
nextButton.pack(pady=10,padx=10,in_=top,side="left")

t=0
for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)
        t+=1

print(t)
canvas.mainloop()
