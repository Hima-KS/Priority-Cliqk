#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/a/audacity/audacity_2.0.6-2_i386.deb"
dpkg -i audacity_2.0.6-2_i386.deb
gdebi audacity_2.0.6-2_i386.deb 
apt-get -y install audacity
clear scr
echo "Audacity has been successfully installed "
done