# Drone idea

## Links

- PXFmini (discontinued) https://ardupilot.org/copter/docs/common-pxfmini.html
- Navio2 https://navio2.hipi.io/
- https://dojofordrones.com/pi-zero-drone/
- https://github.com/erlerobot/erle_gitbook_erlebrain/
- https://github.com/erlerobot/PXF2/
- https://github.com/chipiki/PXFmini_v2/
- https://ardupilot.org/dev/docs/ros-aruco-detection.html
- https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html
- http://wiki.ros.org/mavros
- https://www.rpanion.com/product/pi-connect-lite/
- https://github.com/stephendade/Pi-Connect/
- https://timhanewich.medium.com/taking-flight-with-the-raspberry-pi-pico-micropython-diy-quadcopter-drone-61ed4f7ee746
- https://www.tomshardware.com/raspberry-pi/how-to-use-dual-cameras-on-the-raspberry-pi-5

## Requirements PCB board

- Can click on Raspberry Pi 3 or above (also zero?) as a shield
- Barometer
- IMU sensor (gyro and accelerometer)
- Get power from lipo battery (with voltage protection)
- PWM output (for ESC's)
- PWM input (for transmitter)

FASE 2

- Possibility to connect extra camera?
- Expansion ports
- GPS

## Roadmap

### Fase 0
Get everything working separately

- Drone flying for indoor (prop guards)
- Raspberry pi + 3D sensor (+ RGB camera) in ROS

### Fase 1
Get it all talking to each other

- Raspberry pi + mavlink + mavros
- Get location data from the flight controller
- Try SLAM

### Fase 2
Automated flying

- Raspberry pi controls the drone
