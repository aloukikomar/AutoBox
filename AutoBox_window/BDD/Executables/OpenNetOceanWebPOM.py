import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine

def main(driver):
    driver=Comman.Driver("Webapp:Chrome")
    SeleniumFunction.openURL("http://10.10.30.185:8001",driver)
    return driver