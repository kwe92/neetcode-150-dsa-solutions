import collections  # Easy way to create collections without if else statements e.g. a dict key doesnt have a value there is no need to check that


def isValidSudoku(board: list[list[str]]) -> bool:
    row = collections.defaultdict(set)
    column = collections.defaultdict(set)
    blocks = collections.defaultdict(set)
    # 9 rows, 9 columns, 9 elements (squares) in each row and column
    length = len(board)

    for r in range(length):
        for c in range(length):
            current_square = board[r][c]
            current_block_coord = (r//3, c//3)
            if current_square == ".":  # "." represents empty square
                continue  # skp empty square
            if current_square in row[r] \
                    or current_square in column[c]\
                    or current_square in blocks[current_block_coord]:
                return False
            else:
                row[r].add(current_square)
                column[c].add(current_square)
                blocks[current_block_coord].add(current_square)
    return True


if __name__ == '__main__':
    # board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
    #          ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    #          [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    #          ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    #          [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    #          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", ".", ".", ".", ".", ".", "2", ".", "."],
    #          [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # False

    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # True

print('is valid:', isValidSudoku(board))

# Output: false
