#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/x/xchat/xchat_2.8.8-7.3_i386.deb"
dpkg -i xchat_2.8.8-7.3_i386.deb
gdebi xchat_2.8.8-7.3_i386.deb
apt-get -y install xchat 
clear scr
echo "xchat has been successfully installed"
done