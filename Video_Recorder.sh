#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/v/vdr/vdr_2.0.3-3_amd64.deb "
dpkg -i vdr_2.0.3-3_amd64.deb
gdebi vdr_2.0.3-3_amd64.deb
apt-get -y install vdr 
clear scr
echo "Vdr has been successfully installed"
done