#!/bin/bash
while true
do
apt-get update 
wget " http://ftp.us.debian.org/debian/pool/main/k/keepass2/keepass2_2.28+dfsg-1_all.deb"
dpkg -i keepass2_2.28+dfsg-1_all.deb
gdebi keepass2_2.28+dfsg-1_all.deb 
apt-get -y install keepass2 
clear scr
echo "Keepass2 was successfully installed"
done