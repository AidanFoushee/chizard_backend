# [Chizard Frontend](https://github.com/AidanFoushee/chizard_chess_app)
To start backend using FastAPI run: `uvicorn main:app --host 0.0.0.0 --port 8000` in the terminal

## TODO
- [x] Images can be sent to backend via POST
- [x] Images stored in uploads directory
- [ ] Create machine learning model to create a board position from an image that is compatible with Stockfish
- [ ] Integrate Stockfish and feed it data from machine learning model (evaluation bar, best moves, etc.)
- [ ] Send data from Stockfish back to frontend to be displayed on a digitized chess board (think chess.com)
