from ultralytics import YOLO

def detect_pieces(img):
    model = YOLO("best.pt")  # Load trained model
    esults = model.predict(img, conf=0.5, save=True)  # Run inference and save output