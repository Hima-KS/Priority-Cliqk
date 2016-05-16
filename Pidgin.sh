#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/p/pidgin/pidgin_2.10.11-1_amd64.deb "
dpkg -i pidgin_2.10.11-1_amd64.deb
gdebi pidgin_2.10.11-1_amd64.deb 
apt-get -y install pidgin 
clear scr
echo "Pidgin was successfully installed"
done