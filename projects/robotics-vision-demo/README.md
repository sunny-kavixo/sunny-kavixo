# Autonomous Wheeled Robot — Control Core

A working, hardware-independent autonomy layer for a Raspberry Pi-class wheeled robot. It implements safety-first motion decisions from distance telemetry and perception state.

## 🖼️ Control architecture

```mermaid
flowchart LR
A[Camera / Sensors] --> B[Telemetry + Perception]
B --> C[Safety Decision Layer]
C --> D{Distance / Target}
D -->|< 20 cm| E[STOP]
D -->|20–45 cm| F[SLOW]
D -->|Clear + target| G[FORWARD]
D -->|Clear + no target| H[SEARCH]
E --> I[Motor Driver]
F --> I
G --> I
H --> I
```

## Engineering problem

Robot control logic should be testable before motors are connected. This project separates the decision layer from hardware drivers so safety behaviour can be verified deterministically.

## Current implementation

- Invalid telemetry → **STOP**
- Obstacle closer than 20 cm → **STOP**
- Obstacle between 20–45 cm → **SLOW**
- Clear path + target visible → **FORWARD**
- Clear path + no target → **SEARCH**

## ▶ Run

```bash
python robot_logic.py
```

## 🧪 Automated tests

```bash
python -m pytest tests/
```

Tests cover obstacle stopping, slow mode, and target-search behaviour.

## Hardware integration path

Real Raspberry Pi camera, ultrasonic, and motor-controller adapters can feed telemetry into the same tested decision function. Hardware-specific code stays outside the decision layer.

## Honest scope

This repository contains a tested control core and architecture. It does not claim that a physical robot is autonomously operating from this repository alone.

## Skills demonstrated

**Python · Robotics · Autonomous Systems · Sensor Logic · Safety Engineering · Raspberry Pi Architecture · Testing**
