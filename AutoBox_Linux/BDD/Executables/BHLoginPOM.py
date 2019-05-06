
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//a[contains(text(),'Login')]","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//input[@placeholder='User-Id']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Enter')
    status=SeleniumFunction.SendData(driver,element,"cavisson")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//input[@placeholder='Password']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Enter')
    status=SeleniumFunction.SendData(driver,element,"cavisson")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//button[@id='submit']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    return status,driver