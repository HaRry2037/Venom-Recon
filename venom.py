try:
    import requests
    from colorama import Fore
    import random
    import os
    import builtwith
    import httplib2
    import nmap
    from bs4 import BeautifulSoup
    import requests.exceptions
    from parsel import Selector
    import re
    import socket
except ModuleNotFoundError as e:
    print('Run setup.py and restart again!!!')
nm = nmap.PortScanner()
g = Fore.GREEN
r = Fore.RED
c = Fore.CYAN
w = Fore.WHITE
y = Fore.YELLOW
b = Fore.BLUE
os.system('clear')
colors = (g, c, w, y, b)
color = random.choice(colors)

banner = '''
    
#  ███████╗  █████╗  ██╗  ██╗ ██╗ ██╗     
#  ██╔════╝ ██╔══██╗ ██║  ██║ ██║ ██║       
#  ███████╗ ███████║ ███████║ ██║ ██║       
#  ╚════██║ ██╔══██║ ██╔══██║ ██║ ██║       Created by Venom (24-11-2020)
#  ███████║ ██║  ██║ ██║  ██║ ██║ ███████╗  Instagram - i.m.gauravchaudhary
#  ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚══════╝  Contact - +91 9910332273
#                                     
                                   
                                                                                                                   
'''
ip = requests.get('https://api.ipify.org/')
ip_add = ip.text
print(color + banner + color)
print(w + "     [+] " + w + color + "Your ip: " + color + g + str(ip_add) + g)
print(" ")
target = input(w + '     [+] ' + w + 'Enter the target domain: ')
target_url = []
if target.startswith('https://') or target.startswith('http://') is False:
    ssl = input(w + '     [+] ' + w + color + 'Target runs on http or https? [For Http select 1 and For Https select 2] ' + color)
    if ssl == '1':
        url = 'http://'+target
        target_url.append(url)
    elif ssl == '2':
        url = 'https://'+target
        target_url.append(url)
link = target_url[0]


#headers

print(' ')
print(w + '     [+] Target: ' + w + color + link + color)
print(w + '     [+] Target IP: ' + w + color + socket.gethostbyname(target) + color)
try:
    print(w + '     [+] Target Host: ' + w + color + socket.gethostbyaddr(target)[0] + color)
except socket.herror as e:
    pass
print(' ')
print(w + '     [-] ' + w + color + '----------------- Header Report ------------------' + color + w + ' [-]' + w)
print(' ')
h = httplib2.Http(".cache")
response = h.request(link, "GET")
results = response[0]
headers = []
for i in results:
    key = str(i)
    headers.append(key)
for ok in headers:
    new = dict(filter(lambda item: ok in item[0], results.items()))
    print(w + '     [+] ' + color + ok + color + w + ' : ' + w + g + new[ok] + g)


#target technology
print(' ')
print(w + '     [-] ' + w + color + '------------------ Target Technology -----------------' + color + w + ' [-]' + w)
print(' ')
try:
    output = builtwith.builtwith(link)
    built = []
    for i in output:
        key = str(i)
        built.append(key)
    for new in built:
        ok = dict(filter(lambda item: new in item[0], output.items()))
        count = len(ok[new])
        new = str(new)
        x = 0
        if count == 1:
            print(w + '     [+] ' + w + color + new.capitalize() + color + w + ': ' + w + g + str(ok[new][0]) + g)
        elif count == 2:
            print(w + '     [+] ' + w + color + new.capitalize() + color + w + ': ' + w + g + str(ok[new][0]) + ', ' + str(ok[new][1]) + g)
        elif count == 3:
            print(w + '     [+] ' + w + color + new.capitalize() + color + w + ': ' + w + g + str(ok[new][0]) + ', ' + str(ok[new][1]) + ',' + str(ok[new][2]) + g)
        elif count == 4:
            print(w + '     [+] ' + w + color + new.capitalize() + color + w + ': ' + w + g + str(ok[new][0]) + ', ' + str(ok[new][1]) + ',' + str(ok[new][2]) + ',' + str(ok[new][3]) + g)
        elif count == 5:
            print(w + '     [+] ' + w + color + new.capitalize() + color + w + ': ' + w + g + str(ok[new][0]) + ',' + str(ok[new][1]) + ',' + str(ok[new][2]) + ',' + str(ok[new][3]) + ',' + str(ok[new][4]) + g)
        else:
            pass
