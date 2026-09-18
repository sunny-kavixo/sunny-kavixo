# Autonomous Wheeled Robot — Control Core

A **working, hardware-independent autonomy layer** for a Raspberry Pi-class wheeled robot. It implements safety-first motion decisions from distance telemetry and perception state, with automated tests.

![Robot control architecture](docs/robot-architecture.svg)

## Engineering problem

Robot control logic should be testable before motors are connected. This project separates the decision layer from hardware drivers so safety behaviour can be verified deterministically.

## Real control process

```text
Camera / sensor drivers
        ↓
Telemetry + perception state
        ↓
Safety decision layer
        ↓
STOP / SLOW / FORWARD / SEARCH
        ↓
Motor-driver adapter
        ↓
Physical robot
```

## Current implementation

- Invalid telemetry → **STOP**
- Obstacle closer than 20 cm → **STOP**
- Obstacle between 20–45 cm → **SLOW**
- Clear path + target visible → **FORWARD**
- Clear path + no target → **SEARCH**

Run the control core:

```bash
python robot_logic.py
```

Run automated tests:

```bash
python -m pytest tests/
```

## Hardware integration path

The decision layer is intentionally independent of GPIO and motor libraries. Real Raspberry Pi camera, ultrasonic, and motor-controller adapters can feed telemetry into the same tested decision function.

## Honest scope

This repository contains a tested control core and architecture. It does **not** claim that the physical robot is autonomously operating from this repository alone.

## Skills demonstrated

**Python · Robotics · Autonomous Systems · Sensor Logic · Safety Engineering · Raspberry Pi Architecture · Testing**
