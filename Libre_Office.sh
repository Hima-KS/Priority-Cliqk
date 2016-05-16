#!/bin/bash
while true
do
apt-get update 
 wget "security.debian.org/debian-security/pool/updates/main/libr/libreoffice/libreoffice_4.3.3-2+deb8u2_i386.deb"
dpkg -i libreoffice_4.3.3-2+deb8u2_i386.deb
gdebi libreoffice_4.3.3-2+deb8u2_i386.deb 
apt-get -y install libreoffice 
clear scr
echo "Libreoffice has been successfully installed"
done