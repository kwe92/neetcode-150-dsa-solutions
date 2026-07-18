import collections


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    blocks = collections.defaultdict(set)
    length = len(board)

    for r in range(length):
        for c in range(length):
            current_square = board[r][c]
            if current_square == ".":
                continue
            current_block_id = (r // 3, c // 3)  # Coordinate Hashing
            if current_square in rows[r] \
                    or current_square in columns[c] \
                    or current_square in blocks[current_block_id]:
                return False
            #  State Tracking
            rows[r].add(current_square)
            columns[c].add(current_square)
            blocks[current_block_id].add(current_square)
    return True


if __name__ == '__main__':

    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "1", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print("result:", isValidSudoku(board))

    # Output: false
