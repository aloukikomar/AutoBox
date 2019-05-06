
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//button[@icon='pi pi-caret-down']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//span[text()='Logout']//parent::a","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Close')
    status=SeleniumFunction.CloseDriver(driver)
    if status != True:
        return status,driver
    return status,driver