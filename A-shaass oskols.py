def count_birds_after_shots(n, birds, m, shots):
    for x, y in shots:
        wire_index = x - 1
        bird_position = y - 1
        birds_up = bird_position  
        birds_down = birds[wire_index] - (bird_position + 1)  
        
        if wire_index > 0:
            birds[wire_index - 1] += birds_up
        if wire_index < n - 1:
            birds[wire_index + 1] += birds_down
        
        birds[wire_index] = 0  
    
    return birds
n = int(input().strip())
birds = list(map(int, input().strip().split()))
m = int(input().strip())
shots = [tuple(map(int, input().strip().split())) for _ in range(m)]

result = count_birds_after_shots(n, birds, m, shots)
for count in result:
    print(count)
