#!/bin/bash
while true
do
apt-get update 
wget " http://ftp.us.debian.org/debian/pool/main/l/lekhonee-gnome/lekhonee-gnome_0.11-3_amd64.deb"
dpkg -i lekhonee-gnome_0.11-3_amd64.deb
gdebi lekhonee-gnome_0.11-3_amd64.deb 
apt-get -y install lekhonee-gnome
clear scr
echo "Lekhonee-gnome was successfully installed"
done