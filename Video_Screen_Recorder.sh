#!/bin/bash
while true
do
pt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/g/gtk-recordmydesktop/gtk-recordmydesktop_0.3.8-4.1_all.deb "
dpkg -i gtk-recordmydesktop_0.3.8-4.1_all.deb
gdebi gtk-recordmydesktop_0.3.8-4.1_all.deb 
apt-get -y install recordmydesktop
clear scr
echo "Recordmydesktop was successfully installed"
done