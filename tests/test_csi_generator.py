from pathlib import Path


def test_project_structure():

    assert Path(
        "wifi-sensing-platform"
    ).exists()


def test_simulator_exists():

    assert Path(
        "wifi-sensing-platform/collector/simulator/csi_generator.py"
    ).exists()

