
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//button[@label='Create']","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//div[text()='Project ']/parent::div/descendant::p-dropdown[contains(@class,'filterDrop')]","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='default']//parent::li","xpath")
    SeleniumFunction.Click(driver,element)
    element=SeleniumFunction.FindElement(driver,"//div[text()='Scenario Name ']//following::div//child::input","xpath")
    SeleniumFunction.SendData(driver,element,"NSAutoBoxBegin")
    element=SeleniumFunction.FindElement(driver,"//span[@class='ui-button-icon-left ui-clickable fa fa-fw fa-check']/following-sibling::span[text()='Next']","xpath")
    SeleniumFunction.Click(driver,element)
    return driver