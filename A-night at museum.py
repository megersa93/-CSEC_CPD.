def min_rotations_to_print(s):
    current_char = 'a'  
    total_rotations = 0
    
    for target_char in s:
    
        current_index = ord(current_char) - ord('a')
        target_index = ord(target_char) - ord('a')

        clockwise_distance = (target_index - current_index) % 26
        counterclockwise_distance = (current_index - target_index) % 26
        
     
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        
        current_char = target_char
    
    return total_rotations

exhibit_name = input().strip()

result = min_rotations_to_print(exhibit_name)
print(result)
