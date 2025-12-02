file = open('day2/input.txt')

ranges = list(map(lambda s: s.split('-'), file.read().split(',')))
ranges[-1][-1] = ranges[-1][-1][:-1]        # Removing /n from end of line

res = 0

for l, r in ranges:     # Go through each range in list of ranges
    for i in range(int(l), int(r) + 1):     # Go through each ID in selected range
        si = str(i)
        for j in range(1, (len(si) // 2) + 1):      # Check each combination for repeated sequences
            prev = si[:j]
            idx = j
            while idx < len(si):
                curr = si[idx:idx + j]
                if prev != curr:
                    break       # if not repeated we skip
                prev = curr
                idx += j
            else:
                res += i
                break       # we skip the remaining combinations if we find one repeated sequence

print(res)
