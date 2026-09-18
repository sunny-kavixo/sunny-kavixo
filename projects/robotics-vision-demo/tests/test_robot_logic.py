from robot_logic import Telemetry, decide

def test_stop_for_close_obstacle():
    assert decide(Telemetry(10, True)) == "STOP"

def test_slow_for_medium_distance():
    assert decide(Telemetry(30, True)) == "SLOW"

def test_search_when_no_target():
    assert decide(Telemetry(100, False)) == "SEARCH"
