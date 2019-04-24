
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//button[@label='Create']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//div[text()='Project ']/parent::div/descendant::p-dropdown[contains(@class,'filterDrop')]","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//span[text()='default']//parent::li","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//div[text()='Scenario Name ']//following::div//child::input","xpath")
    loggs('--------------Running Keyword Enter')
    SeleniumFunction.SendData(driver,element,"NSAutoBoxBegin")
    loggs('--------------Running Keyword LookFor')
    element=SeleniumFunction.FindElement(driver,"//span[@class='ui-button-icon-left ui-clickable fa fa-fw fa-check']/following-sibling::span[text()='Next']","xpath")
    loggs('--------------Running Keyword Click')
    SeleniumFunction.Click(driver,element)
    return driver