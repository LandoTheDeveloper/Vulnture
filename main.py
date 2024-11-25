import nmap

DEBUG = True

def scan_grab_banners(target):
    
    nm = nmap.PortScanner() # Init our scanner
    res = nm.scan(target, str(50-55))    # Scan our target and IP's
    print(res)
    status = res['scan'][target]['status']['state']
    print(f'Port 53 is {status}')
    
    
if __name__ == "__main__":
    if not DEBUG:
        target_id = input("What IP do you want to scan? ")
    else:
        target_id = '127.0.0.1'
    scan_grab_banners(target_id)