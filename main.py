from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import shutil
import os
import utils
import board_detection
import piece_detection
import map_pieces
import fen
import cv2
from chess_analysis import analyze_fen

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload directory exists

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    print(f"📸 Received image: {file.filename}")
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("✅ Image saved successfully!")

    # grid = board_detection.detect_board_grid(file_path)
    # grid = board_detection.detect_board_grid(file_path)
    # if grid is None:
    #     return {"error": "Failed to detect the chessboard grid. Please try another image."}
    # else:
    #     print("🛠 Detected Board Grid:", grid)
   
    pieces = piece_detection.detect_pieces(file_path)
    print("🛠 Detected Pieces:", pieces)
    
    # mapped_pieces = map_pieces.map_pieces_to_squares(pieces)
    # print("🛠 Mapped Pieces:", mapped_pieces)
    
    # fen_code = fen.generate_fen(mapped_pieces)
    # print("♟ Generated FEN:", fen_code)

    ip = utils.get_ip() 
    return {"filename": file.filename, "url": f"{ip}{file.filename}"}

# New endpoint to analyze FEN
class FENRequest(BaseModel):
    fen: str

@app.post("/analyze_fen")
async def analyze_fen_endpoint(fen_request: FENRequest):
    fen = fen_request.fen
    print(f"♟ Received FEN: {fen}")
    
    # Use the analyze_fen function to get the evaluation and best move
    analysis_result = analyze_fen(fen)
    print("♟ Analysis Result:", analysis_result)

    return {"evaluation": analysis_result["evaluation"], "best_move": analysis_result["best_move"]}

@app.get("/", response_class=HTMLResponse)
async def home():
    files = os.listdir(UPLOAD_FOLDER)

    # Generate an HTML page with image previews
    image_tags = "".join(
        f"""
        <div class="image-card">
            <img src="/uploads/{file}" alt="{file}" />
            <p class="filename">{file}</p>
        </div>
        """
        for file in files
    )

    return f"""
    <html>
        <head>
            <title>Uploaded Images</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .image-container {{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                    margin-top: 20px;
                }}
                .image-card {{
                    background: white;
                    border: 2px solid #ddd;
                    border-radius: 8px;
                    padding: 15px;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 320px;
                }}
                img {{
                    border-radius: 4px;
                    width: 100%;
                    max-width: 300px;
                    height: auto;
                    display: block;
                    margin: 0 auto;
                }}
                .filename {{
                    margin-top: 10px;
                    font-weight: bold;
                    color: #333;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <h2>Uploaded Images</h2>
            <div class="image-container">
                {image_tags}
            </div>
        </body>
    </html>
    """
# Serve static files (uploaded images)
from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")
