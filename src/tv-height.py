# Package Import
import numpy as np

# Constants
y0 = 3
x0 = 12
theta_range = np.arange(0, 15, 1)

# Function Definitions
def get_height(theta):
	return (
		x0*np.tan(np.radians(theta))+y0
		)

if __name__ == "__main__":
	for theta in theta_range:
		print(
			f"Angle: {theta}",
			f"TV Height: {get_height(theta)}"
		)
