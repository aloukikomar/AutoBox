
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//i[@title='Menu']","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//label[text()='Overview']/parent::span/child::ul/child::li[text()='Last 12 Hours']","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//i[@class='fa fa-pencil']","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//a[text()='Advanced']","xpath")
    SeleniumFunction.Click(element)
    return driver