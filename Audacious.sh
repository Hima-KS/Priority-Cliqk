#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/a/audacious/audacious_3.5-2_amd64.deb "
dpkg -i audacious_3.5-2_amd64.deb 
gdebi audacious_3.5-2_amd64.deb 
apt-get -y install audacious
clear scr
echo "Audacious has been successfully installed"
done