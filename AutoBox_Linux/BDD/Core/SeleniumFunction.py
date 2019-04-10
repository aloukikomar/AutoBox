from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import time

def FindElement(driver,variable,types):
    if types == "xpath":
        element=driver.find_element_by_xpath(variable)
        print("find element for {} {}".format(variable,element))
    return element


def SetDriver(DriverType):
    if DriverType == "Chrome":
                print("chrome")
                driver=webdriver.Chrome("/home/automation/webapps/AutoBox/BDD/bins/Drivers/chromedriver")
    return driver
        
def openURL(URL,driver):
    print(URL)
    driver.get(URL)
    return driver
    
def SendData(element,Fill):
        element.send_keys(Fill)

def Click(element):
        time.sleep(1)
        try:
                element.click()
                time.sleep(4)
                print("Click {}".format(element))
        except exceptions.StaleElementReferenceException as e:
                print(e)  
        time.sleep(7)

def MoveTo(driver,element):
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(3)

def WriteHtml(driver,element,Data):
        driver.execute_script("arguments[0].innerHTML = arguments[1];", element,Data)

def CloseDriver(driver):
        driver.close()

def Store(element):
        data=element.getText()
        print(data)

def SwitchTab(driver):
        driver.switch_to_window(driver.window_handles[-1])