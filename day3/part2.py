file = open("day3/input.txt")

ratings = file.read().split('\n')
ratings.pop()

res = 0
n = 12      # The number of batteries that need to be turned on for each bank

for bank in ratings:
    stack = []
    for idx, str_battery in enumerate(bank):
        battery = int(str_battery)
        while stack and stack[-1] < battery and n - len(bank) + idx < len(stack):
            stack.pop()
        if len(stack) < n:
            stack.append(battery)
        
    res += int(''.join(map(str, stack)))

print(res)
