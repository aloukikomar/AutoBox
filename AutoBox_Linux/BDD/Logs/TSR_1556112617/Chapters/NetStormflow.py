from bins.Execute import loggs
driver=""


loggs('    |    |----Execution Begins of POM For OpenNetStormWeb')

from Executables import OpenNetStormWebPOM
driver=OpenNetStormWebPOM.main(driver)

loggs('    |    |----Execution Ends of POM For OpenNetStormWeb')



loggs('    |    |----Execution Begins of POM For LoginCavisson')

from Executables import LoginCavissonPOM
driver=LoginCavissonPOM.main(driver)

loggs('    |    |----Execution Ends of POM For LoginCavisson')



loggs('    |    |----Execution Begins of POM For HomeGuiNetStormTask1')

from Executables import HomeGuiNetStormTask1POM
driver=HomeGuiNetStormTask1POM.main(driver)

loggs('    |    |----Execution Ends of POM For HomeGuiNetStormTask1')



loggs('    |    |----Execution Begins of POM For ScenariosGuiNetStormTask1')

from Executables import ScenariosGuiNetStormTask1POM
driver=ScenariosGuiNetStormTask1POM.main(driver)

loggs('    |    |----Execution Ends of POM For ScenariosGuiNetStormTask1')



loggs('    |    |----Execution Begins of POM For EditScenarioAndRun')

from Executables import EditScenarioAndRunPOM
driver=EditScenarioAndRunPOM.main(driver)

loggs('    |    |----Execution Ends of POM For EditScenarioAndRun')



loggs('    |    |----Execution Begins of POM For LogoutCavisson')

from Executables import LogoutCavissonPOM
driver=LogoutCavissonPOM.main(driver)

loggs('    |    |----Execution Ends of POM For LogoutCavisson')
