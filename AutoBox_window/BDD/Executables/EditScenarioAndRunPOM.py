
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//button[@title='Add Group']","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//input[@name='groupName']","xpath")
    SeleniumFunction.SendData(driver,element,"G1")
    element=SeleniumFunction.FindElement(driver,"//p-dropdown[@name='scriptName']","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='AutoBox']","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//form[@class='ng-dirty ng-valid ng-touched']//child::footer//child::div//child::button[@label='OK']","xpath")
    SeleniumFunction.Click(driver,element)
    return driver