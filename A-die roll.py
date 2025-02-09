from math import gcd

def calculate_probability(Y, W):
    M = max(Y, W)
    favorable_outcomes = 7 - M
    total_outcomes = 6
    
    if favorable_outcomes <= 0:
        return "0/1"
    
    if favorable_outcomes == total_outcomes:
        return "1/1"
    
    numerator = favorable_outcomes
    denominator = total_outcomes
    divisor = gcd(numerator, denominator)
    return f"{numerator // divisor}/{denominator // divisor}"

Y, W = map(int, input().strip().split())
result = calculate_probability(Y, W)
print(result)
