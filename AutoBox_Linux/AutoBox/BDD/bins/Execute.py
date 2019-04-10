import shutil,time,os
dir_path = os.path.dirname(os.path.realpath(__file__))

def MakeFlow(Chapter):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),"a+")
    flow.write("driver=\"\"")
    flow.close()

def WriteFlow(Chapter,page):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    flow=open(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),"a+")
    flow.write("\n\n")
    flow.write("\nfrom Executables import {}POM\n".format(page))
    flow.write("driver={}POM.main(driver)\n".format(page))
    '''flow.write("\nexcept:\n    print('failed in {}')".format(page))'''
    flow.close()

def ExecuteFlow(Chapter):
    TSR=open(dir_path+"/../tmp/CurrentTSR","r").readline()
    shutil.copy(dir_path+"/../Logs/{}/Chapters/{}flow.py".format(TSR,Chapter),dir_path+"/../tmp/flow.py")
    time.sleep(3)
    
    execfile(dir_path+"/../tmp/flow.py")
    
   
