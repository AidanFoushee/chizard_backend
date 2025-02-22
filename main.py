from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import shutil
import os
import utils

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload directory exists

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    # Get the local ip of your computer
    # ip = utils.get_local_ip()
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ip = utils.get_ip() 
    return {"filename": file.filename, "url": f"{ip}{file.filename}"}


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



from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")
