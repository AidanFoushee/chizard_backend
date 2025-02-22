import chess
import chess.engine

# Set the path to your Stockfish executable
stockfish_path = '/opt/homebrew/bin/stockfish'

# Initialize the engine
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

import random

import random

# def generate_random_fen():
#     # Define piece types and possible placements for each side
#     pieces = ['K', 'Q', 'R', 'B', 'N', 'P']
#     black_pieces = [piece.lower() for piece in pieces]  # Lowercase for black pieces
    
#     # Initialize empty 8x8 board
#     board = [[' ' for _ in range(8)] for _ in range(8)]
    
#     # Randomly place pieces for white and black on the board
#     for row in range(8):
#         for col in range(8):
#             if random.random() < 0.1:  # Random chance to place a piece (10% chance per square)
#                 if random.random() < 0.5:
#                     piece = random.choice(pieces)  # White piece
#                 else:
#                     piece = random.choice(black_pieces)  # Black piece
#                 board[row][col] = piece

#     # Convert the board into FEN format (with piece placement and empty squares)
#     fen_rows = []
#     for row in board:
#         empty_count = 0
#         fen_row = ''
#         for square in row:
#             if square == ' ':
#                 empty_count += 1
#             else:
#                 if empty_count > 0:
#                     fen_row += str(empty_count)
#                     empty_count = 0
#                 fen_row += square
#         if empty_count > 0:
#             fen_row += str(empty_count)
#         fen_rows.append(fen_row)
    
#     # Generate the FEN string from the rows
#     fen = '/'.join(fen_rows)
    
#     # Randomly set castling rights
#     castling_rights = random.choice(['KQkq', 'KQ', 'kq', 'K', 'Q', 'k', 'q', '-'])
    
#     # Randomly set en passant (usually not applicable)
#     en_passant = random.choice(['-', 'a3', 'h6', 'e3', 'd6', '-'])
    
#     # Random halfmove clock (between 0 and 50)
#     halfmove_clock = random.randint(0, 50)
    
#     # Random fullmove number (between 1 and 100)
#     fullmove_number = random.randint(1, 100)
    
#     # Randomly set the side to move (either 'w' for white or 'b' for black)
#     side_to_move = random.choice(['w', 'b'])

#     # Construct the full FEN string
#     random_fen = f"{fen} {side_to_move} {castling_rights} {en_passant} {halfmove_clock} {fullmove_number}"
    
#     return random_fen

# # Example usage
# random_fen = generate_random_fen()
# print(random_fen)

# FEN string for the chess position
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"  # example FEN

# Create a chess board from the FEN
board = chess.Board(fen)
#print('1')
# Set the analysis parameters
info = engine.analyse(board, chess.engine.Limit(time=2.0))  # Limit analysis to 2 seconds
#print('2')
# Get the evaluation result (e.g., the evaluation of the position from Stockfish)
evaluation = info["score"]
print(f"Evaluation: {evaluation}")

# retrieve the best move from the analysis
best_move = info["pv"][0]
print(f"Best move: {best_move}")

if board.turn == chess.BLACK:
    board = board.transform(chess.flip_vertical)
print(board)

# Close the engine when done
engine.quit()
