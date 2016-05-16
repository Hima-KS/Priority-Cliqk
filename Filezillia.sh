#!/bin/bash
while true
do
apt-get update 
 wget " http://ftp.us.debian.org/debian/pool/main/f/filezilla/filezilla_3.9.0.5-1_amd64.deb"
dpkg -i filezilla_3.9.0.5-1_amd64.deb
gdebi filezilla_3.9.0.5-1_amd64.deb
apt-get -y install filezilla 
clear scr
echo " Filezilla  has been successfully installed"
done
