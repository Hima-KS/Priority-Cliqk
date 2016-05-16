#!/bin/bash
while true
do
apt-get update 
 wget "https://notepad-plus-plus.org/repository/6.x/6.8.8/npp.6.8.8.Installer.exe"
apt-get -y install wine
wine npp.6.8.8.Installer.exe 
clear scr
echo " notepad++ has been successfuly installed"
done
