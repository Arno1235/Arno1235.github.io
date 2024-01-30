https://docs.ros.org/en/foxy/How-To-Guides/Installing-on-Raspberry-Pi.html

Install docker

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh

git clone https://github.com/osrf/docker_images
cd docker_images/ros2/source/devel/

sudo docker build -t ros_docker .




sudo apt install ros-[VERSION]-rviz2
