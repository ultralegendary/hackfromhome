import protips as pp
from core import utils

import os,re

from playsound import playsound
import shlex,subprocess

prtip=''
def main():
    eg=utils.dataclass()
    if eg.first:
        playsound('sounds/stage.wav')
        utils.welcome()

    print("Lets ENTER the game!\nyou need to show us how skilled you are in python")
    while True:
        inp=input('>>>')
        if inp and inp[-1]==':':
            inp+='\n'
            i=' '
            while i and i[0]==' ':
                i=input("...")
                inp+=i+'\n'
        if inp=='exit()':
            print("Your process saved successfully")
            break
    
        try:
            exec(inp)
        except Exception as e:
            print(e)
            playsound('sounds/gameover.wav')
            continue
        
        global prtip
        prtip=''
        
        
        
        


        if eg.eggs['print'] and 'print' in inp:
            playsound('sounds/coin.mp3')

            utils.slow('Now, see how `print` is done in c++ : \n')

            f = open("files/print.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to program with two `cout` statements')
            print('\nYou can submit your code by pressing `enter` three times')
            f.close()
            prtip+=pp.prot["print"]
            
            
            

            eg.eggs['print']=0
            eg.dict_file()
            writecpp()
            
        if eg.eggs['if'] and 'if' in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `if` is used in c++ : \n')
            
            f = open("files/if.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to have a condition to check if a number is negative with `cout` statements\n\nYou can submit your code by pressing enter 3 times')
            prtip+=pp.prot["if"]
            f.close()
            
            
            eg.eggs['if']=0
            eg.dict_file()
            writecpp()
        if eg.eggs['elif'] and 'elif' in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `else if` is used in c++ : \n')
            f = open("files/elif.cpp", mode='r', encoding='utf-8')
            print(f.read())
            slow('\n\nYour task now : to check weather a number is higher than 100 or higher than 10 `cout` statements')
            prtip+=pp.prot["elif"]
            f.close()
            
            
            eg.eggs['elif']=0
            eg.dict_file()

            writecpp()
        if eg.eggs['else'] and'else' in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `else` used in c++ : \n')
            f = open("files/else.cpp", mode='r', encoding='utf-8')
            print(f.read())
            s+='\n\nYour task now : to check if a number is divisible by 2 `cout` statements'
            prtip=pp.prot["else"]
            f.close()
            
            
            eg.eggs['else']=0
            eg.dict_file()
            writecpp()
        if eg.eggs['for'] and 'for' in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `for loop` is done in c++ : \n')
            f = open("files/for.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to use a loop to find sum of first 10 natural numbers')
            prtip=pp.prot["for"]
            f.close()
            
            
            eg.eggs['for']=0
            eg.dict_file()
            writecpp()
        if eg.eggs['nested_for'] and re.search("for.*\s*for", inp):
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `nested for loop` is done in c++ : \n')
            f = open("files/nested_for.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to use a nested for loop to print a triangle pattern')
            
            f.close()
            
            
            eg.eggs['for']=0
            eg.dict_file()
            writecpp()


            
        if eg.eggs['function'] and re.search("def \w{1,}\(\):",inp):
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `functions` are defined in c++ : \n')
            f = open("files/function.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to use function to return multiplication of two numbers using return statement')
            f.close()
            
            eg.eggs['function']=0
            eg.dict_file()
            writecpp()

        if eg.eggs['comment_line'] and '#'in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see `comment line` are used in c++ : \n')
            f = open("files/comment.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to use comment line inside main() ')
            
            prtip=pp.prot['comment_line']
            
            f.close()
            eg.eggs['comment_line']=0
            eg.dict_file()
            writecpp()
        if eg.eggs['class'] and re.search('^class',inp):
            playsound('sounds/coin.mp3')
            utils.slow('Now, see `classes` are defined in c++ : \n')
            f = open("files/class.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to define a class with one variable and one function ')
            
            playsound('sounds/coin.mp3')
            f.close()
            eg.eggs['class']=0
            eg.dict_file()
            writecpp()
        if eg.eggs['constructor'] and 'def __init__():'in inp:
            playsound('sounds/coin.mp3')
            utils.slow('Now, see how `constructors` of classes are done in c++ : \n')
            f = open("files/constructor.cpp", mode='r', encoding='utf-8')
            print(f.read())
            utils.slow('\n\nYour task now : to define a function inside a class')
            
            
            f.close()
            eg.eggs['constructor']=0
            eg.dict_file()
            writecpp()
        if prtip:
            i=input("press `p` for a protip!")
            if i=='p'or i=='P':
                print("ProTip:")
                utils.slow(prtip)


def writecpp():
        s=''
        print("Enter your c++ code: (press enter 3 times to submit your code)\n")
        s=input()
        while not(len(s)>3 and s[-3:]=='\n\n\n'):
            s+='\n'+input()
        print("processing your code! ")
        with open("a.cpp", "w+") as file:
            file.write(s)
        try:
            
            output=run(f"g++ a.cpp && a.exe")
            if not output:
                print("Your code has some errors!Try again! ")
                playsound('sounds/gameover.wav')
                writecpp()
            else:
                playsound('sounds/powerup.wav')
                print("congrats! your code has been accepted\nOUTPUT:\n"+output)

            
        except Exception as e:
            playsound('sounds/gameover.wav')
            

            


def run(cmd: str):
        cmd = shlex.split(cmd)
        return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")


if __name__=="__main__":
    main()
