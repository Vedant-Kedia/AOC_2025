file = open('day2/input.txt')

ranges = list(map(lambda s: s.split('-'), file.read().split(',')))
ranges[-1][-1] = ranges[-1][-1][:-1]        # Removing /n from end of line

res = 0

for l, r in ranges:      # Go through each range in list of ranges
    for i in range(int(l), int(r) + 1):     # Go through each ID in selected range
        si = str(i)
        if si[:len(si) // 2] == si[len(si) // 2:]:      # first and last half of id are same
            res += i

print(res)
