
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    Machine.UploadFile("")
    PsudoStore=NFAPI
    Comman.Store("{}|ApiData".format(PsudoStore))
    return driver