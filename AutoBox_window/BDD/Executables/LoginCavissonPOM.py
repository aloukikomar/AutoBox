
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[2]/input","xpath")
    loggs('--------------Running Keyword Enter')
    SeleniumFunction.SendData(driver,element,"aloukik")
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[3]/input","xpath")
    loggs('--------------Running Keyword Enter')
    SeleniumFunction.SendData(driver,element,"aloukik")
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//*[@id='login-button']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword HandleAlert')
    SeleniumFunction.HandleAlert(driver,"positively")
    return driver