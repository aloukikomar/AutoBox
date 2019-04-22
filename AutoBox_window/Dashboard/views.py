# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
PagePath=dir_path+"/../BDD/Pages/"
ChapterPath=dir_path+"/../BDD/Chapters/"
NovelPath=dir_path+"/../BDD/Novels/"

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
    print(ToDoLists)
    return render(request,'Dashboard/home.html',{'ToDoLists':ToDoLists,'NovelAvailable':NovelAvailable})


def BuildPOM(request):
    execfile(dir_path+"/../BDD/MakePOM.py", globals())
    print(dir_path)
    TSR=open(dir_path+"/../BDD/tmp/CurrentTSR","r").readline()
    output=open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"r+").readlines()
    return render(request,'Dashboard/BuildPOM.html',{'output':output})

def RunTest(request):
    
    return render(request,'Dashboard/Runtest.html')

def GetNovel(request):
    NovelContent=request.GET.get("novel")
    NovelContent=open(BaseBDDDir+"Novels/"+NovelContent+"/ChapterIndex.txt","r").readlines()
    NovelContent="".join(NovelContent).replace("\n"," ").replace("\r","").split(" ")
    print(NovelContent)
    return render(request,'Dashboard/novelContent.html',{'NovelContent':NovelContent})

def GetChapter(request):
    ChapterContent=request.GET.get("Chapter")
    ChapterContent=open(BaseBDDDir+"Chapters/"+ChapterContent+"/PageIndex.txt","r").readlines()
    ChapterContent="".join(ChapterContent).replace("\n"," ").replace("\r","").split(" ")
    print(ChapterContent)
    return render(request,'Dashboard/ChapterContent.html',{'ChapterContent':ChapterContent})

def GetPage(request):
    PageContent=request.GET.get("Page")
    Page=open(BaseBDDDir+"Pages/"+PageContent+".txt","r").readlines()
    for line in Page:
        indexN=Page.index(line)
        line=line.split(" ")
        Page[indexN]=line
    PageContent=Page
    KeyWord=['Start\n','PrintContent','Close','Bash','WithArgs','As','Upload','From','Continue\n','LookFor','Enter','Click\n','Include','Open','Run','Store','Click']
    #PageContent="".join(Page).replace("\n","|").split("|")
    return render(request,'Dashboard/PageContent.html',{'PageContent':PageContent,'KeyWord':KeyWord})
# Create your views here.

