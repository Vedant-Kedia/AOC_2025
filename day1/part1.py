file = open('input.txt')

rotations = list(file.read().split('\n'))
rotations.pop()

dial_pos = 50
res = 0

for rotation in rotations:
    cnt = int(rotation[1:])
    if rotation.startswith("L"):
        dial_pos -= cnt
    else:
        dial_pos += cnt
    dial_pos %= 100
    if dial_pos == 0:
        res += 1

print(res)