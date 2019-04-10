import paramiko

def MachineDriver():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return ssh
    except Exception as e :
        print(e.message)
        final_output="error to connect"
    
def ConncetMachine(ssh,hostname,username,password):
    try:
        ssh.connect(hostname,username=username , password=password)
        print("Conncet to %s"%hostname)
        print("connected")
        return ssh
    except Exception as e :
        print(e.message)
        final_output="error to connect"
    
def BashShell(driver,files):
    try:
        print("Bashing file {}".format(files))
        perform(driver,"bash",files,arguments)

    except:
            pass

def perform(ssh,task):
    try:
        print("performing ")
        stdin, stdout, stderr = ssh.exec_command("sed -i '/{}$/d' {} && echo '{}' >>{}".format(name,readersFile,name,writersFile))
        err = ''.join(stderr)
        out = ''.join(stdout)
        final_output2 = str(out) + str(err)
        print(final_output2)
        print("Following is the writers file")
        open('tmp/processLogAll', 'a+').write("enabled for {}\n".format(name))
        open('tmp/processLog', 'w').write("enabled for {}\n".format(name))
    except Exception as e:
        print(e.message)
        final_output="error to cat"
        print(name)

def UploadFile(Variable):
        From=Variable.split("|")[1]
        To=Variable.split("|")[0]
        out = subprocess.Popen(['scp','-r','{}'.format(From),'{}'.format(To)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(out)

def storeVar():
    print "store"