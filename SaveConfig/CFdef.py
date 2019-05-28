#!/bin/python3
#coding:utf-8

import os
import pickle
import time

#******** PICKLE FUNCTIONS *****

def CFdumper(name, src, dest):

    configPath = "configFile/" + name

    with open(configPath, "wb") as my_file:
        file_pickler = pickle.Pickler(my_file)

        file_pickler.dump(name)
        file_pickler.dump(src)
        file_pickler.dump(dest)

def CFshow(name, src, dest):

    configPath = "configFile/" + name

    with open(configPath, "rb") as my_file:
        file_pickler = pickle.Unpickler(my_file)

    name = file_pickler.load()
    src = file_pickler.load()
    dest = file_pickler.load()

    print("name = ", name)
    print("source = ", src)
    print("destination = ", dest)

def CFdirShow():

    print("Actuals save : ")
    CFpath = "/home/neltarim/Documents/archiveManager/configFile"
    dirs = os.listdir(CFpath)
    for file in dirs:
        print(file)

# ******* SAVE FUNCTIONS ********

def newSave():
    print("New save configuration >>> ")
    
    name = str()
    src = str()
    dest = str()

    yesno = str()

    name = input("Define a name for your save : ")
    src = input("Define the source : ")
    dest = input("Define the destination : ")

    print()
    print("name = ", name)
    print("source = ", src)
    print("destination = ", dest)
    yesno = input("Finish the config and create this save? (yes/no) :")

    if yesno == "no":
        print("return to menu ...")
        print("\n\n\n")
        return 0

    print("Creating the config file ...")

    CFdumper(name, src, dest)
    print("config file created, back to menu.")
    print("\n\n\n")

def modifySave():
    print("Modify save >>>")

    name = str()
    src = str()
    dest = str()

    yesno = str()
    choice = str()

    CFdirShow()

    name = input("change : ")
    print()

    CFshow(name, src, dest)

    name = input("Define a name for this save : ")
    src = input("Define the source : ")
    dest = input("Define the destination : ")

    print()
    print("name = ", name)
    print("source = ", src)
    print("destination = ", dest)
    yesno = input("Finish the config and modiffy this save? (yes/no) :")

    if yesno == "no":
        print("return to menu ...")
        return 0

    print("modifying the config file ...")

    CFdumper(name, src, dest)
    print("config file modified, back to menu.")
    print("\n\n\n")

def delSave():
    print("Delete save >>>")

    name = str()

    yesno = str()

    CFdirShow()

    name = input("What save do you want to delete? : ")
    namePath = "configFile/" + name

    yesno = input("are you sure to delete {} ? (yes/no) : ".format(name))
    
    if yesno == "yes":
        os.remove(namePath)
        print("{} removed.".format(name))
        print("\n\n\n")
    else:
        delSave()

def showSaves():
    print("Actual saves >>>")

    CFdirShow()

    time.sleep(1)
    key = input("Press any key to quit ... : ")


    if key != "wfesesgr":
        print("\n\n\n")
        return 0
        