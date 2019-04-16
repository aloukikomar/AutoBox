
    element=SeleniumFunction.FindElement(driver,"variable","xpath")
    SeleniumFunction.Click(element)
    Comman.Store(variable)
    element=SeleniumFunction.FindElement(driver,"//button[@aria-label='Search']","xpath")
    SeleniumFunction.Click(element)
    Comman.Store()