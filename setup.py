import os
banner = '''


#  ███████╗  █████╗  ██╗  ██╗ ██╗ ██╗     
#  ██╔════╝ ██╔══██╗ ██║  ██║ ██║ ██║       
#  ███████╗ ███████║ ███████║ ██║ ██║       
#  ╚════██║ ██╔══██║ ██╔══██║ ██║ ██║       Created by Venom (24-11-2020)
#  ███████║ ██║  ██║ ██║  ██║ ██║ ███████╗  Instagram - i.m.gauravchaudhary
#  ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚══════╝  Contact - +91 9910332273
#                                     
                                

'''
print(banner)
os.system('pip3 install requests')
os.system('pip3 install urllib3')
os.system('pip3 install bs4')
os.system('pip3 install colorama')
os.system('pip3 install builtwith')
os.system('pip3 install sslscan')
os.system('pip3 install parsel')
os.system('pip3 install httplib2')
os.system('curl https://xael.org/pages/python-nmap-0.6.1.tar.gz --output python-nmap-0.6.1.tar.gz')
os.system('tar xvzf python-nmap-0.6.1.tar.gz')
os.system('cd python-nmap-0.6.1 && python3 setup.py install')
os.system('clear')
from colorama import Fore
y = Fore.YELLOW
w = Fore.WHITE
print(y + banner + y)
print(w + '     [+] ' + w + y + 'Now run venom.py!!!' + y)




