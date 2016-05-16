#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/u/uget/uget_1.10.4-1_amd64.deb"
dpkg -i uget_1.10.4-1_amd64.deb
gdebi uget_1.10.4-1_amd64.deb 
apt-get -y install uget
clear scr
echo "Uget downloader was successfully installed"
done