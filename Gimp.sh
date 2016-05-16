#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/g/gimp/gimp_2.8.14-1+b1_amd64.deb "
dpkg -i gimp_2.8.14-1+b1_amd64.deb
gdebi gimp_2.8.14-1+b1_amd64.deb
apt-get -y install gimp 
clear scr
echo "Gimp image editor was successfully installed"
done