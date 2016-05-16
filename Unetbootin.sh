#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.de.debian.org/debian/pool/main/u/unetbootin/unetbootin_471-2_amd64.deb"
dpkg -i unetbootin_471-2_amd64.deb
gdebi unetbootin_471-2_amd64.deb 
apt-get -y install unetbootin
clear scr
echo " unetbootin has been successfully installed" 
done