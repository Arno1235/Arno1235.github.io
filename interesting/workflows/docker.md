# Docker

## Installation

### MacOs

Install Docker Desktop by downloading the installer from the [official website](https://www.docker.com/products/docker-desktop).

### Ubuntu

Install Docker Engine using the following commands:

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Add your user to the `docker` group to run Docker commands without `sudo`:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in to apply the changes.

### Windows

Install Docker Desktop by downloading the installer from the [official website](https://www.docker.com/products/docker-desktop).

## Usage

### Basic Commands

- **Check Docker Version:**

  ```bash
  docker version
  ```

- **List Docker Images:**

  ```bash
  docker images
  ```

- **List Running Containers:**

  ```bash
  docker ps
  ```

- **List All Containers:**

  ```bash
  docker ps -a
  ```

### Managing Containers

- **Run a Container:**

  ```bash
  docker run <image_name>
  ```

- **Run a Container in the Background:**

  ```bash
  docker run -d <image_name>
  ```

- **Stop a Running Container:**

  ```bash
  docker stop <container_id>
  ```

- **Remove a Container:**

  ```bash
  docker rm <container_id>
  ```

### Managing Images

- **Pull an Image from Docker Hub:**

  ```bash
  docker pull <image_name>
  ```

- **Build an Image from Dockerfile:**

  ```bash
  docker build -t <image_name> <path_to_dockerfile>
  ```

- **Remove an Image:**

  ```bash
  docker rmi <image_name>
  ```

### Docker Compose

- **Install Docker Compose:**

  ```bash
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```

- **Check Docker Compose Version:**

  ```bash
  docker-compose version
  ```

- **Run Docker Compose:**

  ```bash
  docker-compose up
  ```

- **Stop Docker Compose:**

  ```bash
  docker-compose down
  ```

### Docker Registry

- **Push Image to Docker Registry:**

  ```bash
  docker push <image_name>
  ```

- **Pull Image from Docker Registry:**

  ```bash
  docker pull <registry_url>/<image_name>
  ```

- **Login to Docker Registry:**

  ```bash
  docker login <registry_url>
  ```

- **Logout from Docker Registry:**

  ```bash
  docker logout
  ```

## Cleanup

- **Remove All Containers:**

  ```bash
  docker rm $(docker ps -aq)
  ```

- **Remove All Images:**

  ```bash
  docker rmi $(docker images -q)
  ```

Note: Replace `<image_name>`, `<container_id>`, `<path_to_dockerfile>`, and `<registry_url>` with your actual values.
