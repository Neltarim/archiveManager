#!/bin/python3
#coding:utf-8

import os
import pickle
import time

#******** PICKLE FUNCTIONS *****

def CFdumper(name, src, dest): #stocke la config dans un fichier

    configPath = "configFile/" + name

    with open(configPath, "wb") as my_file:
        file_pickler = pickle.Pickler(my_file) #cree un pickler sur my_file

        file_pickler.dump(name) #dump le nom de la save
        file_pickler.dump(src)  #la source
        file_pickler.dump(dest) #la destination

def CFshow(name, src, dest): #affiche un config file definit

    configPath = "configFile/" + name

    with open(configPath, "rb") as my_file:
        file_pickler = pickle.Unpickler(my_file)

    name = file_pickler.load() #charge le nom
    src = file_pickler.load()  #charge la source
    dest = file_pickler.load() #charge la destination

    print("name = ", name)
    print("source = ", src)
    print("destination = ", dest)

def CFdirShow(): #affiche les noms de tout les config files

    print("Actuals save : ")
    CFpath = "/home/neltarim/Documents/archiveManager/SaveConfig/configFile"
    dirs = os.listdir(CFpath) #stocke les noms dans un dico
    for file in dirs:         #affiche le tout
        print(file)

# ******* MENU FUNCTIONS ********

def newSave(): #cree une nouvelle sauvegarde
    print("New save configuration >>> ")
    
    name = str()
    src = str()
    dest = str()

    yesno = str()

    #demande les infos au user
    name = input("Define a name for your save : ")
    src = input("Define the source : ")
    dest = input("Define the destination : ")

    print()
    #affiche une confirmation
    print("name = ", name)
    print("source = ", src)
    print("destination = ", dest)
    yesno = input("Finish the config and create this save? (yes/no) :")

    if yesno == "no":
        print("return to menu ...")
        print("\n\n\n")
        return newSave() #retour au debut recursif

    print("Creating the config file ...")

    CFdumper(name, src, dest) #definition  plus haut
    print("config file created, back to menu.")
    print("\n\n\n")

def modifySave(): #modifie une sauvegarde existante
    print("Modify save >>>")

    name = str()
    src = str()
    dest = str()

    yesno = str()
    choice = str()

    CFdirShow() #definition plus haut

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

def delSave(): #supprime une sauvegarde existante
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

def showSaves(): #affiche les sauvegardes actuelles
    print("Actual saves >>>")

    CFdirShow()

    time.sleep(1)
    key = input("Press any key to quit ... : ")
    print("\n\n\n")