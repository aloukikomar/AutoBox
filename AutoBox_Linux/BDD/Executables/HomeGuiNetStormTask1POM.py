import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//i[@class='icon produi-icon-scenario']//parent::span//parent::button","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='Scenarios']//parent::a","xpath")
    SeleniumFunction.Click(element)
    return driver