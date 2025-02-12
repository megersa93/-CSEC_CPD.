one_row = -1
one_col = -1

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        value = row[j]
        if value == 1:
            one_row = i + 1
            one_col = j + 1

target_row = 3
target_col = 3
row_moves = abs(one_row - target_row)
col_moves = abs(one_col - target_col)

total_moves = row_moves + col_moves
print(total_moves)
