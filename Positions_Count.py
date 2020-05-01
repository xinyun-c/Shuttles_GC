import math

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))


if __name__ == '__main__':
    print("Enter dimensions of the game board to calculate number of positions")
    row = input("Enter your number of rows (including the starting rows): ")
    col = input("Enter your number of columns: ")
    piece = input("Enter your number of piece for each side (need to be smaller or equal to number of columns): ")
    shuttle_pos = input("Enter your different positions for each shuttle: ")
    try:
        row = int(row)
        col = int(col)
        piece = int(piece)
        shuttle_move = int(shuttle_pos)
    except:
        raise ValueError("Input invalid")

    if row <= 2 or col <= 4 or piece < 1 or piece > col or (col - piece) % 2 != 0:
        raise ValueError("Input invalid")

    shuttle_pos = shuttle_move ** (row - 2)

    piece_pos = col * (row - 2) + piece * 2
    piece_comb = nCr(piece_pos, piece * 2) * nCr(piece * 2, piece)

    num_pos = piece_comb * shuttle_pos
    print("Number of Positions:", num_pos)

    print("Board:")
    print("." * int(((col - piece) / 2)) + "O" * piece + "." * int(((col - piece) / 2)))
    for i in range(row - 2):
        if i == ((row - 2) - 1) / 2:
            shuttle_owner = "Neutral"
        elif i < ((row - 2) - 1) / 2 and i % 2 == 0:
            shuttle_owner = "O's shuttle"
        elif i > ((row - 2) - 1) / 2 and i % 2 == 1:
            shuttle_owner = "O's shuttle"
        elif i < ((row - 2) - 1) / 2 and i % 2 == 1:
            shuttle_owner = "X's shuttle"
        elif i > ((row - 2) - 1) / 2 and i % 2 == 0:
            shuttle_owner = "X's shuttle"
        print("." * col + " " + "(" + shuttle_owner + ")")
    print("." * int(((col - piece) / 2)) + "X" * piece + "." * int(((col - piece) / 2)))