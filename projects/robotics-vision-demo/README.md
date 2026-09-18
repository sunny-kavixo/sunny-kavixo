# Robotics Vision & Telemetry Demo

A simulation-oriented project structure for an autonomous wheeled robot: camera observations, distance telemetry, safety decisions, and a simple command layer.

## Skills demonstrated
- Robotics software architecture
- Computer-vision pipeline concepts
- Sensor fusion concepts
- Autonomous navigation logic
- Raspberry Pi-oriented system design

## Architecture
Camera / ultrasonic sensors -> perception -> safety state -> motion command.

The repository focuses on explainable interfaces so hardware drivers can later be replaced with Raspberry Pi GPIO, camera, and motor-driver implementations.
