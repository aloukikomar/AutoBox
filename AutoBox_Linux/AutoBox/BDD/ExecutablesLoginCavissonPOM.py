
    element=SeleniumFunction.FindElement(driver,"//input[@name='username']","xpath")
    SeleniumFunction.SendData(element,"netstorm")
    element=SeleniumFunction.FindElement(driver,"//input[@name='password']","xpath")
    SeleniumFunction.SendData(element,"netstorm")
    element=SeleniumFunction.FindElement(driver,"//input[@name='submit']","xpath")
    SeleniumFunction.Click(element)