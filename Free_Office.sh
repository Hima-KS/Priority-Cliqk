#!/bin/bash
while true
do
wget http://www.softmaker.net/down/softmaker-freeoffice_703-01_i386.deb
gdebi softmaker-freeoffice_703-01_i386.deb
clear scr
echo " FreeOffice is successfuly installed" 
done