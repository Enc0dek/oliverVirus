import subprocess

try:
    ipconfig = subprocess.check_output("ipconfig").decode("utf-8")
finally:
    with open("log.txt","w+") as f:
        f.write(ipconfig)