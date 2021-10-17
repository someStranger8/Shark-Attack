
import os
clear = lambda: os.system("clear")
def hackwin():
    os.system("cat \Windows\System32\config")
def hackmac():
    os.system("cat /var/db/dslocal/nodes/Default/users")
def hacklin():
    os.system("cat /etc/passwd")
    os.system("cat /etc/shadow")
def ddos(attack):
    os.system("ping "+ attack+"")
def sqlinject():
    os.system("pip3 install sqlmap")
    clear()
    os.system("sqlmap --sqlmap-shell")
def exploit():
    clear()
    os.system("msfconsole")
def hackwifi():
    os.system("sudo apt install fern-wifi-cracker -y")
    clear()
    os.system("fern-wifi-cracker")
def hackpasswd(username, wordlist, ip):
    os.system("sudo apt install hydra -y")
    clear()
    os.system("hydra -l "+ username+" -P "+ wordlist+" ssh://"+ ip+"")
def mitm():
    os.system("sudo apt instal wireshark -y")
    clear()
    os.system("sudo wireshark")
def scan(nmap):
    os.system("sudo apt install nmap -y")
    clear()
    os.system("nmap "+ nmap+"")
def git(link):
    os.system("git clone "+ link)
def hackweb():
    os.system("pip3 install websploit")
    clear()
    os.system("websploit")
def hackphone():
    os.system("sudo apt install scrcpy -y")
    clear()
    os.system("scrcpy")
def hackdrone():
    os.system("pip3 install dronesploit")
    clear()
    os.system("dronesploit")
def install(package):
    os.system("sudo apt install "+ package+" -y")
    clear()
def run(command):
    os.system(command)
def payload(name):
    os.system("nano "+ name+"")
print("its time to hack the world")