except UnicodeError as e:
    print(w + '     [+] ' + w + r + 'No technology found' + r)

# Port Scanning

print(' ')
print(w + '     [-] ' + w + color + '------------------ Port Scanning Results ------------------' + color + ' [-]' + w)
domain = []
if link.startswith('https://') is True:
    new_domain = target.replace('https://', '')
    domain.append(new_domain)
elif link.startswith('http://') is True:
    new_domain = target.replace('http://', '')
    domain.append(new_domain)
target_domain = domain[0]
results = nm.scan(target_domain, '0-1000')
scaninfo = results['nmap']['scaninfo']
scanstats = results['nmap']['scanstats']
scanresult = results['scan']
ip = []
for i in scanresult:
    ip.append(i)
ipadd = ip[0]
scanstatus = results['scan'][ipadd]['tcp']
scanstatus_new = []
for i in scanstatus:
    scanstatus_new.append(i)
port = []
for i in scanstatus_new:
    port.append(i)
for x in port:
    print(w + '     [+] ' + w + color + 'Port Number: ' + color + g + str(x) + g)
    print(' ')
    print(w + '     [+] ' + w + color + 'State: ' + color + g + scanstatus[x]['state'] + g)
    print(w + '     [+] ' + w + color + 'Reason: ' + color + g + scanstatus[x]['reason'] + g)
    print(w + '     [+] ' + w + color + 'Name: ' + color + g + scanstatus[x]['name'] + g)
    print(w + '     [+] ' + w + color + 'Product: ' + color + g + scanstatus[x]['product'] + g)
    print(w + '     [+] ' + w + color + 'Version: ' + color + g + scanstatus[x]['version'] + g)
    print(w + '     [+] ' + w + color + 'Version Extra Info: ' + color + g + scanstatus[x]['extrainfo'] + g)
    print(w + '     [+] ' + w + color + 'Conf: ' + color + g + scanstatus[x]['conf'] + g)
    print(w + '     [+] ' + w + color + 'Cpe: ' + color + g + scanstatus[x]['cpe'] + g)
    print(' ')

# reverse ip
print(' ')
print(w + '     [-] ' +   w + color + '------------------ Reverse IP Lookup ------------------' + color + ' [-]' + w)
print(' ')
rev = 'http://api.hackertarget.com/reverseiplookup/?q=' + target
res = requests.get(rev)
tar = res.text
if len(tar) != 5:
    lis = tar.strip("").split("\n")
    for lin in lis:
        if len(lin) != 0:
            print(w + '     [+] ' + w + color + lin + color)
else:
    print(w + '     [+] ' + w + r + 'No records found' + r)

#Shared Dns Record
print(' ')
print(w + '     [-] ' + w + color + '------------------- Searching in Shared DNS Records  ------------------' + w)
print(' ')
dns_url = 'https://hackertarget.com/find-shared-dns-servers/'
headers = {'Host': 'hackertarget.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
           'Accept': 'text/html, */*; q=0.01',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'https://hackertarget.com/find-shared-dns-servers/',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'close'}
data = 'theinput=' + target + '&thetest=findshareddns&name_of_nonce_field=765385249e&_wp_http_referer=%2Ffind-shared-dns-servers%2F'
respo = requests.post(url=dns_url, headers=headers, data=data)
soup = BeautifulSoup(respo.content, 'html.parser')
resu = soup.findAll('pre', id='formResponse')
out = resu[0]
_out = str(out)
new_out = _out[23:-6]
if len(new_out) != 5:
    _list = new_out.strip('').split('\n')
    for _links in _list:
        if len(_links) != 0:
            print(w + '     [+] ' + w + color + _links + color)
