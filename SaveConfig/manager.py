#!/bin/python3
# coding:utf-8

from CFdef import *

def menu():

    choice = str()
    
    print("option : ")
    print("new | modify | delete | show | quit \n")
    choice = input("What to do ... : ")

    return choice

print("Welcome to the BMEC archive manager\n")

while True:

    choice = menu()

    if choice == "new":
        newSave()

    elif choice == "modify":
        modifySave()

    elif choice == "delete":
        delSave()

    elif choice == "show":
        showSaves()

    elif choice == "quit":
        quit()

    else:
        print("argument invalid ...")

    continue