def card_game(n, cards):
    sereja_score = 0
    dima_score = 0
    left = 0
    right = n - 1
    
    turn = 0  
    
    while left <= right:
        if cards[left] > cards[right]:
            picked_card = cards[left]
            left += 1
        else:
            picked_card = cards[right]
            right -= 1
        
        if turn == 0:  
            sereja_score += picked_card
        else:  
            dima_score += picked_card
        
        turn = 1 - turn
    
    return sereja_score, dima_score

n = int(input())
cards = list(map(int, input().split()))
sereja_points, dima_points = card_game(n, cards)
print(sereja_points, dima_points)
