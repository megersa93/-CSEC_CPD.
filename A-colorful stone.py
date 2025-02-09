def final_position(s, t):
    position = 0 
    
    for instruction in t:
        if position < len(s) and s[position] == instruction[0]:  
            position += 1 
            
    return position + 1
s = input().strip()
t = input().strip()

result = final_position(s, t)
print(result)
