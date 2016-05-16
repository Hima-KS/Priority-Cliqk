#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/c/ctorrent/ctorrent_1.3.4.dnh3.3.2-4_amd64.deb "
dpkg -i ctorrent_1.3.4.dnh3.3.2-4_amd64.deb 
gdebi ctorrent_1.3.4.dnh3.3.2-4_amd64.deb 
apt-get -y install ctorrent  
clear scr
echo " Ctorrent has been successfully installed"
done