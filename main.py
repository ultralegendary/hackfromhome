import re
import protips as pp

from core import utils



import os
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from playsound import playsound
import shlex,subprocess

prtip=''
def main():
    eg=utils.dataclass()
    if eg.first:
        pass

    

    def checker(inp):
        try:
            exec(inp)
        except Exception as e:
            lbl.config(text="Invalid python syntax!\n\tTry again!")
            playsound('sounds/gameover.wav')
            return
        
        global prtip
        prtip=''
        s=''
        
        
        


        if eg.eggs['print'] and 'print' in inp:
            s='Now, see how `print` is done in c++ : \n'

            f = open("files/print.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to program with two `cout` statements in the right side c++ editor'
            f.close()
            prtip+=pp.prot["print"]
            
            playsound('sounds/coin.mp3')
            lbl.config(text=s)

            eg.eggs['print']=0
            eg.dict_file()
            
        if eg.eggs['if'] and 'if' in inp:
            s='Now, see how `if` is used in c++ : \n'
            
            f = open("files/if.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to have a condition to check if a number is negative with `cout` statements'
            prtip+=pp.prot["if"]
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['if']=0
            eg.dict_file()
            
        if eg.eggs['elif'] and 'elif' in inp:
            s='Now, see how `else if` is used in c++ : \n'
            f = open("files/elif.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to check weather a number is higher than 100 or higher than 10 `cout` statements'
            prtip+=pp.prot["elif"]
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['elif']=0
            eg.dict_file()

            
        if eg.eggs['else'] and'else' in inp:
            s='Now, see how `else` used in c++ : \n'
            f = open("files/else.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to check if a number is divisible by 2 `cout` statements'
            prtip=pp.prot["else"]
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['else']=0
            eg.dict_file()
            
        if eg.eggs['for'] and 'for' in inp:
            s='Now, see how `for loop` is done in c++ : \n'
            f = open("files/for.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to use a loop to find sum of first 10 natural numbers'
            prtip=pp.prot["for"]
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['for']=0
            eg.dict_file()
        if eg.eggs['nested_for'] and re.search("for.*\s*for", inp):
            s='Now, see how `nested for loop` is done in c++ : \n'
            f = open("files/nested_for.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to use a nested for loop to print a triangle pattern'
            
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['for']=0
            eg.dict_file()


            
        if eg.eggs['function'] and re.search("def \w{1,}\(\):",inp):
            s='Now, see how `functions` are defined in c++ : \n'
            f = open("files/function.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to use function to return multiplication of two numbers using return statement'
            f.close()
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            eg.eggs['function']=0
            eg.dict_file()
            

        if eg.eggs['comment_line'] and '#'in inp:
            s='Now, see `comment line` are used in c++ : \n'
            f = open("files/comment.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to use comment line '
            lbl.config(text=s)
            prtip=pp.prot['comment_line']
            playsound('sounds/coin.mp3')
            f.close()
            eg.eggs['comment_line']=0
            eg.dict_file()
        if eg.eggs['class'] and re.search('^class',inp):
            s='Now, see `classes` are defined in c++ : \n'
            f = open("files/class.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to define a class with one variable and one function '
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            f.close()
            eg.eggs['class']=0
            eg.dict_file()
        if eg.eggs['constructor'] and 'def __init__():'in inp:
            s='Now, see how `constructors` of classes are done in c++ : \n'
            f = open("files/constructor.cpp", mode='r', encoding='utf-8')
            s+=f.read()
            s+='\n\nYour task now : to define a function inside a class'
            lbl.config(text=s)
            playsound('sounds/coin.mp3')
            f.close()
            eg.eggs['constructor']=0
            eg.dict_file()
        print(prtip)




    def run(cmd: str):
        cmd = shlex.split(cmd)
        return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
    def outputFunction():
        try:
            output=run(f"g++ a.cpp && a.exe")

            lbl.config(text="Congrats, your code has been accepted!\nOUTPUT:\n"+output)
            playsound('sounds/powerup.wav')
            #messagebox.showinfo('output', output)
        except Exception as e:
            playsound('sounds/gameover.mp3')
            messagebox.showinfo('Error', e)
            

    def printInput():
        inp = textbox2.get(1.0, "end-1c")
        
        with open("a.cpp", "w+") as file:
            file.write(inp)
        outputFunction()

    def out():
        inp=textbox1.get(1.0,"end-1 c")
        lbl.config(text=inp+'\n\nTry something new and explore!')# need to remove
        checker(inp)

    def prot():
        if not prtip:
            protip.config(text='nothing to show')
        else:
            protip.config(text=prtip)





    root=Tk()
    heading = Label(root, text="Code from Code!", font=("Times new roman", 40, BOLD))
    heading.place(x=900, y=20)

    protip=Label(root,text="",font=("",16))
    protip.place(x=700,y=500)

    textbox1 = Text(root, bg="black", fg="white")
    textbox1.place(x=20, y=20, height=350,)

    textbox2 = Text(root, bg="black", fg="white")
    textbox2.place(x=670, y=100,width=600,height=400)


    probutton = Button(root, text="pro tip", fg="black",command=prot)
    probutton.place(x=650, y=540)

    submitButton1 = Button(root, text="Run", fg="black",command=out)
    submitButton1.place(x=600, y=325)

    submitButton2 = Button(root, text="Compile", fg="black",command=printInput)
    submitButton2.place(x=1200, y=460)

    lbl=Label(root,text='''welcome to our Code from Code\nType your python code in the above box and press run
    \nUse The right side box to compile c++ code''',font=("Times new roman",13),justify=LEFT,anchor='w')
    lbl.place(x=20,y=400,width=600)



    root.geometry("1300x700")
    root.mainloop()



    '''while True:
    inp=input('>>>')
    if inp and inp[-1]==':':
            inp+='\n'
            i=' '
            while i and i[0]==' ':
                i=input("...")
                inp+=i+'\n'
    '''





if __name__=="__main__":
    main()
