from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import time,os
from selenium.webdriver.chrome.options import Options
dir_path = os.path.dirname(os.path.realpath(__file__))
def getpath():
        #print(dir_path)
        TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
        paths=dir_path+"/../Logs/{}/Images/".format(TSR)
        print(paths)
        return paths
        #flow.write("driver=\"\"")
        #flow.close()

def FindElement(driver,variable,types):
    if types == "xpath":
        element=driver.find_element_by_xpath(variable)
        print("find element for {} {}".format(variable,element))
    return element


def SetDriver(DriverType):
    if DriverType == "Chrome":
                print("chrome")
                driver=webdriver.Chrome("/home/automation/webapps/AutoBox/BDD/bins/Drivers/chromedriver")
    if DriverType == "ChromeHeadless":
                print("ChromeHeadless",dir_path)
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')  # Last I checked this was necessary.
                driver = webdriver.Chrome(dir_path+"/../bins/Drivers/chromedriver", chrome_options=options)
                driver.set_window_size(1920, 1080)
    return driver
        
def openURL(URL,driver):
    print(URL)
    driver.get(URL)
    paths=getpath()
    timestamp=str(str(time.time()).split(".")[0])
    driver.save_screenshot(paths+timestamp+"HitURL.png")
    return driver
    
def SendData(driver,element,Fill):
        element.send_keys(Fill)
        paths=getpath()
        timestamp=str(str(time.time()).split(".")[0])
        driver.save_screenshot(paths+timestamp+"SendData.png")

def Click(driver,element):
        time.sleep(1)
        paths=getpath()
        timestamp=str(str(time.time()).split(".")[0])
        driver.save_screenshot(paths+timestamp+"Click.png")
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