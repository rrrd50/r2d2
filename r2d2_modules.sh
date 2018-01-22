#!/bin/sh
# Robot Installation Notes
# You should be able to execute this as root, but things may change and errors occur.
# last edited by RayS 1/17/2018

# Python 3.5 is currently the installed version
# Python Modules
# run with: $ sudo ./r2d2_modules.sh

apt-get update
apt-get -y install python-pip
apt-get -y install python3-pip
pip3 install flask
pip3 install pyserial
##pip3 install pyinstaller
##pyinstaller r2d2.py
#pip3 install GPIO
pip3 install PyCRC
pip3 install RPi.GPIO
##apt-get -y install python3-rpi.gpio


# Clone github repo, creates the r2d2 directory
apt-get -y install git
git clone https://github.com/rsundstrom/r2d2.git
chown -R pi:pi r2d2

