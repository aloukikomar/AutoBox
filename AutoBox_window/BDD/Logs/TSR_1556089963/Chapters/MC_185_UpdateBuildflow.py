from bins.Execute import loggs
driver=""


loggs('    |    |----Execution Begins of POM For Blank')

from Executables import BlankPOM
driver=BlankPOM.main(driver)

loggs('    |    |----Execution Ends of POM For Blank')
