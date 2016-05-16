#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/p/pinta/pinta_1.3-3_all.deb "
dpkg -i pinta_1.3-3_all.deb 
gdebi pinta_1.3-3_all.deb  
apt-get -y install pinta
clear scr
echo "Pinta has been successfully installed"
done