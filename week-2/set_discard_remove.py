n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    parts = input().split()
    if parts[0] == 'pop':
        s.pop()
    elif parts[0] == 'remove':
        try:
            s.remove(int(parts[1]))
        except:
            pass
    elif parts[0] == 'discard':
        s.discard(int(parts[1]))

print(sum(s))
