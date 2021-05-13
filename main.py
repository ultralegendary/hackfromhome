import re


from core import utils
eg=utils.dataclass()
if eg.first:
    utils.welcome()

while True:
    inp=input('>>>')
    if inp and inp[-1]==':':
        inp+='\n'
        i=' '
        while i and i[0]==' ':
            i=input("...")
            inp+=i+'\n'
    
    
    if inp=='exit()':
        break
    
    try:
        exec(inp)
    except Exception as e:
        print(e)
        
        continue
    


    if eg.eggs['print'] and 'print' in inp:
        f = open("files/print.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['print']=0
        eg.dict_file()
        
    if eg.eggs['if'] and 'if' in inp:
        f = open("files/if.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['if']=0
        eg.dict_file()
        
    if eg.eggs['elif'] and 'elif' in inp:
        f = open("files/elif.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['elif']=0
        eg.dict_file()

        
    if eg.eggs['else'] and'else' in inp:
        f = open("files/else.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['else']=0
        eg.dict_file()
        
    if eg.eggs['for'] and 'for' in inp:
        f = open("files/for.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['for']=0
        eg.dict_file()
    if eg.eggs['nested_for'] and re.search("for.*\s*for", inp):
        f = open("files/nested_for.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['for']=0
        eg.dict_file()


        
    if eg.eggs['function'] and re.search("def \w{1,}\(\):",inp):
        f = open("files/function.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['function']=0
        eg.dict_file()
        

    if eg.eggs['comment_line'] and '#'in inp:
        f = open("files/comment.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['comment_line']=0
        eg.dict_file()
    if eg.eggs['class'] and re.search('^class',inp):
        f = open("files/class.cpp", mode='r', encoding='utf-8')
        print(f.read())
        f.close()
        eg.eggs['class']=0
        eg.dict_file()




