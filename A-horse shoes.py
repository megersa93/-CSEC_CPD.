def min_horseshoes_needed(colors):
    unique_colors = set(colors)  
    unique_count = len(unique_colors) 
    return 4 - unique_count 

s1, s2, s3, s4 = map(int, input().strip().split())

result = min_horseshoes_needed([s1, s2, s3, s4])

print(result)
