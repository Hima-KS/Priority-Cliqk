#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/g/gui-ufw/gufw_12.10.0-1_all.deb "
dpkg -i gufw_12.10.0-1_all.deb 
gdebi gufw_12.10.0-1_all.deb 
apt-get -y install gufw 
clear scr
echo "Gu-firewall was successfully installed"
done