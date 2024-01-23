https://gist.github.com/wenig/8bab88dede5c838660dd05b8e5b2e23b

sudo apt-get update

sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

sudo apt-get install python3-opencv

sudo apt-get install libopenblas-dev libblas-dev libatlas-base-dev

sudo pip3 install cython

git clone https://github.com/pytorch/pytorch
cd pytorch
git checkout tags/v1.4.0
git submodule sync
git submodule update --init --recursive
git submodule update --remote third_party/protobuf
git submodule update --init --recursive

sudo apt-get install libprotobuf-dev protobuf-compiler

python setup.py clean
CMAKE_C_COMPILER=$(which mpicc) CMAKE_CXX_COMPILER=$(which mpicxx) USE_DISTRIBUTED=1 USE_NUMPY=1 BUILD_TEST=0 Protobuf_LIBRARY=/usr/lib/arm-linux-gnueabihf/libprotobuf.so USE_MKLDNN=OFF USE_CUDA=OFF USE_CUDNN=OFF python setup.py bdist_wheel



CMAKE_C_COMPILER=$(which mpicc) CMAKE_CXX_COMPILER=$(which mpicxx) USE_DISTRIBUTED=1 USE_NUMPY=1 BUILD_TEST=0 Protobuf_LIBRARY=/usr/lib/arm-linux-gnueabihf/libprotobuf.so USE_MKLDNN=OFF USE_CUDA=OFF USE_CUDNN=OFF DCMAKE_CXX_FLAGS=-latomic DOPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic python setup.py bdist_wheel


CMAKE_C_COMPILER=$(which mpicc) \
CMAKE_CXX_COMPILER=$(which mpicxx) \
USE_DISTRIBUTED=1 \
USE_NUMPY=1 \
BUILD_TEST=0 \
Protobuf_LIBRARY=/usr/lib/arm-linux-gnueabihf/libprotobuf.so \
USE_MKLDNN=OFF \
USE_CUDA=OFF \
USE_CUDNN=OFF \
DCMAKE_CXX_FLAGS="-latomic" \
DOPENCV_EXTRA_EXE_LINKER_FLAGS="-latomic" \
python setup.py bdist_wheel




If fails alsways first:
rm -rf build
python setup.py clean



--

pip install dist/torch-1.4.0...whl

sudo pip3 install torchvision torchaudio

