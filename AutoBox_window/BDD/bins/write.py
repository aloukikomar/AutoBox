import json,os
dir_path = os.path.dirname(os.path.realpath(__file__))

def TempInclude(includes):
    open(dir_path+"/../tmp/CurrentIncludes","a+").write(",{}".format(includes))

def writecode(Fdata,files):
    codefile=open(dir_path+"/../Executables/"+files,"a+")
    codefile.write("\n")
    for code in Fdata:    
        codefile.write(code)
    

def createVariable(lines,Data):
    line=lines.split("(")[1].split(")")[0].split(",")
    k =Data.keys()
    for variable in line:
        for key in k:
            val=Data.get(key)
            val=val.get(variable)
            if "None" not in val:
                 return "{}=\"{}\"".format(variable,val)
        
def writepera(use,Data,file,data):
    try:
        Fdata=data["pera"][use][Data]
        codefile=open(file,"a+")
        print(Fdata)
        for code in Fdata:
            codefile.write("\n")
            codefile.write(code)
            
    except:
        print("fata {} Data:{}".format(use,data))


def newWrite(Type,FileName,use,*Args):
    json_data=open(dir_path+"/../Data/CreateData.json").read()
    data = json.loads(json_data)
    try:
            line=data['line'][use]
    except:
        try:
            line=data['pera'][use]
        except:
            print('not required/found')
            return
    if Type == "Static":
        variable='-'
        for arg in Args:
            variable=variable+'|'+arg
        variable=variable[2:]
        #try:
        if '$' in variable:
                line=line.replace('"variable"',variable[1:]) 
        else:
                line=line.replace("variable",variable)
        print(line)
        writecode(line,FileName)
        #except:
        pass
    if Type == "Hybrid":
        try:
            line=line.replace("variable","{\}|").replace("\\","")
            line=line.replace("|","|{}".format(Args[1]))
            line=line.replace('")','".format({}))'.format(Args[0]))
            print(line)
            writecode(line,FileName)
        except:
            print("Hybrid failed")


def writeline(use,Data,file):
    Fdata={}
    json_data=open(dir_path+"/../Data/CreateData.json").read()
    data = json.loads(json_data)
    if Data is None:
        Fdata=data["line"][use]
        writecode(Fdata,file)
        print(Fdata,use,Data,file)
        return
        
    if type(Data) is dict:
        k =Data.keys()
        for key in k:
            try:
                val=Data.get(key)
                val=val.get("url")
                if "None" not in val:
                    Data1=val
            except:
                pass
            try:
                val=Data.get(key)
                val=val.get("type")
                if "None" not in val:
                    Data2=val
            except:
                pass
        Data=Data2 +"|"+ Data1

    try:
        Fdata=data["line"][use]
        try:
            Fdata=Fdata.replace("variable",Data)
        except:
            pass
        writecode(Fdata,file)
    except:        
        writepera(use,Data,file,data)
    return Fdata 
        
    