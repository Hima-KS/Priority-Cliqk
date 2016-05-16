#!/bin/bash
while true
do
apt-get update 
wget "https://fpdownload.adobe.com/get/flashplayer/pdc/11.2.202.559/install_flash_player_11_linux.x86_64.tar.gz"
apt-get install flashplugin-nonfree
update -flashplugin-nonfree --install 
clear scr
echo " flash player has been successfully installed" 
done
