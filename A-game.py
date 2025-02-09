def count_guest_uniform_games(n, uniforms):
    count = 0
    
    for i in range(n):
        home_i = uniforms[i][0]  
        for j in range(n):
            if i != j: 
                guest_j = uniforms[j][1] 
                if home_i == guest_j:
                    count += 1

    return count
n = int(input().strip())
uniforms = [tuple(map(int, input().strip().split())) for _ in range(n)]
result = count_guest_uniform_games(n, uniforms)
print(result)
