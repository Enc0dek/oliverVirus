import subprocess,getpass

ipconfig = subprocess.check_output("ipconfig").decode("utf-8")
sysinfo = subprocess.check_output("systeminfo").decode("utf-8")
user = getpass.getuser()
password = getpass.getpass()
print(user, password)
def loginfo(*val :object):
    with open("log.txt","w+") as f:
        for i in range(len(val)):
            f.write(val[i-1])
loginfo(ipconfig, sysinfo)