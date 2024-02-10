# IMX 519

https://arducam.com/downloads/arducam-imx519-start-guide.pdf

https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/Quick-Start-Guide/

https://www.tomshardware.com/how-to/use-picamera2-take-photos-with-raspberry-pi

4656 (H) × 3496 (V)

```
sudo raspi-config
-> enable camera
-> enable ssh
-> enable glamor
```

```
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
```

Python test

```
from picamera2 import Picamera2
import time

picam2 = Picamera2()

camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
```

# ToF Camera

```
git clone https://github.com/ArduCAM/Arducam_tof_camera.git

cd Arducam_tof_camera

./Install_dependencies.sh
./Install_dependencies_python.sh

./compile.sh
```

```
sudo vim /boot/config.txt

** add under the line [all]:
dtoverlay=arducam-pivariety,media-controller=0

sudo reboot
```

```
curl -s --compressed "https://arducam.github.io/arducam_ppa/KEY.gpg" | sudo apt-key add -
sudo curl -s --compressed -o /etc/apt/sources.list.d/arducam_list_files.list "https://arducam.github.io/arducam_ppa/arducam_list_files.list"
sudo apt update
sudo apt install arducam-config-parser-dev arducam-usb-sdk-dev arducam-tof-sdk-dev

sudo apt-get update
sudo apt-get install build-essential cmake 
sudo apt-get install libopencv-dev


cd Arducam_tof_camera/example
mkdir build && cd build
cmake .. && make

./c/test_c
```

Python test

```
import sys
import cv2
import numpy as np
import ArducamDepthCamera as ac

if __name__ == "__main__":
    cam = ac.ArducamCamera()
    if cam.open(ac.TOFConnect.CSI,0) != 0 :
        print("initialization failed")
    if cam.start(ac.TOFOutput.RAW) != 0 :
        print("Failed to start camera")

    while True:
        frame = cam.requestFrame(200)
        if frame != None:
            buf = frame.getRawData()
            cam.releaseFrame(frame)
            cv2.imwrite("frame.png", buf.astype(np.float32))
            exit_ = True
            cam.stop()
            cam.close()
            sys.exit(0)
```
