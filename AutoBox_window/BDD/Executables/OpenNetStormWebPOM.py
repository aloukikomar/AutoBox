
import sys
sys.path.append("/home/automation/webapps/AutoBox/BDD")
from Core import SeleniumFunction,Comman,Machine,PythonFunction_lib
from bins.Execute import loggs

def main(driver):
    loggs('--------------Running Keyword Run')
    driver=Comman.Driver("Webapp:ChromeHeadless")
    loggs('--------------Running Keyword Open')
    driver=Comman.OpenSystem("Web|http://10.10.30.185",driver)
    return driver