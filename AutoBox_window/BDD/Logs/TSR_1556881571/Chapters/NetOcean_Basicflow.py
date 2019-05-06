from bins.Execute import loggs


def main():
    driver=""
    status=True

    loggs('    |    |----Execution Begins of POM For OpenNetOceanWeb_Mc_25')
    from Executables import OpenNetOceanWeb_Mc_25POM
    status,driver=OpenNetOceanWeb_Mc_25POM.main(driver)
    loggs('    |    |----Execution Ends of POM For OpenNetOceanWeb_Mc_25')
    if status != True:
        return False

    loggs('    |    |----Execution Begins of POM For LoginCavisson')
    from Executables import LoginCavissonPOM
    status,driver=LoginCavissonPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For LoginCavisson')
    if status != True:
        return False

    loggs('    |    |----Execution Begins of POM For LogoutCavisson')
    from Executables import LogoutCavissonPOM
    status,driver=LogoutCavissonPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For LogoutCavisson')
    if status != True:
        return False

    return status