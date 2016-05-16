#!/bin/bash
while true
do
apt-get update 
wget "http://ftp.us.debian.org/debian/pool/main/j/java-common/default-jdk_1.7-52_amd64.deb"
dpkg -i default-jdk_1.7-52_amd64.deb
gdebi default-jdk_1.7-52_amd64.deb 
apt-get -y install default-jdk 
clear scr
echo " Default-jdk has been successfully installed"
done