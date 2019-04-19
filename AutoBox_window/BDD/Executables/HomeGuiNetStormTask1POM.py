
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//i[@class='icon produi-icon-scenario']//parent::span//parent::button","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='Scenarios']//parent::a","xpath")
    SeleniumFunction.Click(driver,element)
    return driver