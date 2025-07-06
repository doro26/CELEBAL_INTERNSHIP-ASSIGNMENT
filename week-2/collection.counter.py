from collections import Counter

x = int(input())
sizes = list(map(int, input().split()))
shoe_inventory = Counter(sizes)

n = int(input())
earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        earnings += price
        shoe_inventory[size] -= 1

print(earnings)
