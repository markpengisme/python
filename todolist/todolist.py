import os
import random

def make_todo_list():
    
    if not os.path.exists('Write_the_list_here.txt'):
        with open('Write_the_list_here.txt', 'w') as f:
            f.write("This is an example.\n"+
                "There is no need to order by numbers.\n"+
                "Hello World!")
            print('Please write a list in new file "Write_the_list_here.txt"')
            return
        
    with open('todolist.txt', 'w') as f:
        pass
    
    f = open("Write_the_list_here.txt",'r')
    content = f.readlines()
    content = [x.strip()+'\n' for x in content]
    #print(content) #debug
    f.close()
    
    lists=[]
    for list in range(len(content)):
        ran=random.randint(0, len(content)-1)
        lists.append("{}.".format(list+1)+content[ran])
        del content[ran]
    with open('todolist.txt', 'w') as f:
        f.writelines(lists)
        print("Already created a to-do list")

if __name__ == '__main__':
    try:
        make_todo_list()
    except:
        print("Error")
