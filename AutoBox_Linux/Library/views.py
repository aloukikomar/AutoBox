# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.shortcuts import redirect

dir_path = os.path.dirname(os.path.realpath(__file__))
PagePath=dir_path+"/../BDD/Pages/"
PageList=os.listdir(PagePath)

filedata="No File Selected"
TestCasesDir="/home/automation/webapps/"
LogToolBoxRunTests="/tmp/LOG_TOOLBOX_RUNTESTS"
path=TestCasesDir+"AutoBox/BDD/ToRead.txt"
def index(request):
	return HttpResponse("<h1>AddCases</h1>")

def home(request):

	filetoopen=open(path,"r")
	outputfile=filetoopen.readlines()
	PageList=os.listdir(PagePath)
	return render(request,'Library/home.html',{'filedata':filedata,'outputfile':outputfile,'PageList':PageList})

def AddNovelForm(request):
    	ChapterAvailable=os.listdir("/home/automation/webapps/AutoBox/BDD/Chapters")
    	print(ChapterAvailable)
    	return render(request,'Library/AddNovel.html',{'ChapterAvailable':ChapterAvailable})

def AddChapterForm(request):
    	ChapterAvailable=os.listdir("/home/automation/webapps/AutoBox/BDD/Chapters")
    	print(ChapterAvailable)
    	return render(request,'Library/AddChapters.html',{'ChapterAvailable':ChapterAvailable,'PageList':PageList})

def AddPageForm(request):
    	ChapterAvailable=os.listdir("/home/automation/webapps/AutoBox/BDD/Chapters")
    	print(ChapterAvailable)
    	return render(request,'Library/AddPage.html',{'ChapterAvailable':ChapterAvailable})
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