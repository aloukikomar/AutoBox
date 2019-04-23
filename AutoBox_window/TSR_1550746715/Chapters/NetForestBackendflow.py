driver=""


from Executables import SetNetForestMachinePOM
driver=SetNetForestMachinePOM.main(driver)



from Executables import GetVerificationDataPOM
driver=GetVerificationDataPOM.main(driver)



from Executables import VerifyPOM
driver=VerifyPOM.main(driver)



from Executables import MachineClosePOM
driver=MachineClosePOM.main(driver)
