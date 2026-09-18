"""Hardware-independent autonomous robot decision logic."""

from dataclasses import dataclass

@dataclass
class Telemetry:
    front_distance_cm: float
    target_visible: bool

def decide(t: Telemetry) -> str:
    if telemetry_invalid(telemetry := t):
        return "STOP"
    if telemetry.front_distance_cm < 20:
        return "STOP"
    if telemetry.front_distance_cm < 45:
        return "SLOW"
    if telemetry.target_visible:
        return "FORWARD"
    return "SEARCH"

def telemetry_invalid(t: Telemetry) -> bool:
    return t.front_distance_cm <= 0 or t.front_distance_cm > 500

if __name__ == "__main__":
    samples = [
        Telemetry(12, True),
        Telemetry(32, True),
        Telemetry(80, True),
        Telemetry(80, False),
    ]
    for sample in samples:
        print(sample, "->", decide(sample))
