
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//div[@title='Analytics']","xpath")
    SeleniumFunction.Click(element)
    SeleniumFunction.SwitchTab(driver)
    return driver