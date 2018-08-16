import subprocess
import time
import os

cmd = "ps -aux | grep 'main.py' | grep -v 'grep'"
cmd2 = "python3 /home/test/sf-mail-notify/main.py &"
text = "/home/test/sf-mail-notify/main.py"

def date():
    Time = time.strftime("%d-%m-%Y %I:%M %p", time.localtime())
    return Time

def log(text):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(dir_path, "watchdog.log")
    f = open(log_file,'a')
    f.write(str(date())+': '+str(text)+'\n')
    f.close()

while True:
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    if text in str(output):
        pid = (output.split()[1]).decode("utf-8")
        log("Script is running, PID: " + str(pid))
    else:
        log("Script not running, Restarting Script")
        subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
        #(output2, err2) = p2.communicate()
        #print(output2, err2)
    time.sleep(300)
