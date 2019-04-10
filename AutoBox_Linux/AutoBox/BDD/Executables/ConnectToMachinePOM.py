import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine

def main(driver):
    driver=Comman.Driver("Machine:linux")
    driver=Comman.OpenSystem("Machine|10.10.30.185|cavisson|cavisson",driver)
    return driver