
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    status=True

    if status != True:
        return status,driver
    loggs('--------------Running Keyword Run')
    status,driver=Comman.Driver("Webapp:ChromeHeadless")
    if status != True:
        return status,driver
    loggs('--------------Running Keyword Open')
    status,driver=Comman.OpenSystem("Web|http://10.10.30.185",driver)
    if status != True:
        return status,driver
    return status,driver