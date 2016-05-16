#!/bin/bash
while true
do
apt-get update 
wget " http://ftp.us.debian.org/debian/pool/main/q/qbittorrent/qbittorrent_3.1.10-1_amd64.deb"
dpkg -i qbittorrent_3.1.10-1_amd64.deb
gdebi qbittorrent_3.1.10-1_amd64.deb
apt-get -y install qbittorrent 
clear scr
echo "Qbittorrent was successfully installed" 
done