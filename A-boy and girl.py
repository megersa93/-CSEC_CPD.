username = input().strip()
distinct_characters = set(username)
count_distinct = len(distinct_characters)
if count_distinct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
