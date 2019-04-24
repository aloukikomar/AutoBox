import json,os
from bins.write import writeline,TempInclude,newWrite
from bins.PreParser import PreParser

class variables:
    
    Libraries="UserData.json"
    App=""

    def CurrentData(self,Libraries,Value):
        Libraries=Libraries.split(",")
        for lib in Libraries:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            data=open(dir_path+'/../Data/{}'.format(lib),'r').read()
            Data=json.loads(data)
            App=self.App
            if self.App == '' :
                try:
                    if Data[Value]:
                        print("Try One\n\n")
                        return Data[Value]
                except:
                    print("Try One Failed\n\n")
            else:
                try:
                    
                    if Data[App]:
                        try:
                            print("try t\n\n")
                            return Data[App][Value]
                        except:
                            print("Try t failed\n\n")
                except:
                    print("Try t main failed\n\n")
        return Data
    
    
def MakeRawData(*vari):
    content=vari[0]
    if '"' in content:
        content=content.split('"')[1]
    else:
        content=variables().CurrentData(vari[1],content)
    return content

def writeCode(FileName,*Args):
    if len(Args) > 1:
        print(Args[1],"-----------")
    if len(Args) > 2:
        print(Args[2],"=-=-=-=")

def PreCompiler(Line):
    print(Line)
    return Line

def MainCompiler(Line,POMFIle):
    print(Line)
    FileName=POMFIle
    Line=PreParser(Line,0)
    print(Line)
    if "Start" in Line:
        newWrite('Static',FileName,'Start')

    if "Continue" in Line:
        newWrite('Static',FileName,'Continue')

    if "Include" in Line:
        Libraries=Line.split("Include ")[1].split(" ")[0]
        Libraries=MakeRawData(Libraries)
        variables.Libraries=Libraries
        newWrite('Static',FileName,'Include',Libraries)

    if "Run" in Line:
        App=Line.split("Run ")[1].split(" ")[0]
        App=variables().CurrentData("Settings.json",App)
        newWrite('Static',FileName,'Run',App)

    if "Open" in Line:
        App=Line.split("Open ")[1].split(" ")[0]
        AppName=App
        App=variables().CurrentData("UserData.json",App)
        variables.App=AppName
        Type=App['type']
        App=App['url']
        newWrite('Static',FileName,'Open',Type,App)

    if "LookFor" in Line:
        LookFor=Line.split("LookFor ")[1].split(" ")[0]
        LookFor=MakeRawData(LookFor,"Xpath.json")
        newWrite('Static',FileName,'LookFor',LookFor)
    
    if "Enter" in Line:
        Enter=Line.split("Enter ")[1].split(" ")[0]
        Enter=MakeRawData(Enter,"UserData.json")
        newWrite('Static',FileName,'Enter',Enter)

    if "WriteHtml" in Line:
        newWrite('Static',FileName,'Continue')

    if "MoveTo" in Line:
        newWrite('Static',FileName,'Continue')

    if "Store" in Line:
        VName="DefVal"
        Store=Line.split("Store ")[1].split(" ")[0]
        if "As" in Line:
                VName=Line.split("As")[1].split(" ")[1]
        if "@" in Store:
            newWrite('Static',FileName,'PsudoStore',Store[1:])
            Store="PsudoStore"
            newWrite('Hybrid',FileName,'Store',Store,VName)  
        else:
            newWrite('Static',FileName,'Store',Store,VName)

    if "PrintContent" in Line:
        PrintContent=Line.split("PrintContent ")[1].split(" ")[0]
        newWrite('Static',FileName,'PrintContent',PrintContent)

    if "Click" in Line:
        newWrite('Static',FileName,'Click')
    
    if "SwitchTab" in Line:
        newWrite('Static',FileName,'SwitchTab')

    if "Upload" in Line:
        newWrite('Static',FileName,'Upload')
        
    if "Close" in Line:
        variables.App=''
        newWrite('Static',FileName,'Close')

    if "HandleAlert" in Line:
        HandleAlert=Line.split("HandleAlert ")[1].split(" ")[0]
        HandleAlert=MakeRawData(HandleAlert,"Xpath.json")
        newWrite('Static',FileName,'HandleAlert',HandleAlert)
        
    if "Wait5" in Line:
        newWrite('Static',FileName,'Wait5')
