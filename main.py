
import subprocess
from eggs import eggs
import tkinter
from core.utils import welcome
string=''''''
welcome()

top=tkinter.Tk()
top.mainloop()

while True:
    semi=0
    inp=input('>>>')
    '''if inp and inp[-1]==':':
        semi=1
        string+=inp
        while semi==1:
            inp=input('>>>  ')
    def run(cmd: str):
        cmd = shlex.split(cmd)
        return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")

        '''
    
    
    if inp=="exit()":
        break
    try:
        eval(inp)
    except:
        print("its an error",inp)
        continue
    for i in eggs:
        if eggs[i] and i in inp:
            eggs[i]=0
            print(i,"has been found")
