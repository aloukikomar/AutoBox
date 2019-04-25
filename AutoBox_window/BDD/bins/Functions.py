import json,os
from bins.write import writeline,TempInclude
from bins.PreParser import PreParser
from bins.Compile import MainCompiler
dir_path = os.path.dirname(os.path.realpath(__file__))
'''from bins.MakePOMCode import ConverToPOM'''

def CreateEXE(page):
    open(dir_path+'/../Executables/{}POM.py'.format(page),"w+")
    return '{}POM.py'.format(page)

def WriteEXE(lines,POMName):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    open(dir_path+"/../Logs/{}/Test.Report".format(TSR),"a+").write("\n--Writing Executable {}".format(POMName))
    POMFIle=open(dir_path+'/../Executables/{}'.format(POMName),"w+")
    POMFIle.write("")
    for line in lines:
            MainCompiler(line,POMName)
    POMFIle=open(dir_path+'/../Executables/{}'.format(POMName),"a+")
    POMFIle.write("\n    return status,driver")
    POMFIle.close()    
            
    

def fetchdata(Data,IncludeData,lookfor):
    for DataSet in IncludeData:
        try:
            return Data[DataSet][lookfor]
        except:
            pass
        

def accureData(Site,includs):
    Fdata={}
    for dataSource in includs:
        try:
            json_data=open(dir_path+"/../Data/{}".format(dataSource)).read()
            data = json.loads(json_data)
            Fdata[dataSource]=data[Site]
        except:
            pass
    return Fdata 