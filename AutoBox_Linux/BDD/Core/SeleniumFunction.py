from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import time,os
from selenium.webdriver.chrome.options import Options
from bins.Execute import DevLogs,loggs
import traceback

dir_path = os.path.dirname(os.path.realpath(__file__))
def getpath():
        #print(dir_path)
        TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
        paths=dir_path+"/../Logs/{}/Images/".format(TSR)
        DevLogs("getpath invoked and returns :{}".format(paths))
        return paths
        #flow.write("driver=\"\"")
        #flow.close()

def FindElement(driver,variable,types):
        DevLogs("FindElement invoked ")
        try:
                DevLogs("type invoked  :{}".format(types))
                if types == "xpath":
                        element=driver.find_element_by_xpath(variable)
                        DevLogs("Find element for :{}\n{}".format(variable,element))
                        status=True
                        return status,element
                        #print(" {} {}".format(variable,element))
        except:
                loggs("\n\nFind Element Failed for :{}\n".format(variable))
                DevLogs("\n\n\nFind Element Failed :\n{}\n\n\n".format(traceback.format_exc()))
                element=""
                return False,element


def SetDriver(DriverType):
        try:
                if DriverType == "Chrome":
                        driver=webdriver.Chrome(dir_path+"/../bins/Drivers/chromedriver")
                        print("chrome")
                if DriverType == "ChromeHeadless":
                        print("ChromeHeadless",dir_path)
                        options = Options()
                        options.add_argument('--headless')
                        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
                        driver = webdriver.Chrome(dir_path+"/../bins/Drivers/chromedriver", chrome_options=options)
                        driver.set_window_size(1800, 1000)
        except:
                print(traceback.format_exc())
        return driver
        
def openURL(URL,driver):
    print(URL)
    driver.get(URL)
    paths=getpath()
    timestamp=str(str(time.time()).split(".")[0])
    driver.save_screenshot(paths+timestamp+"HitURL.png")
    return driver
    
def SendData(driver,element,Fill):
        try:
                element.send_keys(Fill)
                paths=getpath()
                timestamp=str(str(time.time()).split(".")[0])
                driver.save_screenshot(paths+timestamp+"SendData.png")
                return True
        except:
                return False

def Click(driver,element):
        try:
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
                return True
        except:
                return False

def MoveTo(driver,element):
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(3)

def WriteHtml(driver,element,Data):
        driver.execute_script("arguments[0].innerHTML = arguments[1];", element,Data)

def CloseDriver(driver):
        try:
                driver.close()
                return True
        except:
                return False

def Store(element):
        data=element.getText()
        print(data)

def SwitchTab(driver):
        driver.switch_to_window(driver.window_handles[-1])

def HandleAlert(driver,option):
        try:
                
                if option == "positively":
                        driver.switch_to_alert().accept()
                else:
                        driver.switch_to_alert().dismiss()
                paths=getpath()
                timestamp=str(str(time.time()).split(".")[0])
                driver.save_screenshot(paths+timestamp+"HandleAlert.png")
                return True
        except:
                print("No alerts")
                return False