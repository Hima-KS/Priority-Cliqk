#!/bin/bash
while true
do
wget "http://download.skype.com/linux/skype-debian_4.3.0.37-1_i386.deb"
echo "skype-debian_4.3.0.37-1_i386"
echo "http://download.skype.com/linux/skype-debian_4.3.0.37-1_i386.deb"
dpkg --add-architecture i386
apt-get update
apt-get -f install
apt-get install gdebi
dpkg -i skype-debian_4.3.0.37-1_i386.deb
gdebi skype-debian_4.3.0.37-1_i386.deb 
apt-get -y install skype
echo " skype has been successfully installed"
done