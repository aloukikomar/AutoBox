
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[2]/input","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Enter')
    status=SeleniumFunction.SendData(driver,element,"aloukik")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[3]/input","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Enter')
    status=SeleniumFunction.SendData(driver,element,"aloukik")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//*[@id='login-button']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword HandleAlert')
    SeleniumFunction.HandleAlert(driver,"positively")
    if status != True:
        return status,driver
    return status,driver