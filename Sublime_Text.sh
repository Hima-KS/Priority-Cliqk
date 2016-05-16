#!/bin/bash
while true
do
apt-get update 
 wget "c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_amd64.deb"
dpkg -i sublime-text_build-3083_amd64.deb
gdebi sublime-text_build-3083_amd64.deb
apt-get -y install sublime-text 
clear scr
echo " sublime-text  has been successfully installed"
done