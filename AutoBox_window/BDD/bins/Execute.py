import shutil,time,os

def loggs(message):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Test.Report".format(TSR),"a+")
    flow.write("\n"+message)
    flow.close()

def DevLogs(message):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/DevLogs.txt".format(TSR),"a+")
    flow.write("\n"+message)
    flow.close()

dir_path = os.path.dirname(os.path.realpath(__file__))

def MakeFlow(Chapter):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),"a+")
    flow.write("from bins.Execute import loggs\n")
    flow.write("\n\ndef main():\n")
    flow.write("    driver=\"\"\n    status=True")
    flow.close()

def WriteFlow(Chapter,page):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),"a+")
    flow.write("\n")
    flow.write("\n    loggs('    |    |----Execution Begins of POM For {}')\n".format(page))
    flow.write("    from Executables import {}POM\n".format(page))
    flow.write("    status,driver={}POM.main(driver)\n".format(page))
    flow.write("    loggs('    |    |----Execution Ends of POM For {}')\n".format(page))
    flow.write("    if status != True:\n        return False")
    '''flow.write("\nexcept:\n    print('failed in {}')".format(page))'''
    flow.close()

def FinishWritingFlow(Chapter):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),"a+")
    flow.write("\n")
    flow.write("\n    return status")
    flow.close()

def ExecuteFlow(Chapter):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    shutil.copy(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),dir_path+"/../tmp/{}flow.py".format(Chapter))
    time.sleep(3)
    exec("from tmp import {}flow as flow".format(Chapter))
    status=flow.main()
    print(status)
    os.remove(dir_path+"/../tmp/{}flow.py".format(Chapter))
    os.remove(dir_path+"/../tmp/{}flow.pyc".format(Chapter))
    return status
    #execfile(dir_path+"/../tmp/flow.py")
    
   
