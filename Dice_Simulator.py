import random as rd

def check(no):
    if no == 1:
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
    elif no == 2:
        print("[   0   ]")
        print("[       ]")
        print("[   0   ]")
    elif no == 3:
        print("[0      ]")
        print("[   0   ]")
        print("[      0]")
    elif no == 4:
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
    elif no == 5:
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
    else:
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")

def simulator():
    no = rd.randint(1,6)
    print("---------")
    check(no)
    print("---------")

if __name__ == '__main__':

    print(simulator())
    while(True):
        print("Press y to roll again")
        character = input()
        if(character=='y'):
            simulator()
        else:
            exit()