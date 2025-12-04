file = open('day4/input.txt')

grid = file.read().split('\n')
grid.pop()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

res = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            available = []
            adj_cnt = 0
            for dl, dr in directions:
                l, r = i + dl, j + dr
                if 0 <= l < len(grid) and 0 <= r < len(grid[i]) and grid[l][r] == '@':
                    adj_cnt += 1
            
            if adj_cnt < 4:
                res += 1

print(res)
