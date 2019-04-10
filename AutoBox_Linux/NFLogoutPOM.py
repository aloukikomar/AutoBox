
    element=SeleniumFunction.FindElement(driver,"variable","xpath")
    SeleniumFunction.Click(element)
    Machine.UploadFile("variable")
    element=SeleniumFunction.FindElement(driver,"//a[@title='LogOut']","xpath")
    SeleniumFunction.Click(element)
    Machine.UploadFile("")