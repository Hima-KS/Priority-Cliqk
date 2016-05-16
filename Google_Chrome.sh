#!/bin/bash
while true
do
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
gdebi '/root/google-chrome-stable_current_amd64.deb' 
clear scr
echo "Google Chrome is successfully installed" ;;
done