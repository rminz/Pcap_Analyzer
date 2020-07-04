from scapy.all import *
import time
import IPAbuseChecker

def extract_IP(filename):
    start = time.time()
    print("** Extraction started ...")
    
    IP.payload_guess = []
    dst_ips = set(p[IP].dst for p in PcapReader(filename) if IP in p)
    
    end = time.time()
    print( "Extracting IPs Took %g s" % (end - start))
    
    for ip in dst_ips:
        IPAbuseChecker.check_IP(ip)
        