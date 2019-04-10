
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//button[@icon='fa-caret-down']","xpath")
    SeleniumFunction.Click(element)
    element=SeleniumFunction.FindElement(driver,"//span[text()='Logout']//parent::a","xpath")
    SeleniumFunction.Click(element)
    SeleniumFunction.CloseDriver(driver)
    return driver