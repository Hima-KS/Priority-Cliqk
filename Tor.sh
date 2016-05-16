#!/bin/bash
while true
do
wget https://www.torproject.org/dist/torbrowser/5.0.6/tor-browser-linux32-5.0.6_en-US.tar.xz
echo "deb http://deb.torproject.org/torproject.org wheezy main" >> /etc/apt/sources.list
clear scr
echo "[*] Installing the keys...."
gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
echo "Ready!!"
clear scr
echo "[*] Updating Repositories...."
apt-get update
clear scr
echo "[*] Installing TOR"
apt-get install deb.torproject.org-keyring
apt-get install tor
echo "Ready!!"
echo "[*] Installing Vidalia"
apt-get install vidalia
echo "Ready!!"
echo "[*] Installing iceweasel-torbutton"
apt-get install iceweasel-torbutton
echo "Ready!!"
clear scr
echo "[*] Installing Privoxy"
apt-get install privoxy
echo "[*] Configuring privoxy"
echo "forward-socks5 / 127.0.0.1:9050 ." >> /etc/privoxy/config
echo "Ready!!"
service tor restart
service privoxy restart
echo "Tor has been installed successfully." ;;

done