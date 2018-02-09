# r2d2
r2d2 robot software


Commands to check on usb connection. It should just work, but sometimes I have
to mess with it. the Roboclaw to usb cable connection may be the problem.

ls /dev | grep ttyA (ttyACM0 should appear)
lsusb (should show your usb serial connection. roboclas is: 03eb:2404 Atmel Corp.)
dmesg | grep usb (shows a log of all usb devices attached and unattached since boot)


