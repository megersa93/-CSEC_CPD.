def min_shovels(k, r):
    for n in range(1, 11):
        total_cost = n * k
        last_digit = total_cost % 10
        if last_digit == 0 or last_digit == r:
            return n
    return 10  
k, r = map(int, input().strip().split())

result = min_shovels(k, r)
print(result)
