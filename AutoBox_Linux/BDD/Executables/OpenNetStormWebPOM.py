import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine

def main(driver):
    driver=Comman.Driver("Webapp:Chrome")
    driver=Comman.OpenSystem("Web|http://10.10.30.185",driver)
    return driver