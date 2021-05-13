
import os
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

import shlex,subprocess

def run(cmd: str):
    cmd = shlex.split(cmd)
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
def outputFunction():
    try:
        output=run(f"g++ a.cpp && a.exe")

        
        messagebox.showinfo('output', "excuted successfully")
    except:
        print("Exception")

def printInput():
    inp = textbox.get(1.0, "end-1c")
    
    with open("a.cpp", "w+") as file:
        file.write(inp)
    outputFunction()

root = Tk()
window = Frame(root)
window.pack()

heading = Label(window, text="Heading", font=("Times new roman", 80, BOLD))
heading.pack()

textbox = Text(bg="black", fg="white",width=50)
textbox.pack()

submitButton = Button(root, text="Submit", height=5, width=15, command=printInput)
submitButton.pack()

root.geometry("600x600")
root.mainloop()