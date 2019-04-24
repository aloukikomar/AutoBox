# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
import os,time
import json
import multiprocessing

dir_path = os.path.dirname(os.path.realpath(__file__))
PagePath=dir_path+"/../BDD/Pages/"
ChapterPath=dir_path+"/../BDD/Chapters/"
NovelPath=dir_path+"/../BDD/Novels/"
lockPath=dir_path+"/../BDD/tmp/.lock"

BaseBDDDir="/home/automation/webapps/AutoBox/BDD/"
ToReadFile= BaseBDDDir+"ToRead.txt"

LogToolBoxRunTests="tmp/LOG_TOOLBOX_RUNTESTS"
lockFile="tmp/lock"
message="Hit and Run !!"
def index(request):
	return HttpResponse("<h1>Run</h1>")

def home(request,*messag):
    NovelAvailable=os.listdir(NovelPath)
    ToDoList=open(ToReadFile,"r").readlines()
    ToDoLists="".join(ToDoList).replace("\n"," ").split(" ")
    if os.path.isfile(lockPath):
        lock=1
    else:
        lock=0
    print(ToDoLists)
    TSR=open(dir_path+"/../BDD/tmp/CurrentTSR","r").readline()
    images=os.listdir(dir_path+"/../BDD/Logs/"+TSR+"/Images/")
    images=[ TSR + '/Images/' + s for s in images ]
    return render(request,'Dashboard/home.html',{'ToDoLists':ToDoLists,'NovelAvailable':NovelAvailable,'lock':lock,'TSR':TSR,'images':images})


def LiveLogFile(request,TSRpath=None):
    print(TSRpath)
    path=dir_path+"/../BDD/Logs/"+TSRpath+"/Test.Report"
    out=open(path,"r").readlines()
    return render(request,'Dashboard/TSRLogs.html',{'TSRLogs':out})
    #return HttpResponse("<h1>{}</h1>".format(out))

# Create your views here.