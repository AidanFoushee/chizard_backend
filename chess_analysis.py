import chess
import chess.engine

# Path to the Stockfish executable (make sure to set this to your correct path)
 # Replace with your Stockfish path
#stockfish_path = "/Users/liamfoushee/desktop/ChessAIModel/stockfish"

stockfish_path = '/opt/homebrew/bin/stockfish'
engine = None  # Initialize the engine variable

# Initialize the chess engine
def init_engine():
    try:
        engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        return engine
    except Exception as e:
        print(f"Failed to start chess engine: {e}")
        return None

def analyze_fen(fen: str):
    engine = init_engine()
    if engine is None:
        raise RuntimeError("Chess engine is not running!")
    
    if engine.ping() is False:
        raise RuntimeError("NO GOOD!")

    board = chess.Board(fen)  # Create a chess board from the FEN string

    # Analyze the position
    info = engine.analyse(board, chess.engine.Limit(time=2.0))  # Limit to 2 seconds for analysis
    evaluation = info["score"].relative.score(mate_score=10000)  # Get the evaluation score

# Handle special cases for checkmate and stalemate
    if evaluation >= 10000:
        evaluation_str = "Checkmate in favor of White"
    elif evaluation <= -10000:
        evaluation_str = "Checkmate in favor of Black"
    elif evaluation == 0:
        evaluation_str = "Stalemate"
    else:
        evaluation_str = str(evaluation)  # Regular evaluation score
    
    best_move = engine.play(board, chess.engine.Limit(time=2.0))  # Get the best move for the position
    
    # Prepare the output
    result = {
        "evaluation": evaluation,
        "best_move": best_move.move.uci()  # Convert the move to UCI notation
    }
    
    return result