else:
    print(w + '     [+] ' + w + r + 'error' + r)

# subnet calcuator
tar_ip = socket.gethostbyname(target)
print(' ')
print(w + '     [-] ' + w + color + '------------------- Subnet Calculator  ------------------' + w)
print(' ')
sub_url = 'https://hackertarget.com/subnet-lookup-online'
headers1 = {'Host': 'hackertarget.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
           'Accept': 'text/html, */*; q=0.01',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'https://hackertarget.com/subnet-lookup-online',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'close'}
data1 = 'theinput=' + target + '&thetest=subnetcalc&name_of_nonce_field=765385249e&_wp_http_referer=%2Ffind-shared-dns-servers%2F'
respo1 = requests.post(url=sub_url, headers=headers1, data=data1)
soup1 = BeautifulSoup(respo1.content, 'html.parser')
resu1 = soup1.findAll('pre', id='formResponse')
out1 = resu1[0]
_out1 = str(out1)
new_out1 = _out1[23:-6]
if len(new_out1) != 5:
    _list1 = new_out1.strip('').split('\n')
    for _links1 in _list1:
        if len(_links1) != 0:
            print(w + '     [+] ' + w + color + _links1 + color)
else:
    print(w + '     [+] ' + w + r + 'error' + r)
print(' ')

#finding dns records
print(' ')
print(w + '     [-] ' + w + color + '------------------- Searching Sub Domains  ------------------' + w)
print(' ')
dns_host_rec = 'https://hackertarget.com/find-dns-host-records'
headers2 = {'Host': 'hackertarget.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
           'Accept': 'text/html, */*; q=0.01',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'https://hackertarget.com/find-dns-host-records',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'close'}
data2 = 'theinput=' + target + '&thetest=hostsearch&name_of_nonce_field=765385249e&_wp_http_referer=%2Ffind-shared-dns-servers%2F'
respo2 = requests.post(url=dns_host_rec, headers=headers2, data=data2)
soup2 = BeautifulSoup(respo2.content, 'html.parser')
resu2 = soup2.findAll('pre', id='formResponse')
out2 = resu2[0]
_out2 = str(out2)
new_out2 = _out2[23:-6]
if len(new_out2) != 5:
    _list2 = new_out2.strip('').split('\n')
    for _links2 in _list2:
        if len(_links2) != 0:
            print(w + '     [+] ' + w + color + _links2 + color)
else:
    print(w + '     [+] ' + w + r + 'error' + r)

# asn lookup

print(' ')
print(w + '     [-] ' + w + color + '------------------- ASN Lookup ------------------' + w)
print(' ')
asn_rec = 'https://hackertarget.com/as-ip-lookup/'
headers4 = {'Host': 'hackertarget.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
           'Accept': 'text/html, */*; q=0.01',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'https://hackertarget.com/find-dns-host-records',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'close'}
data4 = 'theinput=' + target + '&thetest=asnlookup&name_of_nonce_field=765385249e&_wp_http_referer=%2Ffind-shared-dns-servers%2F'
respo4 = requests.post(url=asn_rec, headers=headers4, data=data4)
soup4 = BeautifulSoup(respo4.content, 'html.parser')
resu5 = soup4.find('table', id='myTable')
try:
    resu4 = str(resu5.text)
    resu6 = resu4[30:]
    if len(resu6) != 5:
        _list4 = resu6.strip('').split('\n')
        for _links4 in _list4:
            if len(_links4) != 0:
                print(w + '     [+] ' + w + color + _links4 + color)
    else:
        print(w + '     [+] ' + w + r + 'error' + r)
except AttributeError as e:
    print(w + '     [+] ' + w + r + 'No Asn record found    ' + r)
# Ssl verify

