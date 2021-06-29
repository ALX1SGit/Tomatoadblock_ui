#/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for, flash
#import system
import subprocess
import shlex
import datetime
from time import strptime
import requests
import urllib3
from flask_googlecharts import GoogleCharts

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Getting Devices Name
def device_list():
    usr= 'root'
    password= 'laylasaurio'
    router = "192.168.1.1"
    queryStr1 = 'http://' + router + '/status-devices.asp'
    r1 = requests.get(queryStr1, auth=(usr, password), verify=False)
    dhcpd_lease=str(r1.text).split("dhcpd_lease = ")[1].split(";")[0].replace("[ [","").replace("]]","").split("],[")
    return dhcpd_lease

start=datetime.datetime.now() - datetime.timedelta(hours=3)

#projectlocation= system.os("pwd")
projectlocation= "//opt//python3"

#Definiciiones de servicios a usar
app = Flask(__name__)
#app = Flask(__name__, static_folder='templates\\static\\', static_url_path='/templates/static/')
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    dhcpd_lease=device_list()
    print(dhcpd_lease)

    cmd = 'more /var/log/messages | grep "dnsmasq"'
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = proc.communicate()

    lines=str(out).count("dnsmasq")
    block=str(out).count("0.0.0.0")
    resolutions=str(out).count(" is ")
    output=str(out).replace('b"','').replace("b'",'').split("\\n")
    #output=str(out).replace('b"','').replace("b'",'').split("\n")#for testing in Windows
    #print(output)
    first=str(output).split(" unknown")[0].split("'")[1]
    #first=str(output).split(" unknown")[0].split("'")[3] #fer testing in windows
    print("first: " + str(first))
    y=datetime.date.today().year
    mon=strptime(first.split(" ")[0],'%b').tm_mon
    d=first.split(" ")[1]
    h=first.split(" ")[2].split(":")[0]
    min=first.split(" ")[2].split(":")[1]
    s=first.split(" ")[2].split(":")[2]
    time0= datetime.datetime(int(y), int(mon), int(d), int(h), int(min), int(s))
    timenow=datetime.datetime.now() - datetime.timedelta(hours=3)
    uptime=str(timenow-start).split(":")[0] + " hs " + str(timenow-time0).split(":")[1] + " min"
    print("now: " + str(timenow))
    delta=str(timenow-time0).split(":")[0] + " hs " + str(timenow-time0).split(":")[1]
    print("Diference is: " + str(delta))
    lines= str(lines)
    delta=str(delta)
    block=str(block)
    devices=list()
    online=int(0)
    forward=int(resolutions)-int(block)
    for device in dhcpd_lease:
        print(device)
        ip=str(device).split(",")[1].replace("'","")
        print(ip)
        match=str(output).count(ip)
        print(match)
        if (match>=1):
            online+=1
            devices.append((str(device).split(",")[0].replace("'","") + "," + ip + "").split(","))
    print(online)
    print(devices)
    #block="Queries filtered in last " + str(delta) + " minutes: " + str(block)
    for line in output:
        string=line.strip().replace("unknown daemon.info dnsmasq","")
        try:
            #string=line.split("unknown")[0] + ":" + line
            toprint=string.split(":")
        except:
            flash(string)
        else:
            flash(toprint)
    return render_template("main.html", lines = lines, block = block, delta=delta, online=online, devices=devices, resolutions=resolutions, forward=forward, uptime=uptime)

@app.route('/search/<dev>')
def search(dev):
    dhcpd_lease=device_list()
    print(dhcpd_lease)

    cmd = 'more /var/log/messages | grep "dnsmasq"'
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = proc.communicate()

    lines=str(out).count("dnsmasq")
    block=str(out).count("0.0.0.0")
    resolutions=str(out).count(" is ")
    output=str(out).replace('b"','').replace("b'",'').split("\\n")
    #output=str(out).replace('b"','').replace("b'",'').split("\n")#for testing in Windows
    #print(output)
    first=str(output).split(" unknown")[0].split("'")[1]
    #first=str(output).split(" unknown")[0].split("'")[3] #fer testing in windows
    print("first: " + str(first))
    y=datetime.date.today().year
    mon=strptime(first.split(" ")[0],'%b').tm_mon
    d=first.split(" ")[1]
    h=first.split(" ")[2].split(":")[0]
    min=first.split(" ")[2].split(":")[1]
    s=first.split(" ")[2].split(":")[2]
    time0= datetime.datetime(int(y), int(mon), int(d), int(h), int(min), int(s))
    timenow=datetime.datetime.now() - datetime.timedelta(hours=3)
    uptime=str(timenow-start).split(":")[0] + " hs " + str(timenow-time0).split(":")[1] + " min"
    print("now: " + str(timenow))
    delta=str(timenow-time0).split(":")[0] + " hs " + str(timenow-time0).split(":")[1]
    print("Diference is: " + str(delta))
    lines= str(lines)
    delta=str(delta)
    block=str(block)
    devices=list()
    online=int(0)
    forward=int(resolutions)-int(block)
    for device in dhcpd_lease:
        #print(device)
        ip=str(device).split(",")[1].replace("'","")
        #print(ip)
        match=str(output).count(ip)
        print(match)
        if (match>=1):
            online+=1
            devices.append((str(device).split(",")[0].replace("'","") + "," + ip + "").split(","))
    #print(online)
    #print(devices)
    #block="Queries filtered in last " + str(delta) + " minutes: " + str(block)
    #print(dev)
    #print(output[10])
    i=0
    while(i<=int(lines)):
        n=output[i].count(str(dev))#Searching for filtered device
        #print(n)
        if (n>=1):
            #print(i)
            #s1=output[i+1].count(" cached ")
            #s2=output[i+1].count("config")
            #s3=output[i+1].count(" forwarded ")
            #s4=output[i+1].count(" <CNAME>")
            #s5=output[i+1].count(" reply ")
            #s6=output[i+1].count(" is ")
            try:
                s7=output[i+2].count(" from ")
            except:
                toprint=str(output[i] + "\n" + output[i+1])
                i+=1
            else:
                if (s7==1): #Reply just have 1 line and 2 lines before is next querys
                    toprint=str(output[i] + "\n" + output[i+1])
                    i+=1
                else: #Reply has multiple lines
                    toprint=str(output[i] + "\n")
                    while(s7==0):
                        i+=1
                        try:
                            s7=str(output[i+2]).count(" from ")
                        except:
                            break
                        else:
                            toprint=(toprint + str(output[i] + "\n"))
                    toprint=toprint + "\n" + output[i+1]
            toprint=toprint.replace("unknown daemon.info dnsmasq","").replace("\n","\\n").split("\\n")
            flash(toprint)
        else:
            i+=1
    return render_template("search.html", lines = lines, block = block, delta=delta, online=online, devices=devices, resolutions=resolutions, forward=forward, uptime=uptime)



if (__name__ == '__main__'):
    app.run(port=3000, host='0.0.0.0', debug=True)
