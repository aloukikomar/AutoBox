
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//i[@class='icon produi-icon-scenario']//parent::span//parent::button","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//span[text()='Scenarios']//parent::a","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    return driver