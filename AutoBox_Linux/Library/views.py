# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.shortcuts import redirect
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
PagePath=dir_path+"/../BDD/Pages/"
ChapterPath=dir_path+"/../BDD/Chapters/"
NovelPath=dir_path+"/../BDD/Novels/"
DataPath=dir_path+"/../BDD/Data/"

PageList=os.listdir(PagePath)

filedata="No File Selected"
TestCasesDir="/home/automation/webapps/"
LogToolBoxRunTests="/tmp/LOG_TOOLBOX_RUNTESTS"
path=TestCasesDir+"AutoBox/BDD/ToRead.txt"
def index(request):
	return HttpResponse("<h1>AddCases</h1>")

def home(request):
	ChapterAvailable=os.listdir(ChapterPath)
	NovelAvailable=os.listdir(NovelPath)
	filetoopen=open(path,"r")
	outputfile=filetoopen.readlines()
	PageList=os.listdir(PagePath)
	glossarylist=os.listdir(DataPath)
	glossarylist=[ s.replace(".json","") for s in glossarylist ]
	return render(request,'Library/home.html',{'glossarylist':glossarylist,'filedata':filedata,'outputfile':outputfile,'PageList':PageList,'ChapterAvailable':ChapterAvailable,'NovelAvailable':NovelAvailable})

def AddNovelForm(request):
	ChapterAvailable=os.listdir(ChapterPath)
	NovelAvailable=os.listdir(NovelPath)
	print(ChapterAvailable,NovelAvailable)
	return render(request,'Library/AddNovel.html',{'ChapterAvailable':ChapterAvailable,'NovelAvailable':NovelAvailable})

def AddChapterForm(request):
	ChapterAvailable=os.listdir(ChapterPath)
	PageListCurrent=os.listdir(PagePath)
	PageListCurrent="".join(PageListCurrent).replace(".txt"," ").replace("\r","").split(" ")
	PageListCurrent.sort()
	print(ChapterAvailable)
	return render(request,'Library/AddChapters.html',{'ChapterAvailable':ChapterAvailable,'PageListCurrent':PageListCurrent})

def AddPageForm(request):
		ChapterAvailable=os.listdir(ChapterPath)
		print(ChapterAvailable)
		keylist=['Start','Continue','Include','Close','SwitchTab','LookFor','Run','Open','Wait5','MoveTo','Store','PrintContent','HandleAlert']
		keylist.sort()
		Subkeylist=['Enter','WriteHtml','Click']
		Subkeylist.sort()
		return render(request,'Library/AddPage.html',{'Subkeylist':Subkeylist,'keylist':keylist,'ChapterAvailable':ChapterAvailable})
# Create your views here.
def ADDPAGE(request):
	if request.method =='POST':
		PageName=request.POST.get('PageName')
		Contents=request.POST.get('PageContent')
		NewPagePath=PagePath+PageName+".txt"
		p=open(NewPagePath,"w+")
		p.write(Contents)
		p.close()
		print(NewPagePath)
        return redirect("/Library/home/")

def ADDCHAPTER(request):
	if request.method =='POST':
		ChapterName=request.POST.get('ChapterName')
		Contents=request.POST.get('ChapterContent')
		directory=ChapterPath+ChapterName
		if not os.path.exists(directory):
			os.makedirs(directory)
		p=open(directory+"/PageIndex.txt","w+")
		p.write(Contents)
		p.close()
        return redirect("/Library/home/")

def ADDNOVEL(request):
	if request.method =='POST':
		NovelName=request.POST.get('NovelName')
		Contents=request.POST.get('NovelContent')
		directory=NovelPath+NovelName
		if not os.path.exists(directory):
			os.makedirs(directory)
		p=open(directory+"/ChapterIndex.txt","w+")
		p.write(Contents)
		p.close()
        return redirect("/Library/home/")

def fetchdata(request,filename):
	try:
		with open(DataPath+filename+".json") as json_file:
			Env=json.load(json_file)
			Env=Env.keys()
		with open(DataPath+filename+".json") as json_file2:	
			data = json_file2.readlines()
			print(data)
			data='\n'.join(data).replace("{","\n{").replace("}","}\n").split("\n")
			data=[ s.replace("{","\n{\n").replace("}","\n}\n") for s in data ]
			#data = json.load(json_file)
	except:
		data ="Error in opening the file"
		Env="failed to find env create a new one"
	return render(request,'Library/DisplayedData.html',{'data':data,'Env':Env,'file':filename})