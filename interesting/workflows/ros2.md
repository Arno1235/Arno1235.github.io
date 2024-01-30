# ROS 2 (Robot Operating System 2)

## Installation

### Ubuntu

#### Step 1: Setup Sources and Keys

```bash
sudo apt update
sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

#### Step 2: Install ROS 2

```bash
sudo apt update
sudo apt install ros-<distro>-desktop
```

Replace `<distro>` with the ROS 2 distribution (e.g., `foxy`, `galactic`, etc.).

#### Step 3: Setup Environment

```bash
source /opt/ros/<distro>/setup.bash
```

Add the above line to your `.bashrc` or `.zshrc` file to automatically set up the ROS 2 environment on each new shell session.

## Usage

### Create and Build a ROS 2 Workspace

#### Step 1: Create a Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```

#### Step 2: Source the Workspace

```bash
source ~/ros2_ws/install/setup.bash
```

Add the above line to your `.bashrc` or `.zshrc` file for automatic sourcing.

### Basic ROS 2 Commands

- **Run a ROS 2 Node:**

  ```bash
  ros2 run <package_name> <node_name>
  ```

- **List Available Nodes:**

  ```bash
  ros2 node list
  ```

- **List Topics:**

  ```bash
  ros2 topic list
  ```

- **Publish to a Topic:**

  ```bash
  ros2 topic pub <topic_name> <message_type> '<message_content>'
  ```

- **Subscribe to a Topic:**

  ```bash
  ros2 topic echo <topic_name>
  ```

### Create a ROS 2 Package

#### Step 1: Create a Package

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python <package_name>
```

#### Step 2: Build the Workspace

```bash
cd ~/ros2_ws
colcon build
```

### ROS 2 Development Tools

- **ROS 2 Launch System:**

  ```bash
  ros2 launch <package_name> <launch_file_name>
  ```

- **ROS 2 Bag Recorder:**

  ```bash
  ros2 bag record -a
  ```

- **ROS 2 Parameter Commands:**

  ```bash
  ros2 param set <node_name> <parameter_name> <parameter_value>
  ```

- **ROS 2 GUI (RViz):**

  ```bash
  ros2 run rviz2 rviz2
  ```

### Cleanup

- **Remove ROS 2 Installation:**

  ```bash
  sudo apt remove ros-<distro>-desktop
  sudo apt autoremove
  ```

- **Remove ROS 2 Workspace:**

  ```bash
  rm -rf ~/ros2_ws
  ```

Note: Replace `<distro>`, `<package_name>`, `<node_name>`, `<launch_file_name>`, `<topic_name>`, `<message_type>`, `<message_content>`, `<parameter_name>`, and `<parameter_value>` with your actual values. Adjust the commands according to the ROS 2 distribution you installed.
