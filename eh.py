import os
import sys



def check_system():
    
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
        return "linux"
    elif sys.platform == "win32":
        os.system("cls")
        return "win32"

check_system()


with open("pages/"+sys.argv[1], "r") as opnr:
    for data in opnr:
        print(data)