class dataclass:
  def __init__(self):
    import pickle
    try:
      File=open("dicteggs.pkl","rb")#file must be exist before
      self.eggs = pickle. load(File)
      File.close()
      self.first=False
    except:
      d=initial()
      self.eggs=d.eggs
      f=open("dicteggs.pkl","wb")
      pickle.dump(self.eggs,f)
      f.close()
      self.first=True


    

  def dict_file(self):
    import pickle
    File=open("dicteggs.pkl","wb")
    pickle.dump(self.eggs,File)
    File.close()


class initial:
  def __init__(self):
    self.eggs={
      "print":1,
      "if":1,
      "elif":1,
      "else":1,
      "function":1,
      "recurssion":1,
      "for":1,
      "nested_for":1,
      "comment_line":1,
      "class":1,
      "list":1,
      "import":1,
      "constructor":1,
      "return":1,
      "list":1,
      }

import time
#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=congrats
egg= '''                                        
                                ████████                                  
                              ██        ██                                
                            ██▒▒▒▒        ██                              
                          ██▒▒▒▒▒▒      ▒▒▒▒██                            
                          ██▒▒▒▒▒▒      ▒▒▒▒██                            
                        ██  ▒▒▒▒        ▒▒▒▒▒▒██                          
                        ██                ▒▒▒▒██                          
                      ██▒▒      ▒▒▒▒▒▒          ██                        
                      ██      ▒▒▒▒▒▒▒▒▒▒        ██                        
                      ██      ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒██                        
                      ██▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒██                        
                        ██▒▒▒▒  ▒▒▒▒▒▒    ▒▒▒▒██                          
                        ██▒▒▒▒            ▒▒▒▒██                          
                          ██▒▒              ██                            
                            ████        ████                              
                                ████████                                  
                                          '''
egg1='''
        .-"-.
      .'=^=^='.
     /=^=^=^=^=\\
    :^=^=^=^=^=^;
    |^=^=^=^=^=^|
    :^=^=^=^=^=^:
     \=^=^=^=^=/
      `.=^=^=.'
        `~~~`
         '''
design='''.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.'''
def welcome():
    slow("Welcome to out project Code from Code!")
    slow(design)
    slow(egg1)
    slow("This is about testing your python skills and we will be displaying its equivalent in c++ and make you code in c++")

from termcolor import cprint

def slow(t,*args, speed=130,**kwargs):
    for i in t:
        cprint(i,*args,end='',flush=True)
        time.sleep(5.0 / speed)
    print()
    time.sleep(1)