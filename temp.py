
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

        lbl.config(text="OUTPUT:\n"+output)
        #messagebox.showinfo('output', output)
    except Exception as e:
        messagebox.showinfo('Error', e)
        

def printInput():
    inp = textbox2.get(1.0, "end-1c")
    
    with open("a.cpp", "w+") as file:
        file.write(inp)
    outputFunction()

def out():
    inp=textbox1.get(1.0,"end-1 c")
    lbl.config(text=inp)

#new
# window = Frame(root, bg="yellow")
# window.place(x=0, y=0)
root=Tk()
heading = Label(root, text="project", font=("Times new roman", 40, BOLD))
heading.place(x=900, y=20)

textbox1 = Text(root, bg="black", fg="white")
textbox1.place(x=20, y=20, height=350,)

textbox2 = Text(root, bg="black", fg="white")
textbox2.place(x=670, y=100,width=600,height=400)


submitButton1 = Button(root, text="Run", fg="black",command=out)
submitButton1.place(x=600, y=325)

submitButton2 = Button(root, text="Compile", fg="black",command=printInput)
submitButton2.place(x=1200, y=500)

lbl=Label(root,text='text',font=("Times new roman",20))
lbl.place(x=40,y=450)

root.geometry("1300x700")
root.mainloop()

