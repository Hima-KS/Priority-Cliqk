#!/bin/bash
while true
do
apt-get update 
wget " http://ftp.us.debian.org/debian/pool/main/a/amarok/amarok_2.8.0-2.1+b1_amd64.deb"
dpkg -i amarok_2.8.0-2.1+b1_amd64.deb
gdebi amarok_2.8.0-2.1+b1_amd64.deb
apt-get -y install amarok
clear scr
echo "Amarok  has been successfully installed"
done