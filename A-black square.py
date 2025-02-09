a1, a2, a3, a4 = map(int, input().split())
s = input().strip()

calories = {
    '1': a1,
    '2': a2,
    '3': a3,
    '4': a4
}

total_calories = sum(calories[char] for char in s)
print(total_calories)
