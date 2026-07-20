"""
Synthetic CSI data generator.

Used for software testing before connecting ESP32 hardware.
Generates Wi-Fi CSI-like amplitude data.
"""

import csv
import random
import time
from pathlib import Path


OUTPUT_FILE = Path("csi_sample.csv")


def generate_csi_sample():
    """
    Generate one synthetic CSI packet.
    """

    timestamp = time.time()

    # Simulate 64 subcarriers
    amplitudes = [
        round(random.uniform(20, 80), 2)
        for _ in range(64)
    ]

    return [
        timestamp,
        *amplitudes
    ]


def generate_dataset(samples=1000):

    with OUTPUT_FILE.open("w", newline="") as file:

        writer = csv.writer(file)

        header = [
            "timestamp"
        ] + [
            f"subcarrier_{i}"
            for i in range(64)
        ]

        writer.writerow(header)

        for _ in range(samples):

            writer.writerow(
                generate_csi_sample()
            )

            time.sleep(0.01)


if __name__ == "__main__":

    print("Generating CSI dataset...")

    generate_dataset()

    print(
        f"Created {OUTPUT_FILE}"
    )
