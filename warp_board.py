import cv2
import numpy as np

def warp_board(image, corners, size=400):
    """
    Warps the chessboard for accurate square mapping.
    """
    dst_pts = np.float32([[0, 0], [size, 0], [0, size], [size, size]])
    M = cv2.getPerspectiveTransform(np.float32(corners), dst_pts)
    return cv2.warpPerspective(image, M, (size, size))
