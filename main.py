from fileinput import close
from logging import root
from pypresence import Presence
import time
import random
from tkinter import * 
from tkinter import messagebox
import multiprocessing
from multiprocessing import Process, Pipe
import os
import sys

version = "1.1.2"

client_id = '6666666' ##fake_client_id  
RPC = Presence(client_id)   
quotes = [
    "Yacine zebou sghir btw",
    "Yacine yheb el marbolou",
    "Yacine laham",
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
    "malboro forever",
    "Ghanem bakey",
    "Hamemi rajel",
    "Sakrou rab lycee",
    "Mlewi zbr",
    '"Dakhalhouli blhi"',
    "pornhub.com",
    "Zamel bombi",
    "Zamel Khouna",
    "Zamel hoby",
    "Zamel Rajel",
    "Zamel pro",
    "FOV",
    "Terma"
]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("icoyacine.ico")

def error(error):
    print("[+] Kill Message")
    root = Tk()
    root.title(f"Yacine Petit Pipi - v{version}")
    root.iconbitmap(icon)
    root.geometry("800x200")
    root.resizable(0,0)
    root['background']='#1C1C1C'
    w = Label(root, text ='\n' + error, font = "10",  bg='#1C1C1C', fg="#fff") 
    w.pack()
    exit_button = Button(root, text="    OK    ", command=root.destroy)
    exit_button.pack(pady=20)
    root.mainloop()

def killme():
    print("[+] Kill Message")
    root = Tk()
    root.title(f"Yacine Petit Pipi - v{version}")
    root.iconbitmap(icon)
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
        error("Couldn't connect to Discord's RPC, restart Discord and try again.")
    print("[+] Connected to Discord's RPC Succesfully")
    while True:  
        RPC.update(large_image="gg", details="Ma3louma Moufida:", state=random.choice(quotes), buttons=[{"label": "Yacine Petit Pipi - Website", "url": "https://yacinepetitpipi.weebly.com"}]) 
        time.sleep(10) 

def window():
    lol = random.choice(quotes)
    print("[+] Starting Gui")
    root = Tk()
    root.iconbitmap(icon)
    root.title(f"Yacine Petit Pipi - v{version}")
    root.geometry("300x150")
    root.resizable(0,0)
    root['background']='#1C1C1C'
    w = Label(root, text ='\n' + lol, font = "50",  bg='#1C1C1C', fg="#fff") 
    l = Label(root, text ="Discord Rich Presence : ON", font = "50",  bg='#1C1C1C', fg="#67ef23")
    w.pack()
    l.pack()
    exit_button = Button(root, text="   STOP   ", command=killme)
    exit_button.pack(pady=20)
    root.protocol('WM_DELETE_WINDOW', killme)
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
