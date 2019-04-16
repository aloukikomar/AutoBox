import sys
sys.path.append("C:\\git\\cavisson\\automation\\ToolBox\\")

from BDD.Core import SeleniumFunction 

driver=SeleniumFunction.SetDriver("Chrome")
SeleniumFunction.openUrl("http://10.10.30.185",driver)
SeleniumFunction.FindElement("xpath",driver,"/html/body/entry/login/div/div[2]/div/form/div[2]/input")