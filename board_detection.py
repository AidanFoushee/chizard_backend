# import numpy as np
# import cv2 as cv
# import glob

# def detect_board(img):
    
#     # Convert to gray
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # Apply Gaussian Blur to reduce noise
#     blurred = cv.GaussianBlur(gray, (5, 5), 0)

#     # Detect edges using Canny
#     edges = cv.Canny(blurred, 50, 150, apertureSize=3)

#     # Detect lines using Hough Transform (tuned parameters)
#     lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=20)

#     # Draw detected lines
#     output = img.copy()
#     if lines is not None:
#         for line in lines:
#             x1, y1, x2, y2 = line[0]
            
#             # Calculate angle of the line
#             angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            
#             # Keep only near-vertical and near-horizontal lines (avoid diagonals)
#             if abs(angle) < 10 or abs(angle) > 80:
#                 cv.line(output, (x1, y1), (x2, y2), (0, 255, 0), 2)

#     return output

import cv2
import numpy as np

def detect_board_grid(image):
    """
    Detects the chessboard grid using Hough Line Transform.
    Returns a list of square positions.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
    if lines is None:
        return None

    horizontal_lines = []
    vertical_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(y2 - y1) < abs(x2 - x1):  # Horizontal
            horizontal_lines.append((y1, y2))
        else:  # Vertical
            vertical_lines.append((x1, x2))

    # Sort lines to get ordered rows and columns
    horizontal_lines = sorted(set(y for y1, y2 in horizontal_lines for y in (y1, y2)))
    vertical_lines = sorted(set(x for x1, x2 in vertical_lines for x in (x1, x2)))

    if len(horizontal_lines) != 9 or len(vertical_lines) != 9:
        print("Warning: Detected grid lines do not match expected count (9 each).")
        return None

    # Create 8x8 grid of square positions
    squares = []
    for row in range(8):
        for col in range(8):
            squares.append((
                (vertical_lines[col], horizontal_lines[row]),  # Top-left corner
                (vertical_lines[col+1], horizontal_lines[row+1])  # Bottom-right corner
            ))

    return squares
