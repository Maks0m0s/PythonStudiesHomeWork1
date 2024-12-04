import math


def arc_length(radius, angle_radians):
    """
    Calculate the length of an arc for a given radius and angle in radians.

    Parameters:
        radius (float): The radius of the circle.
        angle_radians (float): The angle in radians.

    Returns:
        float: The length of the arc.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    if angle_radians < 0:
        raise ValueError("Angle in radians cannot be negative.")

    # Calculate the arc length using the formula L = r * θ
    length = radius * angle_radians
    return length


def degrees_to_radians(angle_degrees):
    """
    Convert an angle from degrees to radians.

    Parameters:
        angle_degrees (float): The angle in degrees.

    Returns:
        float: The angle in radians.
    """
    return math.radians(angle_degrees)


# Example usage
radius = 7  # Radius of the circle
angle_degrees = 90  # Angle in degrees

# Convert degrees to radians
angle_radians = degrees_to_radians(angle_degrees)

# Calculate the arc length
arc = arc_length(radius, angle_radians)

print(f"Довжина дуги для радіуса {radius} і кута {angle_degrees}°: {arc:.2f}")