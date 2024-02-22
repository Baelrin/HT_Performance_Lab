import sys
import numpy as np


def calculate_distance(points, circle_center):
    """
    Calculates the distances from points to the center of a circle.
    """
    return np.sqrt(np.sum((points - circle_center)**2, axis=1))


def main():
    """
    The main function to read files and calculate distances.
    """
    if len(sys.argv) != 3:
        print("Usage: python master.py <circle_file_path> <points_file_path>")
        return []

    circle_file_path = sys.argv[1]
    points_file_path = sys.argv[2]

    try:
        circle_center = np.loadtxt(circle_file_path, usecols=(0,   1))
        circle_radius = np.loadtxt(circle_file_path, usecols=2)
    except FileNotFoundError:
        print(f"Circle file not found: {circle_file_path}")
        return []
    except ValueError:
        print("Invalid circle file format")
        return []

    try:
        points = np.loadtxt(points_file_path, usecols=(0,   1))
    except FileNotFoundError:
        print(f"Points file not found: {points_file_path}")
        return []
    except ValueError:
        print("Invalid points file format")
        return []

    # Check the coordinate range
    if not np.all((points >= -38) & (points <= 38)):
        print("Coordinates are out of range (-38 to  38)")
        return []

    # Check the number of points
    if len(points) < 1 or len(points) > 100:
        print("Invalid number of points (1 to  100)")
        return []

    distances = calculate_distance(points, circle_center)
    results = np.where(distances == circle_radius,   0,
                       np.where(distances < circle_radius,   1,   2))

    return results.tolist()


if __name__ == "__main__":
    results = main()
    for result in results:
        print(result)
