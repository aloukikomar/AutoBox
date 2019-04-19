
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    driver=Comman.Driver("Webapp:ChromeHeadless")
    driver=Comman.OpenSystem("Web|http://10.10.30.62:8017",driver)
    return driver