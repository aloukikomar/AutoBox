import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//i[@class='icon no-icon-service']//parent::span//parent::button","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='Add']","xpath")
    SeleniumFunction.MoveTo(driver,element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='Add']//parent::a//parent::li//child::p-tieredmenusub//child::ul//child::li//child::span[text()='Normal Mode']//parent::a","xpath")
    SeleniumFunction.Click(element)
    return driver