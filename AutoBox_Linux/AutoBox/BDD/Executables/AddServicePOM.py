import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman

def main(driver):
    element=SeleniumFunction.FindElement(driver,"//span[text()='Service Name:']/following-sibling::input","xpath")
    SeleniumFunction.SendData(element,"AutoBoxData")
    element=SeleniumFunction.FindElement(driver,"//span[text()=' URL:']/following-sibling::input","xpath")
    SeleniumFunction.SendData(element,"/AutoBox")
    element=SeleniumFunction.FindElement(driver,"//span[text()='Template Name:']/following-sibling::input","xpath")
    SeleniumFunction.SendData(element,"temp")
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/app-root/app-netocean-add-services/div[2]/div/p-accordion/div/p-accordiontab/div[2]/div/div/div/div[1]/div[2]/codemirror/div/div[6]/div[1]/div/div/div/div[5]/div/pre/span","xpath")
    SeleniumFunction.WriteHtml(driver,element,"Req")
    element=SeleniumFunction.FindElement(driver,"/html/body/entry/app-root/app-netocean-add-services/div[2]/div/p-accordion/div/p-accordiontab/div[2]/div/div/div/div[2]/div[2]/codemirror/div/div[6]/div[1]/div/div/div/div[5]/div/pre/span","xpath")
    SeleniumFunction.WriteHtml(driver,element,"Res")
    element=SeleniumFunction.FindElement(driver,"//span[text()='Add']/parent::button","xpath")
    SeleniumFunction.Click(element)
    return driver