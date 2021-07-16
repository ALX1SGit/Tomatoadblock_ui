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

maxapiquery=45

#Getting Devices Name
def device_list():
    usr= 'root'
    password= 'laylasaurio'
    router = "192.168.1.1"
    queryStr1 = 'http://' + router + '/status-devices.asp'
    r1 = requests.get(queryStr1, auth=(usr, password), verify=False)
    dhcpd_lease=str(r1.text).split("dhcpd_lease = ")[1].split(";")[0].replace("[ [","").replace("]]","").split("],[")
    return dhcpd_lease

def get_location(ip,cache):
    if ("192.168" in ip):
        location="local"
    else:
        try:
            print(ip)
            net=ip.split(".")
            print(net)
            net=net[0]+"."+net[1]+"."+net[2]+"."
            print(net)
            n=len(cache)
            #print(n)
        except:
            location="Entry Error"
        else:
            if (net in str(cache)):
                location=str(cache).split(net)[1].split(":")[1].split("'")[0]
                print("Recovered from the cache")
            else:
                if (n<=maxapiquery):
                    queryStr1 = 'http://ip-api.com/json/' + ip
                    try:
                        r1 = requests.get(queryStr1, verify=False)
                        reply=r1.json()
                        location=reply["countryCode"] + " - " + reply["isp"]
                        cache.append(ip + ":" + location)
                        print(cache)
                    except:
                        location="Unknown"
                else:
                    location="Geo API limit reached"
    #print(location)
    return location, cache
	

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
    logfile='/var/log/messages'
    lines=0
    block=0
    block_local=0
    resolutions=0
    output=list()
    for line in reversed(list(open(logfile,'r'))):
        if ("dnsmasq" in line):
            line=line.rstrip()
            #print(line)
            output.append(line)
            lines+=1
            if ("0.0.0.0" in line):
                block+=1
            if ("is 127.0.0.1" in line):
                block+=1
                block_local+=1
            if (" is " in line):
                resolutions+=1
    #first=str(output[lines-10]).split(" unknown")[0].split("'")[1]
    first=str(list(open(logfile,'r'))[0]).split(" unknown")[0]
    print("first: " + str(first))
    y=datetime.date.today().year
    mon=strptime(first.split(" ")[0],'%b').tm_mon
    try:
        min=first.split(" ")[2].split(":")[1]
        s=first.split(" ")[2].split(":")[2]
    #date in the log has just 1 digit
    except:
        min=first.split(" ")[3].split(":")[1]
        s=first.split(" ")[3].split(":")[2]
        d=first.split(" ")[2]
        h=first.split(" ")[3].split(":")[0]
    else:
        d=first.split(" ")[1]
        h=first.split(" ")[2].split(":")[0]
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
    block_remote=int(block)-int(block_local)
    return render_template("main.html", lines = lines, block = block, block_local=block_local, block_remote=block_remote, delta=delta, online=online, devices=devices, resolutions=resolutions, forward=forward, uptime=uptime)

@app.route('/search/<dev>')
def search(dev):
    dhcpd_lease=device_list()
    print(dhcpd_lease)
    logfile='/var/log/messages'
    lines=0
    block=0
    block_local=0
    resolutions=0
    output=list()
    for line in list(open(logfile,'r')):
        if ("dnsmasq" in line):
            line=line.rstrip()
            #print(line)
            output.append(line)
            lines+=1
            if ("0.0.0.0" in line):
                block+=1
            if ("is 127.0.0.1" in line):
                block+=1
                block_local+=1
            if (" is " in line):
                resolutions+=1
    first=str(output).split(" unknown")[0].split("'")[1]
    #first=str(output).split(" unknown")[0].split("'")[3] #fer testing in windows
    print("first: " + str(first))
    y=datetime.date.today().year
    mon=strptime(first.split(" ")[0],'%b').tm_mon
    try:
        min=first.split(" ")[2].split(":")[1]
        s=first.split(" ")[2].split(":")[2]
    #date in the log has just 1 digit
    except:
        min=first.split(" ")[3].split(":")[1]
        s=first.split(" ")[3].split(":")[2]
        d=first.split(" ")[2]
        h=first.split(" ")[3].split(":")[0]
    else:
        d=first.split(" ")[1]
        h=first.split(" ")[2].split(":")[0]
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
    cache=list()
    for device in dhcpd_lease:
        #print(device)
        ip=str(device).split(",")[1].replace("'","")
        #print(ip)
        match=str(output).count(ip)
        print(match)
        if (match>=1):
            online+=1
            devices.append((str(device).split(",")[0].replace("'","") + "," + ip + "").split(","))
    i=0
    while(i<=int(lines)-1):
        n=output[i].count(str(dev))#Searching for filtered device
        #print(n)
        if (n>=1):
            try:
                s7=output[i+2].count(" from ")
            except:
                toprint=str(output[i] + "\n" + output[i+1])
                i+=1
            else:
                if (s7==1): #Reply just have 1 line and 2 lines before is next querys
                    if ("cached" in output[i+1] and "is" in output[i+1]):
                        location,cache=get_location(output[i+1].split("is")[1].strip(),cache)
                        toprint=str(output[i] + "\n" + output[i+1] + " { " + str(location) + " }")
                    else:
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
                    if ("is" in output[i+1]):
                        location,cache=get_location(output[i+1].split("is")[1].strip(),cache)
                        toprint=toprint + "\n" + output[i+1] + " { " + str(location) + " }"
                    else:
                        toprint=toprint + "\n" + output[i+1]
            toprint=toprint.replace("unknown daemon.info dnsmasq","").replace("\n","\\n").split("\\n")
            flash(toprint)
        else:
            i+=1
    block_remote=int(block)-int(block_local)
    return render_template("search.html", lines = lines, block = block, block_local=block_local, block_remote=block_remote, delta=delta, online=online, devices=devices, resolutions=resolutions, forward=forward, uptime=uptime)


@app.route('/blacklist/<domain>')
def blacklist(domain):
    try:
        domain=domain.split(" ")[5].strip()
    except:
        print("error")
    else:
        print(domain)
        blacklist="/tmp/home/root/publicdns.conf"
        bl=open(blacklist,'a')
        bl.write("address=/" + domain + "/127.0.0.1\n")
        bl.close()
    return redirect(request.referrer)
    

if (__name__ == '__main__'):
    app.run(port=3000, host='0.0.0.0', debug=True)
