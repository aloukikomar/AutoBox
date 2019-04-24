from bins.Execute import loggs
driver=""


loggs('    |    |----Executing Begins of POM For OpenNetOceanWeb_Mc_25')

from Executables import OpenNetOceanWeb_Mc_25POM
driver=OpenNetOceanWeb_Mc_25POM.main(driver)

loggs('    |    |----Executing Ends of POM For OpenNetOceanWeb_Mc_25')



loggs('    |    |----Executing Begins of POM For LoginCavisson')

from Executables import LoginCavissonPOM
driver=LoginCavissonPOM.main(driver)

loggs('    |    |----Executing Ends of POM For LoginCavisson')



loggs('    |    |----Executing Begins of POM For LogoutCavisson')

from Executables import LogoutCavissonPOM
driver=LogoutCavissonPOM.main(driver)

loggs('    |    |----Executing Ends of POM For LogoutCavisson')
