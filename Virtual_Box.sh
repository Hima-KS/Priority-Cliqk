#!/bin/bash
while true
do
apt-get update 
wget "http://download.virtualbox.org/virtualbox/5.0.12/virtualbox-5.0_5.0.12-104815~Debian~wheezy_i386.deb"
dpkg -i virtualbox-5.0_5.0.12-104815~Debian~wheezy_i386.deb
gdebi virtualbox-5.0_5.0.12-104815~Debian~wheezy_i386.deb 
apt-get -y install virtualbox
clear scr
echo " virtualbox  has been successfully installed"
done
