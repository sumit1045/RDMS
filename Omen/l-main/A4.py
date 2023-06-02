def is_safe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:
            return False

    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def n_queen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if is_safe(arr, x, col, n):
            arr[x][col] = 1
            if n_queen(arr, x + 1, n):
                return True
            arr[x][col] = 0

    return False


n = int(input("Enter the value of n: "))
arr = [[0] * n for _ in range(n)]

if n_queen(arr, 0, n):
    for row in arr:
        print(' '.join(map(str, row)))
else:
    print("No solution exists.")
