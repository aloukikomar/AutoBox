import os,sys,time
print(time.time())
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from bins.Functions import CreateEXE,WriteEXE
from bins.Execute import MakeFlow,ExecuteFlow,WriteFlow,FinishWritingFlow

dir_path = os.path.dirname(os.path.realpath(__file__))
ToReadFile=dir_path+"/../BDD/ToRead.txt"
def RunFlow():
    TSR=open(dir_path+"/..//BDD/tmp/CurrentTSR","r").readline()
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n--------------------\nExecute the flow \n--------------------")
    data=open(ToReadFile,"r").readlines()
    NovelCount=0
    NovelSucc=0
    NovelFail=0
    for novel in data:
        NovelCount=NovelCount + 1
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n Executing Novel :{}".format(novel))
        novel=open(dir_path+"/../BDD/Novels/{}/ChapterIndex.txt".format(novel),"r").readlines()
        ChapterCount=0
        ChapterSucc=0
        ChapterFail=0
        for Chapter in novel:
            ChapterCount=ChapterCount +1
            Chapter=Chapter.replace("\n","").replace("\r","")
            open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n    |--Executing Chapter:{}\n".format(Chapter))
            Pages=open(dir_path+"/../BDD/Chapters/{}/PageIndex.txt".format(Chapter),"r").readlines()
            MakeFlow(Chapter)
            for page in Pages:
                page=page.replace("\r","").replace("\n","")
                WriteFlow(Chapter,page)
            FinishWritingFlow(Chapter)
            status=ExecuteFlow(Chapter)
            if status == True:
                ChapterSucc=ChapterSucc +1
                open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n    |--Chapter:{} Pass\n".format(Chapter))
            else:
                ChapterFail=ChapterFail +1
                open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n    |--Chapter:{} Fails\n".format(Chapter))
        print(ChapterCount,ChapterSucc,ChapterFail)
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n Novel:{}\n Execution Completed".format(novel))
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n======================================================================")
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n Novel Result: Total Chapters:{} Total Succes:{} Total Faliurs:{}\n".format(ChapterCount,ChapterSucc,ChapterFail))
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n======================================================================")
        try:
            persentSucc=(ChapterSucc/ChapterCount)*100
        except:
            print("error in calculating persentage")
        if ChapterCount == ChapterSucc:
            NovelSucc=NovelSucc + 1    
        else:
            NovelFail=NovelFail + 1
    print(NovelCount,NovelSucc,NovelFail)
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n TSR Result: {}\n Execution Completed".format(TSR))
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n======================================================================")
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n TSR Result: Total Novels:{} Total Succes:{} Total Faliurs:{}\n".format(NovelCount,NovelSucc,NovelFail))
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n======================================================================") 

def MakeDirs(LogDir):
    os.mkdir( dir_path+"/../BDD/Logs/{}".format(LogDir), 0755 )
    os.mkdir( dir_path+"/../BDD/Logs/{}/Novels".format(LogDir), 0755 )
    os.mkdir( dir_path+"/../BDD/Logs/{}/Chapters".format(LogDir), 0755 )
    os.mkdir( dir_path+"/../BDD/Logs/{}/Pages".format(LogDir), 0755 )
    os.mkdir( dir_path+"/../BDD/Logs/{}/Images".format(LogDir), 0755 )

def MakeLog():
    LogDir="TSR_"+str(time.time()).split(".")[0]
    MakeDirs(LogDir)
    open(dir_path+"/../BDD/tmp/CurrentTSR","w+").write(LogDir)
    logBegin=open(dir_path+"/../BDD/Logs/{}/Test.Report".format(LogDir),"w+")
    logBegin.write("\n==========================|Test Report :{}|========================\n".format(LogDir))
    logBegin.close()
    flow=open(dir_path+"/../BDD/Logs/{}/DevLogs.txt".format(LogDir),"w+")
    flow.write("\n===|Dev Logs :{}|===============================================\n".format(LogDir))
    flow.close()
    open(dir_path+'/../BDD/tmp/Variables.json', 'w+').write("")

def ReadPage(Pages):
    TSR=open(dir_path+"/../BDD/tmp/CurrentTSR","r").readline()
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n--Reading Lines")
    newlines=[]
    lines=open(dir_path+"/../BDD/Pages/{}.txt".format(Pages),"r").readlines()
    for line in lines:
        line=line.replace("\n","").replace("\r","")
        newlines.append(line)
    return newlines

def ToRead():
    TSR=open(dir_path+"/../BDD/tmp/CurrentTSR","r").readline()
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n\n---------\nTree:\n---------")
    ChapterFlow=[]
    allChapters=[]
    allPages=[]
    data=open(ToReadFile,"r").readlines()
    for novel in data:
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n + {}".format(novel))
        novel=open(dir_path+"/../BDD/Novels/{}/ChapterIndex.txt".format(novel),"r").readlines()
        novelFlow=novel
        for Chapter in novel:
            Chapter=Chapter.replace("\n","").replace("\r","")
            allChapters.append(Chapter)
            open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n    |--{}\n".format(Chapter))
            Pages=open(dir_path+"/../BDD/Chapters/{}/PageIndex.txt".format(Chapter),"r").readlines()
            for page in Pages:
                open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("    |    |----{}".format(page))
                page=page.replace("\r","").replace("\n","")
                ChapterFlow.append(page)
                if page not in allPages:
                    allPages.append(page)
    return allChapters,allPages        

def makeExecutables(allPages):
    TSR=open(dir_path+"/../BDD/tmp/CurrentTSR","r").readline()
    open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\n-----------------------------------\nMake Executable files\n-----------------------------------\nList:{}".format(allPages))
    for page in allPages:
        POMName=CreateEXE(page)
        open(dir_path+"/../BDD/Logs/{}/Test.Report".format(TSR),"a+").write("\nExecutable Creation for {} begins".format(page))
        page=page.replace("\n","").replace("\r","")
        lines=ReadPage(page)
        WriteEXE(lines,POMName)

        
#MakeLog()
#allChapters,allPages=ToRead()
#makeExecutables(allPages)
#RunFlow()