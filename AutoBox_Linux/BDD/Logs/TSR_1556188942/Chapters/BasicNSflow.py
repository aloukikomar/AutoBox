from bins.Execute import loggs


def main():
    driver=""
    status=True

    loggs('    |    |----Execution Begins of POM For OpenNetStormWeb')
    from Executables import OpenNetStormWebPOM
    status,driver=OpenNetStormWebPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For OpenNetStormWeb')
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