from ultralytics import YOLO

def detect_pieces(img):
    # Load the trained model
    model = YOLO("best.pt")

    # Run inference
    results = model.predict(img, conf=0.5, save=True)

    # Initialize an empty list to store detected pieces
    piece_positions = []

    # Iterate through the results
    for result in results:
        # Extract bounding boxes, class labels, and class names
        for box in result.boxes:
            # Get the bounding box coordinates (center and size)
            x, y, w, h = box.xywh.numpy()[0]  # These are center x, center y, width, height

            # Convert to top-left and bottom-right if needed (for better accuracy)
            x1 = x - w / 2  # top-left x
            y1 = y - h / 2  # top-left y
            x2 = x + w / 2  # bottom-right x
            y2 = y + h / 2  # bottom-right y

            # Get the class label
            label = result.names[int(box.cls)]  # Class name based on the index

            # Append the coordinates and label
            piece_positions.append((x1, y1, x2, y2, label))

    return piece_positions