print(' ')
print(w + '     [-] ' + w + color + '------------------- Verifying SSL  ------------------' + w)
print(' ')
ssl_scan = os.system('pysslscan scan --scan=protocol.http --scan=vuln.heartbleed --scan=server.renegotiation --scan=server.preferred_ciphers --scan=server.ciphers --report=term:rating=ssllabs.2009e --ssl2 --ssl3 --tls10 --tls11 --tls12 http://' + target)
ssl_scan = str(ssl_scan)
if len(ssl_scan) != 5:
    _list5 = ssl_scan.strip('').split('\n')
    for _links5 in _list5:
        if len(_links5) != 0:
            print(w + '     ' + w + color + _links5 + color)
else:
    print(w + '     [+] ' + w + r + 'error' + r)

# spf record checker
print(' ')
print(w + '     [-] ' + w + color + '------------------- Searching For SPF records  ------------------' + w)
print(' ')
url5 = 'https://api-181.fraudmarc.com/web-20209/check/' + target + '/spf'
headers5 = {'Referer': 'https://secure.fraudmarc.com/tool/spf/simple.com',
            'Origin': 'https://secure.fraudmarc.com'}
response5 = requests.get(url=url5, headers=headers5)
soup5 = BeautifulSoup(response5.content, 'html.parser')
print(soup5)
#web crawler

print(' ')
print(w + '     [-] ' + w + color + '------------------- Website Crawling  ------------------' + w)
print(' ')

response = requests.get(link)
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
for i in href_links:
    _string = str(i)
    if _string == '#':
        pass
    elif _string.startswith(link) is False:
        if (_string.startswith('http://') or _string.startswith('https://')) is True:
            print(w + '     [+]' + w + color + 'Link Found: ' + color + g + _string + g)
        else:
            print(w + '     [+] ' + w + color + 'Link Found: ' + color + g + target + '/' + _string + g)
    else:
        pass

# way back machine

print(' ')
print(w + '     [-] ' + w + color + '------------------- Searching in WayBack Machine  ------------------' + w)
print(' ')
try:
    print(' ')
    url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'
    response = requests.get(url)
    response = response.text
    length = len(response)
    if length > 1:
        response = response.splitlines()
        for i in response:
            print(w + '     [+]Link Found: ' + w + g + i + g)
    else:
        print(w + '        [-]' + w + r + ' No Link Found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '         [+] ' + w + r + 'Connection Error' + r)
print(' ')

#.swf google

print(w + '     [-] ' + w + color + '------------------- Looking for .SWF file (Google) ------------------' + color + w + '[-]' + w)
print(' ')
try:
    url = 'https://www.google.com/search?q=+inurl:' + target + '+ext:swf'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

#subdomains

print(" ")
print(w + '     [-] ' + w + color + '------------------- Looking for Subdomains ------------------' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:*.' + target
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

# sensitive files

print(" ")
print(w + '     [-] ' + w + color + '------------------- Sensitive Files ------------------' + color + w + '[-]' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:' + target + '+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+simple.com%20-github'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

#Looking for employees on linkedin

print(" ")
print(w + '     [-] ' + w + color + '------------------- Looking For employees on linked ------------------' + color + w + '[-]' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:linkedin.com+employees+' + target
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

# Pastebin enteries
print(" ")
print(w + '     [-] ' + w + color + '------------------- Looking for Pastebin entries ------------------' + color + '[-]' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:pastebin.com+' + target
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

# php info

print(" ")
print(w + '     [-] ' + w + color + '------------------- Looking For phpinfoPhp() ------------------' + color + '[-]' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:' + target + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)

# sql errors

print(" ")
print(w + '     [-] ' + w + color + '------------------- Looking for SQL errors ------------------' + color + '[-]' + w)
print(" ")
try:
    url = 'https://www.google.com/search?q=site:' + target + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                print(w + '     [+] Link Found: ' + w + g + i + g)
    else:
        print(w + '     [+] ' + w + r + 'No Link found' + r)
except requests.exceptions.ConnectionError as e:
    print(w + '      [+] ' + w + r + 'Connection Error' + r)


