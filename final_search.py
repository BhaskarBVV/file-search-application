import os
import tkinter as tk
import string
from tkinter.constants import CENTER

if __name__ == "__main__":
    print(os.getlogin())
    search_input = input("Enter the file name : ").lower()
    print("Would not recommend to enetr disk C, it automatically searches in C:/Users area\n")
    print("Enter the local Disk's to be searched (with spaces) : ")
    disk= list(input())
    # for _ in disk:
    #     print(_)
    for str in disk:
        disk_name=str.upper()+":/"
        print(disk_name)
        listing = os.walk(disk_name)
        base_path_1 = disk_name
        found = False
        x = 1
        print("These are the matching files:\n")
        file_list = []
        for root_path in listing:
            for directories in root_path:
                for files in directories:
                    if search_input in files.lower():
                        found = True
                        z = os.path.join(root_path[0], files)
                        print(x, " ", files)
                        file_list.append(z)
                        z = ""
                        x = x+1
    special_area="C:/Users"+(os.getlogin());
    listing = os.walk(special_area)
    base_path_1 = special_area
    for root_path in listing:
        for directories in root_path:
            for files in directories:
                if search_input in files.lower():
                    found = True
                    z = os.path.join(root_path[0], files)
                    print(x, " ", files)
                    file_list.append(z)
                    z = ""
                    x = x+1
    if found == True:
        while True:
            print("Enter the file number (0 to exit) : ")
            inp = int(input())
            if inp==0:
                break
            elif inp != 0 and inp<x:
                os.startfile(file_list[inp-1])
            else:
                print("Invlaid input, try again")
    if found == False:
        print("No such file found")
