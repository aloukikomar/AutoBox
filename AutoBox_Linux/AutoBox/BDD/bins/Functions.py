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
            '''
            if "Start" in line:
                POMFIle.write("import sys\n")
                POMFIle.write("sys.path.append(\"/home/automation/webapps/AutoBox/BDD\")\n")
                POMFIle.write("from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib")
                POMFIle.write("\n\ndef main(driver):")
                POMFIle.close()
    
            if "Continue" in line:
                POMFIle.write("import sys\n")
                POMFIle.write("sys.path.append(\"/home/automation/webapps/AutoBox/BDD\")\n")
                POMFIle.write("from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib")
                POMFIle.write("\n\ndef main(driver):")
                POMFIle.close()
                IncludeData = open(dir_path+'/../tmp/CurrentIncludes', 'r').read()
                IncludeData=IncludeData.split(",")
                with open(dir_path+'/../tmp/Data.json', 'r') as fp:
                    Data=json.load(fp)
                print("Continue with Data {}".format(Data))
            
            if "Include" in line:
                IncludeData=line.split(" ")[1].split(",")
                for Includes in IncludeData:
                    TempInclude(Includes)
                print(IncludeData)

            if "Run" in line:
                DriverType=line.split(" ")[1]
                FindData=open(dir_path+"/../Data/Settings.json","r").read()
                FindData = json.loads(FindData)
                try:
                    DriverType=FindData[DriverType]
                except:
                    pass
                print(DriverType)
                if "And" not in line :
                    writeline("Run",DriverType,dir_path+'/../Executables/{}'.format(POMName))

            if "Open" in line:
                Site=line.split(" ")[1]
                Data=accureData(Site,IncludeData)
                with open(dir_path+'/../tmp/Data.json', 'w') as fp:
                    json.dump(Data, fp)
                writeline("open",Data,dir_path+'/../Executables/{}'.format(POMName))


            if "LookFor" in line:
                lookfor=line.split(" ")[1]
                xpathforelement=fetchdata(Data,IncludeData,lookfor)
                if "And" not in line :
                    writeline("LookFor",xpathforelement,dir_path+'/../Executables/{}'.format(POMName))

            
            if "Enter" in line:
                Enter=line.split("Enter")[1].split(" ")[1]
                Details=fetchdata(Data,IncludeData,Enter)
                if "And" not in line :
                    writeline("Enter",Details,dir_path+'/../Executables/{}'.format(POMName))
                
            if "WriteHtml" in line:
                Html=line.split("WriteHtml")[1].split(" ")[1]
                Html=fetchdata(Data,IncludeData,Html)
                if "And" not in line :
                    writeline("WriteHtml",Html,dir_path+'/../Executables/{}'.format(POMName))

            if "MoveTo" in line:
                MoveTo=fetchdata(Data,IncludeData,"MoveTo")
                if "And" not in line :
                    writeline("MoveTo",MoveTo,dir_path+'/../Executables/{}'.format(POMName))

            if "Store" in line:
                VName="DefVal"
                store=line.split(" ")[1]
                if "As" in line:
                    VName=line.split("As")[1].split(" ")[1]
                POMFIle=open(dir_path+'/../Executables/{}'.format(POMName),"a+")
                if "@" in store:
                    POMFIle.write("\n    {}={}".format(VName,store[1:]))
                else:
                    POMFIle.write("\n    {}='{}'".format(VName,store))
                POMFIle.close()
                print(line,store,VName)
                Details="'{}|"+VName+"'.format("+VName+")"
                print(Details)
                if "And" not in line :
                    writeline("Store",Details,dir_path+'/../Executables/{}'.format(POMName))

            if "Click" in line:
                print(line)
                Details=fetchdata(Data,IncludeData,"Click")
                print(Details)
                if "And" not in line :
                    writeline("Click",Details,dir_path+'/../Executables/{}'.format(POMName))
            
            if "Upload" in line:
                print(line)
                Upload=line.split(" ")[1]
                if "From" in line:
                    From=line.split("From ")[1].split(" ")[0]
                Upload=Upload+'|'+From
                if "And" not in line :
                    writeline("Upload",Upload,dir_path+'/../Executables/{}'.format(POMName))


            if "Close" in line:
                Close=fetchdata(Data,IncludeData,"Close")
                writeline("Close",Close,dir_path+'/../Executables/{}'.format(POMName))
'''
    POMFIle=open(dir_path+'/../Executables/{}'.format(POMName),"a+")
    POMFIle.write("\n    return driver")    
            
    

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