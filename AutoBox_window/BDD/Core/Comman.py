from SeleniumFunction import SetDriver,openURL
from Machine import ConncetMachine,MachineDriver
from tmp.TempClasses import temps
import Core.PythonFunction_lib
import time,os,json
dir_path = os.path.dirname(os.path.realpath(__file__))

def Driver(TypeD): 
    try:
        TypeD=TypeD.split(":")
        if TypeD[0] == "Webapp":
            print("webapp")
            driver=SetDriver(TypeD[1])
        if TypeD[0] == "Machine":
            print("Machine")
            driver=MachineDriver()
        status=True
        return status,driver
    except:
        print("crashed")
        status=False
        driver=""
        return status,driver

def OpenSystem(option,driver):
    try:
        option=option.split("|")
        if option[0] == "Web":
            driver=openURL(option[1],driver)
        if option[0] == "Machine":
            driver=ConncetMachine(driver,option[1],option[2],option[3])
        status=True
        return status,driver
    except:
        status=False
        driver=""
        return status,driver

def Wait5():
    try:
        time.sleep(5)
        print("sleep")
        status=True
        return status
    except:
        status=False
        return status

def Store(value):
    try:
        store=value.split("|")[0]
        Vname=value.split("|")[1]
        Data={Vname:store}
        temps.Stored[Vname]=store
        print(temps.Stored[Vname])
        with open(dir_path+'/../tmp/Variables.json', 'a+') as fp:
            json.dump(Data, fp)
        status=True
        return status
    except:
        status=False
        return status
    

def PrintContent(Content):
    try:
        print(Content)
        status=True
        return status
    except:
        status=False
        return status