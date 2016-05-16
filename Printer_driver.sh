#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/p/printing-metas/printer-driver-all_0.20140714_all.deb "
dpkg -i printer-driver-all_0.20140714_all.deb
gdebi printer-driver-all_0.20140714_all.deb 
apt-get -y install printer-driver-all 
clear scr
echo "Printer-driver has been successfully installed"
done