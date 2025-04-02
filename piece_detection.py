import os
import cv2
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO("best.pt")  # Replace with your trained model

def detect_pieces(image_path):
    # Convert to absolute path
    absolute_path = os.path.abspath(image_path)
    print(f"!!! Reading image from: {absolute_path}")

    # Check if the file exists
    if not os.path.exists(absolute_path):
        print(f"❌ File not found: {absolute_path}")
        return []

    # Read the image
    image = cv2.imread(absolute_path)
    if image is None:
        print(f"❌ Failed to load image from {absolute_path}")
        return []

    # Run inference
    results = model.predict(image)
    coordinates = []

    # Loop through detections and extract bounding boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # Get bounding box coordinates
            class_id = int(box.cls[0])  # Class ID

            coordinates.append(f"Class: {class_id}, BBox: ({x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f})")

    return coordinates

# Test with the image path
detect_pieces("uploads/uploaded_0f662cb3-5823-4d2a-9960-f46bd98cf03f6847814347796807512.jpg")
