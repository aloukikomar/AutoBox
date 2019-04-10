
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//a[@title='LogOut']","xpath")
    SeleniumFunction.Click(element)
    SeleniumFunction.CloseDriver(driver)
    return driver