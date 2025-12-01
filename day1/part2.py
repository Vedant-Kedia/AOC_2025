file = open('day1/input.txt')

rotations = list(file.read().split('\n'))
rotations.pop()

res = 0
dial = 50

for rotation in rotations:
    cnt = int(rotation[1:])
    if rotation.startswith("L"):
        for _ in range(cnt):
            if dial == 0:
                dial = 100
            dial -= 1
            if dial == 0:
                res += 1
            
    else:
        for _ in range(cnt):
            if dial == 99:
                dial = -1
            dial += 1
            if dial == 0:
                res += 1

print(res)