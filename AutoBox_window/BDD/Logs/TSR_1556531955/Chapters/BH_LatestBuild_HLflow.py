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

    return status