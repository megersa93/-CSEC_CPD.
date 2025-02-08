word = input().strip()

uppercase_count = sum(1 for c in word if c.isupper())
lowercase_count = len(word) - uppercase_count  uppercase count

if uppercase_count > lowercase_count:
    print(word.upper())
else:
    print(word.lower())
