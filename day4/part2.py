file = open('day4/input.txt')

grid = list(map(list, file.read().split('\n')))
grid.pop()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

removals = 0

while True:
    res = 0
    new_grid = grid[:]
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
                    new_grid[i][j] = '.'
                    res += 1
    if res == 0:
        break
    removals += res
    grid = new_grid[:]


print(removals)
