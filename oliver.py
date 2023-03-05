import subprocess,getpass,os,glob
# vars
rootuser = getpass.getuser()
rootdirectory = fr"C:\Users\{rootuser}"

# to log
ipconfig = subprocess.check_output("ipconfig").decode("utf-8")
sysinfo = subprocess.check_output("systeminfo").decode("utf-8")
docs = subprocess.check_output(fr"dir C:\Users\{rootuser}\OneDrive\Documentos /s").decode("utf-8")
def loginfo(*val :object):
    with open("log.txt","w+") as f:
        for i in range(len(val)):
            f.write(val[i-1])
loginfo(ipconfig, sysinfo, docs)