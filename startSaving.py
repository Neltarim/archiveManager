#!/bin/python3
#coding:utf-8

import os
import pickle

def CFgrabber(&name, &src, &dest):

    configPath = "configFile/" + name

    with open(name, "rb") as CFile:
        cf_pickler = pickle.Pickler(CFile)

        name = cf_pickler.load()
        src = cf_pickler.load()
        dest = cf_pickler.load()


#script copy

dirLen = 0

CFpath = "/home/neltarim/Documents/archiveManager/configFile"
dirs = os.listdir(CFpath)
for file in dirs:
    dirLen += 1

if dirLen == 0:
    print("No config file.")

while dirLen != 0:
    