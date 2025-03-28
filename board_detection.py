import numpy as np
import cv2 as cv
import glob

def detect_board(img):
    
    # Convert to gray
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny
    edges = cv.Canny(blurred, 50, 150, apertureSize=3)

    # Detect lines using Hough Transform (tuned parameters)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=20)

    # Draw detected lines
    output = img.copy()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            
            # Calculate angle of the line
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            
            # Keep only near-vertical and near-horizontal lines (avoid diagonals)
            if abs(angle) < 10 or abs(angle) > 80:
                cv.line(output, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return output
