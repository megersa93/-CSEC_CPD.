n = int(input().strip())
s = input().strip()

removals = 0

for i in range(n - 1):
    if s[i] == s[i + 1]:  
        removals += 1

print(removals)
