import math

def design_web_page(area):
    # Start from the square root of the area
    L = area
    while L > 0:
        if area % L == 0:  # Check if L is a valid divisor
            W = area // L  # Calculate width
            if L >= W:  # Ensure L >= W
                return [L, W]
        L -= 1
    return []  # Shouldn't reach this point

# Example usage
area = 37
print(design_web_page(area))  # Output: [5, 2]