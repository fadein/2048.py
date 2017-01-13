#!/usr/bin/python2

from __future__ import print_function
from random import randint
import sys

def getnums(f,r=[0,1,2,3],c=[0,1,2,3]):
    ints=[]
    for y in r:
        for x in c:ints.append(f[y][x])
    return ints

def sert(f,liste,r=[0,1,2,3],c=[0,1,2,3],reverse=False):
    pop_from=0
    if reverse==True:pop_from=-1
    for y in range(4):
        for x in range(4):
            if y in r and x in c:f[y][x]=liste.pop(pop_from)
    return f

def emp(f):
    poses=[]
    for y in range(4):
        for x in range(4):
            if f[y][x]==0:poses.append([y,x])
    return poses

def add_random(f):
    empty=emp(f)
    y,x=empty[randint(0,len(empty)-1)]
    f[y][x]=2
    if randint(0,9)>8:f[y][x]=4
    return f

def get_new_field():
    f=[]
    for i in range(4):
        f.append([])
        for j in range(4):f[i].append(0)
    return f

def tilt_field(f, cmd):
    f2=get_new_field()
    for n in range(4):
        if cmd=="w":liste=getnums(f,c=[n])
        if cmd=="a":liste=getnums(f,r=[n])
        if cmd=="s":liste=getnums(f,c=[n])[::-1]
        if cmd=="d":liste=getnums(f,r=[n])[::-1]
        start_len=len(liste)
        while 0 in liste:
            liste.remove(0)
        i=0
        while i < len(liste) -1:
            if liste[i] == liste[i + 1]:
                liste[i] = liste[i] * 2
            i = i + 1
        liste += [0] * (start_len - len(liste))
        if cmd=="w": liste=sert(f2,liste, c=[n])
        if cmd=="a": liste=sert(f2,liste, r=[n])
        if cmd=="s": liste=sert(f2,liste, c=[n], reverse = True)
        if cmd=="d": liste=sert(f2,liste, r=[n], reverse = True)
    return f2


def pprint(f):
    for row in f:
        for ele in row:
            log10=len(str(ele))
            nexttext=" "*(4-log10)
            if ele==0:
                print("    ",end="|")
            else:
                print(nexttext+str(ele),end="|")
        print()

f=add_random(add_random(get_new_field()))
while not (f==tilt_field(f,"w")==tilt_field(f,"a")
==tilt_field(f,"s")==tilt_field(f,"d")):
    cmd=""
    pprint(f)
    while cmd not in["w","a","s","d"]:
        cmd=raw_input(">")
    f2=tilt_field(f,cmd)
    if f2!=f:f=add_random(f2)
    if max_tile(f)==2048:
        print("you win")
        sys.exit(1)
pprint(field)
print("you lose")
