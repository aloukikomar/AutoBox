import  datetime
from tmp.TempClasses import temps

def variableCall(variableName):
    try:
        return temps.Stored[variableName]
    except:
        pass


def TimeStamp():
    usestamp=str(datetime.datetime.now())
    usestamp=usestamp.split(" ")[1].split(".")[0]
    return usestamp

def CpFromClipboard():
    from Tkinter import Tk
    root = Tk()
    return root.clipboard_get()