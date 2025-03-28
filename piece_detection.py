from ultralytics import YOLO

def detect_pieces(img):
    model = YOLO("best.pt")  # Load trained model
    results = model.predict(img, conf=0.5, save=True)  # Run inference and save output

    # Extract detected pieces
    piece_positions = []
    for r in results:
        for box in r.boxes:
            x, y, w, h = box.xywh.numpy()[0]
            label = r.names[int(box.cls)]
            piece_positions.append((x, y, label))

    return piece_positions