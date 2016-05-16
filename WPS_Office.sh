#!/bin/bash
while true
do
wget "kdl.cc.ksosoft.com/wps-community/download/a20/wps-office_10.1.0.5503~a20p2_amd64.deb"
gdebi "wps-office_10.1.0.5503~a20p2_amd64.deb"
clear scr
echo " WPS successfully installed"
done