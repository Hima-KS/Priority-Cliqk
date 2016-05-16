#!/usr/bin/python
# -*- coding: utf-8 -*-




"""
Author        : Hima KS 
Name          : Priority Cliqk
Description   : Automatically downloads , installs and updates applications in one click. Tested on all Debian distribtions.
Last edited   : May16 2016
"""





import os
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowIcon(QtGui.QIcon('pr.jpeg'))
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Chromium", self)
        btn1.resize(200, 30)
        btn1.move(50, 30)
       

        btn2 = QtGui.QPushButton("Tor", self)
        btn2.resize(200, 30)
        btn2.move(280, 30)

        btn3 = QtGui.QPushButton("Skype", self)
        btn3.resize(200, 30)
        btn3.move(510, 30)

        btn4 = QtGui.QPushButton("Team Viewer", self)
        btn4.resize(200, 30)
        btn4.move(740, 30)

        btn5 = QtGui.QPushButton("Adobe Flash Player", self)
        btn5.resize(200, 30)
        btn5.move(970, 30)

        btn6 = QtGui.QPushButton("Notepad++", self)
        btn6.resize(200, 30)
        btn6.move(50, 100)

        btn7 = QtGui.QPushButton("Sublime Text", self)
        btn7.resize(200, 30)
        btn7.move(280, 100)

        btn8 = QtGui.QPushButton("Virtual Box", self)
        btn8.resize(200, 30)
        btn8.move(510, 100)

        btn9 = QtGui.QPushButton("Unetbootin", self)
        btn9.resize(200, 30)
        btn9.move(740, 100)

        btn10 = QtGui.QPushButton("Claws Mail Client", self)
        btn10.resize(200, 30)
        btn10.move(970, 100)

        btn11 = QtGui.QPushButton("xChat-IRC", self)
        btn11.resize(200, 30)
        btn11.move(50, 170)

        btn12 = QtGui.QPushButton("Libre Office", self)
        btn12.resize(200, 30)
        btn12.move(280, 170)

        btn13 = QtGui.QPushButton("Audiocity", self)
        btn13.resize(200, 30)
        btn13.move(510, 170)

        btn14 = QtGui.QPushButton("Pinta", self)
        btn14.resize(200, 30)
        btn14.move(740, 170)

        btn15 = QtGui.QPushButton("Audacious", self)
        btn15.resize(200, 30)
        btn15.move(970, 170)

        btn16 = QtGui.QPushButton("Amarok Player", self)
        btn16.resize(200, 30)
        btn16.move(50, 240)

        btn17 = QtGui.QPushButton("VLC Video Player", self)
        btn17.resize(200, 30)
        btn17.move(280, 240)

        btn18 = QtGui.QPushButton("Java JDK", self)
        btn18.resize(200, 30)
        btn18.move(510, 240)

        btn19 = QtGui.QPushButton("Inkscape", self)
        btn19.resize(200, 30)
        btn19.move(740, 240)

        btn20 = QtGui.QPushButton("Printer driver", self)
        btn20.resize(200, 30)
        btn20.move(970, 240)

        btn21 = QtGui.QPushButton("Filezillia-ftp", self)
        btn21.resize(200, 30)
        btn21.move(50, 310)

        btn22 = QtGui.QPushButton("Video Recorder", self)
        btn22.resize(200, 30)
        btn22.move(280, 310)

        btn23 = QtGui.QPushButton("c Torrent", self)
        btn23.resize(200, 30)
        btn23.move(510, 310)

        btn24 = QtGui.QPushButton(" Screen Recorder", self)
        btn24.resize(200, 30)
        btn24.move(740, 310)

        btn25 = QtGui.QPushButton("WordPress", self)
        btn25.resize(200, 30)
        btn25.move(970, 310)

        btn26 = QtGui.QPushButton("Eclipse", self)
        btn26.resize(200, 30)
        btn26.move(50, 380)

        btn27 = QtGui.QPushButton("Pidgin-IM", self)
        btn27.resize(200, 30)
        btn27.move(280, 380)

        btn28 = QtGui.QPushButton("qBittorrent", self)
        btn28.resize(200, 30)
        btn28.move(510, 380)

        btn29 = QtGui.QPushButton("uget Downloader", self)
        btn29.resize(200, 30)
        btn29.move(740, 380)

        btn30 = QtGui.QPushButton("Password Manager", self)
        btn30.resize(200, 30)
        btn30.move(970, 380)

        btn31 = QtGui.QPushButton("gufw Firewall", self)
        btn31.resize(200, 30)
        btn31.move(50, 440)

        btn32 = QtGui.QPushButton("Gimp", self)
        btn32.resize(200, 30)
        btn32.move(280, 440)

        btn33 = QtGui.QPushButton("Backuppc", self)
        btn33.resize(200, 30)
        btn33.move(510, 440)

        btn34 = QtGui.QPushButton("Kate", self)
        btn34.resize(200, 30)
        btn34.move(740, 440)

        btn35 = QtGui.QPushButton("Deluge", self)
        btn35.resize(200, 30)
        btn35.move(970, 440)

        btn36 = QtGui.QPushButton("Google Chrome", self)
        btn36.resize(200, 30)
        btn36.move(50, 510)

        btn37 = QtGui.QPushButton("Rhythmbox", self)
        btn37.resize(200, 30)
        btn37.move(280, 510)

        btn38 = QtGui.QPushButton("Dosbox", self)
        btn38.resize(200, 30)
        btn38.move(510, 510)

        btn39 = QtGui.QPushButton("WPS Office", self)
        btn39.resize(200, 30)
        btn39.move(740, 510)

        btn40 = QtGui.QPushButton("Callingra Office", self)
        btn40.resize(200, 30)
        btn40.move(970, 510)

        btn41 = QtGui.QPushButton("Free Office", self)
        btn41.resize(200, 30)
        btn41.move(50, 580)

        btn42 = QtGui.QPushButton("Synaptic", self)
        btn42.resize(200, 30)
        btn42.move(280, 580)

        btn43 = QtGui.QPushButton("Kmail", self)
        btn43.resize(200, 30)
        btn43.move(510, 580)

        btn44 = QtGui.QPushButton("Kopete", self)
        btn44.resize(200, 30)
        btn44.move(740, 580)

        btn45 = QtGui.QPushButton("Emacs", self)
        btn45.resize(200, 30)
        btn45.move(970, 580)

        btn46 = QtGui.QPushButton("Internet Explorer", self)
        btn46.resize(200, 30)
        btn46.move(50, 650)

        btn47 = QtGui.QPushButton("Tuxpaint", self)
        btn47.resize(200, 30)
        btn47.move(280, 650)

        btn48 = QtGui.QPushButton("kftpgrabber", self)
        btn48.resize(200, 30)
        btn48.move(510, 650)

        btn49 = QtGui.QPushButton("Sonata", self)
        btn49.resize(200, 30)
        btn49.move(740, 650)

        btn50 = QtGui.QPushButton("Joe", self)
        btn50.resize(200, 30)
        btn50.move(970, 650)




        
        btn1.clicked.connect(self.Chromium)            
        btn2.clicked.connect(self.Tor)
        btn3.clicked.connect(self.Skype)
        btn4.clicked.connect(self.Team_Viewer)
        btn5.clicked.connect(self.Adobe_Flash_Player)
        btn6.clicked.connect(self.Notepad)
        btn7.clicked.connect(self.Sublime_Text)
        btn8.clicked.connect(self.Virtual_Box)
        btn9.clicked.connect(self.Unetbootin)
        btn10.clicked.connect(self.Claws)
        btn11.clicked.connect(self.xChat)
        btn12.clicked.connect(self.Libre_Office)
        btn13.clicked.connect(self.Audiocity)
        btn14.clicked.connect(self.Pinta)
        btn15.clicked.connect(self.Audacious)
        btn16.clicked.connect(self.Amarok)
        btn17.clicked.connect(self.VLC)
        btn18.clicked.connect(self.Java)
        btn19.clicked.connect(self.Inkscape)
        btn20.clicked.connect(self.Printer_driver)
        btn21.clicked.connect(self.Filezillia)
        btn22.clicked.connect(self.Video_Recorder)
        btn23.clicked.connect(self.c_Torrent)
        btn24.clicked.connect(self.Video_Screen_Recorder)
        btn25.clicked.connect(self.WordPress)
        btn26.clicked.connect(self.Eclipse)
        btn27.clicked.connect(self.Pidgin)
        btn28.clicked.connect(self.qBittorrent)
        btn29.clicked.connect(self.uget_Downloader)
        btn30.clicked.connect(self.Keep_Password_Manager)
        btn31.clicked.connect(self.gufw_Firewall)
        btn32.clicked.connect(self.Gimp)
        btn33.clicked.connect(self.Backuppc)
        btn34.clicked.connect(self.Kate)
        btn35.clicked.connect(self.Deluge)
        btn36.clicked.connect(self.Google_Chrome)
        btn37.clicked.connect(self.Rhythmbox)
        btn38.clicked.connect(self.Dosbox)
        btn39.clicked.connect(self.WPS_Office)
        btn40.clicked.connect(self.Callingra_Office)
        btn41.clicked.connect(self.Free_Office)
        btn42.clicked.connect(self.Synaptic)
        btn43.clicked.connect(self.Kmail)
        btn44.clicked.connect(self.Kopete)
        btn45.clicked.connect(self.Emacs)
        btn46.clicked.connect(self.Internet_Explorer)
        btn47.clicked.connect(self.Tuxpaint)
        btn48.clicked.connect(self.kftpgrabber)
        btn49.clicked.connect(self.Sonata)
        btn50.clicked.connect(self.Joe)




        
        self.statusBar()
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Priority Cliqk')
        self.show()
        
    def Chromium(self):
      
        self.os = os
        os.system("sh Chromium.sh") 
        self.statusBar().showMessage('Chromium has been started to download and install in your system')

    def Tor(self):
        self.os = os
        os.system("sh Tor.sh") 
        self.statusBar().showMessage('Tor has been started to download and install in your system')

    def Skype(self):
        self.os = os
        os.system("sh Skype.sh") 
        self.statusBar().showMessage('Skype has been started to download and install in your system')

    def Team_Viewer(self):
        self.os = os
        os.system("sh Team_Viewer.sh") 
        self.statusBar().showMessage('Team Viewer has been started to download and install in your system')

    def Adobe_Flash_Player(self):
        self.os = os
        os.system("sh Adobe_Flash_Player.sh") 
        self.statusBar().showMessage('Adobe Flash Player has been started to download and install in your system')

    def Notepad(self):
        self.os = os
        os.system("sh Notepad.sh") 
        self.statusBar().showMessage('Notepad++  has been started to download and install in your system')

    def Sublime_Text(self):
        self.os = os
        os.system("sh Sublime_Text.sh") 
        self.statusBar().showMessage('Sublime Text has been started to download and install in your system')

    def Virtual_Box(self):
        self.os = os
        os.system("sh Virtual_Box.sh") 
        self.statusBar().showMessage('Virtual Box has been started to download and install in your system')

    def Unetbootin(self):
        self.os = os
        os.system("sh Unetbootin.sh") 
        self.statusBar().showMessage('Unetbootin has been started to download and install in your system')

    def Claws(self):
        self.os = os
        os.system("sh Claws.sh") 
        self.statusBar().showMessage('Claws Mail Client has been started to download and install in your system')

    def xChat(self):
        self.os = os
        os.system("sh xChat.sh") 
        self.statusBar().showMessage('xChat-IRC has been started to download and install in your system')

    def Libre_Office(self):
        self.os = os
        os.system("sh Libre_Office.sh") 
        self.statusBar().showMessage('Libre Office has been started to download and install in your system')

    def Audiocity(self):
        self.os = os
        os.system("sh Audiocity.sh") 
        self.statusBar().showMessage('Audiocity has been started to download and install in your system')

    def Pinta(self):
        self.os = os
        os.system("sh Pinta.sh") 
        self.statusBar().showMessage('Pinta has been started to download and install in your system')

    def Audacious(self):
        self.os = os
        os.system("sh Audacious.sh") 
        self.statusBar().showMessage('Audacious has been started to download and install in your system')

    def Amarok(self):
        self.os = os
        os.system("sh Amarok.sh") 
        self.statusBar().showMessage('Amarok Player has been started to download and install in your system')

    def VLC(self):
        self.os = os
        os.system("sh VLC.sh") 
        self.statusBar().showMessage('VLC Video Player has been started to download and install in your system')

    def Java(self):
        self.os = os
        os.system("sh Java.sh") 
        self.statusBar().showMessage('Java JDK has been started to download and install in your system')

    def Inkscape(self):
        self.os = os
        os.system("sh Inkscape.sh") 
        self.statusBar().showMessage('Inkscape has been started to download and install in your system')

    def Printer_driver(self):
        self.os = os
        os.system("sh Printer_driver.sh") 
        self.statusBar().showMessage('Printer Driver has been started to download and install in your system')

    def Filezillia(self):
        self.os = os
        os.system("sh Filezillia.sh") 
        self.statusBar().showMessage('Filezillia has been started to download and install in your system')

    def Video_Recorder(self):
        self.os = os
        os.system("sh Video_Recorder.sh") 
        self.statusBar().showMessage('Video Recorder has been started to download and install in your system')

    def c_Torrent(self):
        self.os = os
        os.system("sh c_Torrent.sh") 
        self.statusBar().showMessage('c Torrent-client has been started to download and install in your system')

    def Video_Screen_Recorder(self):
        self.os = os
        os.system("sh Video_Screen_Recorder.sh") 
        self.statusBar().showMessage('Video Screen Recorder has been started to download and install in your system')

    def WordPress(self):
        self.os = os
        os.system("sh WordPress.sh") 
        self.statusBar().showMessage('WordPress has been started to download and install in your system')

    def Eclipse(self):
        self.os = os
        os.system("sh Eclipse.sh") 
        self.statusBar().showMessage('Eclipse has been started to download and install in your system')

    def Pidgin(self):
        self.os = os
        os.system("sh Pidgin.sh") 
        self.statusBar().showMessage('Pidgin has been started to download and install in your system')

    def qBittorrent(self):
        self.os = os
        os.system("sh qBittorrent.sh") 
        self.statusBar().showMessage('qBittorrent has been started to download and install in your system')

    def uget_Downloader(self):
        self.os = os
        os.system("sh uget_Downloader.sh") 
        self.statusBar().showMessage('uget Downloader has been started to download and install in your system')

    def Keep_Password_Manager(self):
        self.os = os
        os.system("sh Keep_Password_Manager.sh") 
        self.statusBar().showMessage('Keep Password Manager has been started to download and install in your system')

    def gufw_Firewall(self):
        self.os = os
        os.system("sh gufw_Firewall.sh") 
        self.statusBar().showMessage('gufw Firewall has been started to download and install in your system')

    def Gimp(self):
        self.os = os
        os.system("sh Gimp.sh") 
        self.statusBar().showMessage('Gimp has been started to download and install in your system')
 
    def Backuppc(self):
        self.os = os
        os.system("sh Backuppc.sh") 
        self.statusBar().showMessage('Backuppc has been started to download and install in your system')
 
    def Kate(self):
        self.os = os
        os.system("sh Kate.sh") 
        self.statusBar().showMessage('Kate has been started to download and install in your system')
 
    def Deluge(self):
        self.os = os
        os.system("sh Deluge.sh") 
        self.statusBar().showMessage('Deluge has been started to download and install in your system')
 
    def Google_Chrome(self):
        self.os = os
        os.system("sh Google_Chrome.sh") 
        self.statusBar().showMessage('Google Chrome has been started to download and install in your system')
 
    def Rhythmbox(self):
        self.os = os
        os.system("sh Rhythmbox.sh") 
        self.statusBar().showMessage('Rhythmbox has been started to download and install in your system')
 
    def Dosbox(self):
        self.os = os
        os.system("sh Dosbox.sh") 
        self.statusBar().showMessage('Dosbox has been started to download and install in your system')
 
    def WPS_Office(self):
        self.os = os
        os.system("sh WPS_Office.sh") 
        self.statusBar().showMessage('WPS Office has been started to download and install in your system')
 
    def Callingra_Office(self):
        self.os = os
        os.system("sh Callingra_Office.sh") 
        self.statusBar().showMessage('Callingra Office has been started to download and install in your system')
 
    def Free_Office(self):
        self.os = os
        os.system("sh Free_Office.sh") 
        self.statusBar().showMessage('Free Office has been started to download and install in your system')
 
    def Synaptic(self):
        self.os = os
        os.system("sh Synaptic.sh") 
        self.statusBar().showMessage('Synaptic has been started to download and install in your system')
 
    def Kmail(self):
        self.os = os
        os.system("sh Kmail.sh") 
        self.statusBar().showMessage('Kmail has been started to download and install in your system')
 
   
    def Kopete(self):
        self.os = os
        os.system("sh Kopete.sh") 
        self.statusBar().showMessage('Kopete has been started to download and install in your system')
 
    def Emacs(self):
        self.os = os
        os.system("sh Emacs.sh") 
        self.statusBar().showMessage('Emacs has been started to download and install in your system')
 
    def Internet_Explorer(self):
        self.os = os
        os.system("sh Internet_Explorer.sh") 
        self.statusBar().showMessage('Internet Explorer has been started to download and install in your system')
 
    def Tuxpaint(self):
        self.os = os
        os.system("sh Tuxpaint.sh") 
        self.statusBar().showMessage('Tuxpaint has been started to download and install in your system')
 
    def kftpgrabber(self):
        self.os = os
        os.system("sh kftpgrabber.sh") 
        self.statusBar().showMessage('kftpgrabber has been started to download and install in your system')
 
    def Sonata(self):
        self.os = os
        os.system("sh sssSonata.sh") 
        self.statusBar().showMessage('Sonata has been started to download and install in your system')
 
    
    def Joe(self):
        self.os = os
        os.system("sh Joe.sh") 
        self.statusBar().showMessage('Joe  has been started to download and install in your system')
 
    
    

        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()