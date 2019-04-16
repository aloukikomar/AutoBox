
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    driver=Comman.Driver("Webapp:Chrome")
    driver=Comman.OpenSystem("Web|http://10.10.70.15:8000",driver)
    return driver