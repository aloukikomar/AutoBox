
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib

def main(driver):
    driver=Comman.Driver("Machine:linux")
    driver=Comman.OpenSystem("Machine|10.10.70.15|cavisson|cavisson",driver)
    return driver