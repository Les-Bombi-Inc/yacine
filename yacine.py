from fileinput import close
from pypresence import Presence
import time
import random
from tkinter import * 
from tkinter import messagebox
import multiprocessing
from multiprocessing import Process, Pipe
import signal
import os

version = "1.0.0"

client_id = '933772175817723965'  
RPC = Presence(client_id)   
quotes = [
    "Yacine zebou sghir btw",
    "Yacine yheb el marbolou",
    "Yacine laham-",
    "YDK F ZEBI",
    "Fama mara selim karez.",
    "Yacine Gay?",
    "Yacine weld omi.",
    "Yacine Yetkayef",
    "Yacine 3ndou ch3ar f termtou.",
    "Fblk eli Yacine mawloud f 2006",
    "https://yacinepetitpipi.weebly.com/.",
    "Haya nala3bou minecraft pls.",
    "ZOK OMK.",
    "Nheb zboub",
    "Selim naghar",
    "nhbk wlh",
    "malboro forever"
]

def killme():
    print("[+] Kill Message")
    root = Tk()
    root.title(f"Yacine Petit Pipi - V{version}")
    root.geometry("630x115")
    root.resizable(0,0)
    root['background']='#1C1C1C'
    w = Label(root, text ='\n' + "Please terminate Yacine Petit Pipi's process from Task Manager!", font = "10",  bg='#1C1C1C', fg="#fff") 
    w.pack()
    exit_button = Button(root, text="    OK    ", command=root.destroy)
    exit_button.pack(pady=20)
    root.mainloop()

def rpcdiscord():
    print("[+] Connecting to Discord's RPC")
    try:
        RPC.connect() 
    except:
        print("[+] Error While Connecting")
        killme()
    print("[+] Connected to Discord's RPC Succesfully")
    while True:  
        RPC.update(large_image="gg", details="Yacine Petit Pipi:", state=random.choice(quotes), buttons=[{"label": "Yacine Petit Pipi - Website", "url": "https://yacinepetitpipi.weebly.com"}]) 
        time.sleep(10) 

def window():
    print("[+] Starting Gui")
    root = Tk()
    root.title(f"Yacine Petit Pipi - V{version}")
    root.geometry("300x150")
    root.resizable(0,0)
    root['background']='#1C1C1C'
    w = Label(root, text ='\n' + "Zamel Bombi", font = "50",  bg='#1C1C1C', fg="#fff") 
    l = Label(root, text ="Discord Rich Presence : ON", font = "50",  bg='#1C1C1C', fg="#67ef23")
    w.pack()
    l.pack()
    exit_button = Button(root, text="   STOP   ", command=killme)
    exit_button.pack(pady=20)
    root.protocol("WM_DELETE_WINDOW", killme)
    root.mainloop()

multiprocessing.freeze_support()
p1 = multiprocessing.Process(target=rpcdiscord)
p2 = multiprocessing.Process(target=window)

def main():
    print(f"[+] Starting Yacine Petit Pipi v{version}")
    print(f"[+] Created by TIGGER-X#2197")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
  
if __name__ == "__main__":
    main()