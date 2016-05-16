#!/bin/bash
while true
do
apt-get update  
wget " http://ftp.us.debian.org/debian/pool/main/e/eclipse/eclipse_3.8.1-7_all.deb"
dpkg -i eclipse_3.8.1-7_all.deb
gdebi eclipse_3.8.1-7_all.deb 
apt-get -y install eclipse 
clear scr
echo "Eclipse was successfully installed"
done