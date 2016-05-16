#!/bin/bash
while true
do
apt-get update 
 wget "http://ftp.us.debian.org/debian/pool/main/c/claws-mail/claws-mail_3.11.1-3_amd64.deb"
dpkg -i claws-mail_3.11.1-3_amd64.deb
gdebi claws-mail_3.11.1-3_amd64.deb 
apt-get -y install claws-mail
clear scr
echo " Claws-mail has been successfully installed"
done