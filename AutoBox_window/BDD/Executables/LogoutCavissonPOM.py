
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//button[@icon='pi pi-caret-down']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//span[text()='Logout']//parent::a","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword Close')
    SeleniumFunction.CloseDriver(driver)
    return driver