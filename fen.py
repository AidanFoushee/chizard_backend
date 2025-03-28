def generate_fen(board_dict):
    """
    Generates a FEN string from detected piece positions.
    """
    piece_map = {
        "pawn": "P", "knight": "N", "bishop": "B", 
        "rook": "R", "queen": "Q", "king": "K"
    }

    # Create empty board
    board = [["" for _ in range(8)] for _ in range(8)]

    for square, piece in board_dict.items():
        col = ord(square[0]) - ord('a')
        row = 8 - int(square[1])  

        board[row][col] = piece_map.get(piece.lower(), "?")  

    fen_rows = []
    for row in board:
        empty_count = 0
        row_fen = ""
        for cell in row:
            if cell == "":
                empty_count += 1
            else:
                if empty_count > 0:
                    row_fen += str(empty_count)
                    empty_count = 0
                row_fen += cell
        if empty_count > 0:
            row_fen += str(empty_count)
        fen_rows.append(row_fen)

    return "/".join(fen_rows) + " w - - 0 1"
