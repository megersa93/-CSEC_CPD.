n = int(input())
heights = list(map(int, input().split()))

heights.sort()

print(" ".join(map(str, heights)))
