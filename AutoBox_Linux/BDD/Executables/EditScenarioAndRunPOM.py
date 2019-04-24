
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//button[@title='Add Group']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//input[@name='groupName']","xpath")
    loggs('--------------Running Keyword Enter')
    SeleniumFunction.SendData(driver,element,"G1")
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//p-dropdown[@name='scriptName']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//span[text()='AutoBox']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//form[@class='ng-dirty ng-valid ng-touched']//child::footer//child::div//child::button[@label='OK']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    return driver