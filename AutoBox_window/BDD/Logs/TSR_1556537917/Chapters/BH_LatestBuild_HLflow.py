from bins.Execute import loggs


def main():
    driver=""
    status=True

    loggs('    |    |----Execution Begins of POM For OpenBuildHub_Hl')
    from Executables import OpenBuildHub_HlPOM
    status,driver=OpenBuildHub_HlPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For OpenBuildHub_Hl')
    if status != True:
        return False

    loggs('    |    |----Execution Begins of POM For BHLogin')
    from Executables import BHLoginPOM
    status,driver=BHLoginPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For BHLogin')
    if status != True:
        return False

    loggs('    |    |----Execution Begins of POM For BH_ClipboredLatestBuild')
    from Executables import BH_ClipboredLatestBuildPOM
    status,driver=BH_ClipboredLatestBuildPOM.main(driver)
    loggs('    |    |----Execution Ends of POM For BH_ClipboredLatestBuild')
    if status != True:
        return False

    return status