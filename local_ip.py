import ipaddress
import random

def get_random_ip_by_mask(ip_str, mask_str):
    try:
        
        interface = ipaddress.IPv4Interface(f"{ip_str}/{mask_str}")
        network = interface.network
        
        
        random_ip_int = random.randint(int(network.network_address) + 1, 
                                       int(network.broadcast_address) - 1)
                                                                                            
        return str(ipaddress.IPv4Address(random_ip_int))
    except ValueError as e:
        return f"Ошибка: {e}"

