# Package Import
import numpy as np
import argparse

# Constants
theta_range = np.arange(0, 15, 1)

# Arguments
parser = argparse.ArgumentParser(description="Gather numeric inputs.")

parser.add_argument(
    "--dist", type=str, help="Distance from your face to the TV's wall. Add m or ft to the number e.g. 10m"
)
parser.add_argument(
    "--height", type=str, help="How far your face is off the ground while watching TV. Add m or ft to the number e.g. 4ft."
)
args = parser.parse_args()


# Function Definitions
def get_height(theta):
    return round(args.dist * np.tan(np.radians(theta)) + args.height, 3)


if __name__ == "__main__":
    for theta in theta_range:
        print(f"Angle: {theta}", f"TV Height: {get_height(theta)}")
