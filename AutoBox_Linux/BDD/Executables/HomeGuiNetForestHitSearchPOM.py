
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//button[@aria-label='Search']","xpath")
    SeleniumFunction.Click(element)
    PsudoStore=PythonFunction_lib.TimeStamp()
    Comman.Store("{}|HitTime".format(PsudoStore))
    Comman.PrintContent(PythonFunction_lib.variableCall('HitTime'))
    return driver