import json
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

def PreParser(line,count):
        if "@" in line or "{" in line or "$" in line:
                line=line.replace("\n","")
                listline=line.split(" ")
                for word in listline:
                    if ("@" == word[0]) and (")" == word[-1]):
                        function=word[1:]
                        result="PythonFunction_lib.{}".format(function)
                        line=line.replace(word,"@"+result)
                    if "$" == word[0]:
                        #try:
                            result="PythonFunction_lib.variableCall('{}')".format(word[1:])
                            line=line.replace(word,"$"+result)
                        #except:
                            pass
        return line
        print("PreParser Failed")
        return line
