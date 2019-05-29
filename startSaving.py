#!/bin/python3
#coding:utf-8

import os
import pickle
import datetime
import shutil


#******* DEF **********

def applyDate(dest):
    date = datetime.datetime.now()
    simpleDate = str(date.day + date.month + date.year)
    day = str(date.day)
    month = str(date.month)
    year = str(date.year)

    dest = dest + "-" + day + "_" + month + "_" + year
    return(dest)

#****** SCRIPT *********

dirLen = -1 #vous comprendrez plus loin

CFpath = "/home/neltarim/Documents/archiveManager/SaveConfig/configFile"
dirs = os.listdir(CFpath) #liste les fichiers config dans dirs
for file in dirs:
    dirLen += 1

print(dirs)
print(dirLen + 1)

if dirLen < 0:
    print("No config files detected.")
elif dirLen > 10: #evite un trop grand nombre de config file ou alors une mauvaise localisation du dossier configFile.
    print("too many config files.")


while dirLen != -1: #opere sur tous les fichiers de config

    print("Saving {} ...".format(dirs[dirLen]))
    name = dirs[dirLen]
    src = str()
    dest = str()

    configPath = "SaveConfig/configFile/" + name

    with open(configPath, "rb") as CFile: #importe la config
        cf_pickler = pickle.Unpickler(CFile)

        name = cf_pickler.load()
        src = cf_pickler.load()
        dest = cf_pickler.load()

    dest = applyDate(dest) #ajoute la date au dir de destination

    shutil.copytree(src, dest) #copie recursivement l'arborescence
    print("{} saved from :\n{} \nto : \n{} .".format(dirs[dirLen], src, dest))
    dirLen -= 1 #passe au config file suivant

print("All saves have been done successfuly.")
    