### Linux Network Config 
`/etc/network/interfaces`


    auto eth0
    iface eth0 inet static
      address 192.168.0.3
      netmask 255.255.255.0
      broadcast 192.168.0.255
      network 192.168.0.0
      gateway 192.168.0.1


### Wireless interfaces
* needs the wpasupplicant pkg
`/etc/network/interfaces`


    iface wlan0 inet dhcp
      wpa-ssid MyNetWork
      wpa-psk plainTxtPasswordHere

### Bring network up and down


    ifup <network> 
    ifdown <network>


### systemd networking config (optional)
`/etc/systemd/network/dhcp*.network`


    [Match]
    Name=en*

    [Network]
    DHCP=yes


`/etc/systemd/network/static*.network`


    [Match]
    Name=eth0*

    [Network]
    Address=192.168.0.15/24
    Gateway=192.168.0.1
    DNS=1.1.1.1
    

Systemd-resolved is disabled by default, start it up


    systemctl enable systemd-networkd
    systemctl enable systemd-resolved
    systemctl start systemd-networkd
    systemctl start systemd-resolved
    ln -sf /run/system/resolve/resolv.conf /etc/resolv.conf
    
    
