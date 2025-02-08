n = int(input().strip())
previous_magnet = input().strip()
groups = 1  
for _ in range(1, n):
    current_magnet = input().strip()
    if current_magnet != previous_magnet:
        groups += 1
    previous_magnet = current_magnet  
print(groups)
