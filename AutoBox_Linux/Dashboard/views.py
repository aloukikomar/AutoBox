# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    TSR='TSR_1555668924'
    images=os.listdir(dir_path+"/../BDD/Logs/"+TSR+"/Images/")
    images=[ TSR + '/Images/' + s for s in images ]
    return render(request,'Dashboard/home.html',{'ToDoLists':ToDoLists,'NovelAvailable':NovelAvailable,'lock':lock,'TSR':TSR,'images':images})


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

def StartTest(request):
    if request.method =='POST':
        Cont=request.POST.get('AllNovels')
        print(Cont,"======")
        open(dir_path+"/../BDD/ToRead.txt","w+").write(Cont)
        open(lockPath,"w+").write("started")
        print("Lock Implemented")
    return redirect("/Dashboard/home/")

def StopTest(request):
    os.remove(lockPath)
    print("Lock Removed!")
    return redirect("/Dashboard/home/")
# Create your views here.