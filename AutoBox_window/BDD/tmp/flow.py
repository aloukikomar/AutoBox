from bins.Execute import loggs
driver=""


loggs('    |    |----Execution Begins of POM For OpenNetOceanWeb_Mc_25')

from Executables import OpenNetOceanWeb_Mc_25POM
driver=OpenNetOceanWeb_Mc_25POM.main(driver)

loggs('    |    |----Execution Ends of POM For OpenNetOceanWeb_Mc_25')



loggs('    |    |----Execution Begins of POM For LoginCavisson')

from Executables import LoginCavissonPOM
driver=LoginCavissonPOM.main(driver)

loggs('    |    |----Execution Ends of POM For LoginCavisson')



loggs('    |    |----Execution Begins of POM For LogoutCavisson')

from Executables import LogoutCavissonPOM
driver=LogoutCavissonPOM.main(driver)

loggs('    |    |----Execution Ends of POM For LogoutCavisson')
