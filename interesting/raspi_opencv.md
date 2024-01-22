sudo apt-get update

sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

sudo apt-get install python3-opencv

sudo apt-get install libopenblas-dev libblas-dev libatlas-base-dev

sudo pip3 install cython

git clone --recursive https://github.com/pytorch/pytorch

if failes while recursively cloning: git submodule update --init --recursive

cd pytorch
git checkout tags/v1.10.0  # Use the latest stable version
python3 setup.py build_deps
sudo python3 setup.py develop

sudo pip3 install torchvision torchaudio

