
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//button[@label='Create']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//div[text()='Project ']/parent::div/descendant::p-dropdown[contains(@class,'filterDrop')]","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//span[text()='default']//parent::li","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//div[text()='Scenario Name ']//following::div//child::input","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Enter')
    status=SeleniumFunction.SendData(driver,element,"NSAutoBoxBegin")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword LookFor')
    status,element=SeleniumFunction.FindElement(driver,"//span[@class='ui-button-icon-left ui-clickable fa fa-fw fa-check']/following-sibling::span[text()='Next']","xpath")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Click')
    status=SeleniumFunction.Click(driver,element)
    if status != True:
        return status,driver
    return status,driver