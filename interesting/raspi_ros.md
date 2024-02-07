## ROS 2 Iron core

```
sudo apt-get install -y python3-rosdep2 wget python3-flake8-docstrings python3-pytest-cov python3-pytest-rerunfailures python3-vcstools libx11-dev libxrandr-dev libasio-dev libtinyxml2-dev libacl1-dev libtinyxml2-dev

pip install colcon-common-extensions vcstool flake8-blind-except flake8-builtins flake8-class-newline flake8-comprehensions flake8-deprecated flake8-import-order flake8-quotes pytest-repeat pylibacl lark-parser

export PATH=$PATH:/home/pi/.local/bin

mkdir -p ~/ros2_iron/src
cd ~/ros2_iron

sudo reboot

cd ~/ros2_iron

vcs import --input https://raw.githubusercontent.com/ros2/ros2/iron/ros2.repos src

sudo rm /etc/ros/rosdep/sources.list.d/20-default.list

sudo apt upgrade
sudo rosdep init
rosdep update

rosdep install --from-paths src --ignore-src --rosdistro iron -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers python3-vcstool ignition-cmake2 ignition-math6"

sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

screen -S colcon_build

???

colcon build --symlink-install --cmake-clean-first
colcon build --symlink-install --parallel-workers 1
colcon build --symlink-install --packages-skip rviz --cmake-clean-first --parallel-workers 1

???

source ...
```

** Never succesfully installed... **
