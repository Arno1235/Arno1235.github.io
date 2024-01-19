https://arducam.com/downloads/arducam-imx519-start-guide.pdf
https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/Quick-Start-Guide/
4656 (H) × 3496 (V)


sudo raspi-config
-> enable camera
-> enable ssh
-> enable glamor

sudo apt update
sudo apt full-upgrade

lsb_release -a
cat /etc/os-release
hostnamectl

cd Downloads

wget -O install_pivariety_pkgs.sh https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/releases/download/install_script/install_pivariety_pkgs.sh
chmod +x install_pivariety_pkgs.sh

./install_pivariety_pkgs.sh -p libcamera

./install_pivariety_pkgs.sh -p libcamera_apps

sudo apt-get install vim

sudo vim /boot/config.txt
** add dtoverlay=imx519 under the line [all]
** comment dtoverlay under [pi4]
sudo reboot

python test:

from picamera2 import Picamera2
import time

picam2 = Picamera2()

camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")

