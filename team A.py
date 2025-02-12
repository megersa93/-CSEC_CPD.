n = int(input())
count = 0

for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    sure_count = petya + vasya + tonya

    if sure_count >= 2:
        count += 1

print(count)
