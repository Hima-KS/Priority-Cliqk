#!/bin/bash
while true
do
apt-get update 
wget "http://download.teamviewer.com/download/teamviewer_i386.deb"
dpkg --add-architecture i386
apt-get install libjpeg62:i386
gdebi teamviewer_i386.deb
clear scr
echo " team viewer has been successfully installed"
done