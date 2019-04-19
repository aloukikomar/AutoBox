
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[2]/input","xpath")
    SeleniumFunction.SendData(driver,element,"cavisson")
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/login/div/div[2]/div/form/div[3]/input","xpath")
    SeleniumFunction.SendData(driver,element,"@dmin")
    element=SeleniumFunction.FindElement(driver,"//*[@id='login-button']","xpath")
    SeleniumFunction.Click(driver,element)
    return driver