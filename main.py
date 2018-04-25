#coding:utf8
#qpy:2
#qpy:console

print "This is console module"
import requests
import androidhelper
import os
class warna:
    W  = '\033[0m'  # white (default)
    R  = '\033[31m' # red
    G  = '\033[1;32m' # green bold
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple
    C  = '\033[36m' # cyan
    GR = '\033[37m' # gray
color = warna()
resp = [200,302]
droid = androidhelper.Android()
def sit():
    droid.vibrate()
    sites = raw_input("TARGET: ")
    if sites == "https://" or "http://":
        return sites.replace("https://","").replace("http://","")
        
def dScan():
    #direktori dir1
    files = "/storage/emulated/0/QZ/dork3.txt"
    dork = open(files).readlines()
    n = 0
    green = 0
    green_list = []
    for i in dork:
        n += 1
        i = i.replace("W","w")        
        try:
            r = requests.get("http://"+site+i)
        except:
            print "Jaringan putus - putus ?"
            print site
        if r.status_code not in resp:
            print color.R+"[+] http://"+site+i+"Status Code: "+str(r.status_code)+color.W
        else:
            green += 1
            green_list.append("http://"+site+i+"Status Code: "+str(r.status_code)+"\n")
            print color.G+"[+] http://"+site+i+"Status Code: "+str(r.status_code)+color.W
    print "[+] Total Scan: ", n
    print "[+] Ijo :", green
    for listsite in green_list:
        print listsite
    droid.vibrate()

def admf():
    #Admf directory
    file = "/storage/emulated/0/QZ/admin.txt"
    buka = open(file).readlines()
    n = 0
    green = 0
    green_list = []
    for i in buka:
        n += 1
        try:        
            r = requests.get("http://"+site+"/"+i)
        except:
            print "Jaringan Putus - putus ?"
            print site
        if r.status_code not in resp:
            print color.R+"[+] http://"+site+"/"+i+"Status Code: "+str(r.status_code)+color.W
        else:
            green += 1
            green_list.append("http://"+site+"/"+i+"Status Code: "+str(r.status_code)+"\n")
            print color.G+"[+] http://"+site+"/"+i+"Status Code: "+str(r.status_code)+color.W        
    print "[+] Total Scan: ", n
    print "[+] Ijo :", green
    for listsite in green_list:
        print listsite
    droid.vibrate()
site = sit()

if __name__ == "__main__":
    print """1. Scan Dir\n2. Admin Finder\r\n"""
    print "Script By "+color.G+"Qiuby Zhukhi\n"+"worldlist by "+color.R+"GOOGLE"+color.W
    print "--== WELCOME TO MOBILE LEGEND ==--"  
    ops = raw_input("Use Ops ==> ")        
    if ops == "1":
        print "Scan Dir"
        dScan()
         
    if ops == "2":
        print "Scan Admin"
        admf()
    else:
        pass