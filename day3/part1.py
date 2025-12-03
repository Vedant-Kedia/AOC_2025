file = open("day3/input.txt")

ratings = file.read().split('\n')
ratings.pop()

res = 0

for bank in ratings:
    battery1 = 0
    battery2 = 0
    battery_swapped = False
    for idx, str_battery in enumerate(bank):
        battery = int(str_battery)
        if battery2 > battery1:
            battery1 = battery2
            battery2 = 0
            battery_swapped = True
        if battery > battery1:
            if battery_swapped:
                battery2 = battery1
                battery_swapped = False
                battery1 = battery
                continue
            elif idx <= len(bank) - 2:
                battery1 = battery
                battery2 = 0
                continue
        if battery > battery2:
            battery2 = battery
    res += battery1 * 10 + battery2

print(res)