#!/bin/bash
# file: photoboothsetup.sh
#
# Setup the folders and files required for the GSOC Raspberry Pi Photobooth
#
# You will need to have your Raspberry Pi connected to the Internet, and use �sudo sh photoboothsetup.sh� to run this script.
#
 
# check if sudo is used
if [ "$(id -u)" != 0 ]; then
  echo 'Sorry, you need to run this script with sudo'
  exit 1
fi
 
# install Adafruit MPR121 library
unzip Adafruit_Python_MPR121-master.zip
cd Adafruit_Python_MPR121-master
python3 setup.py install

pip3 install -r requirements.txt

