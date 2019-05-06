
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//a[contains(text(),'UBUNTU 16')]","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"(//a[@class='accordion-toggle'])[1]","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//div[@id='2b']//div[1]//div[1]//table[1]//tbody[1]//tr[3]//td[5]//div[1]//div[1]//button[1]","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    PsudoStore=PythonFunction_lib.CpFromClipboard()
    if status != True:
        return status,driver
    loggs('--------------Running Keyword MoveTo')
    status=Comman.Store("{}|link".format(PsudoStore))
    if status != True:
        return status,driver
    return status,driver