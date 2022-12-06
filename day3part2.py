with open('day3.txt', 'r') as file:
    sacks = file.readlines()

total_sum = 0

for x in range(0, len(sacks), 3):
    badge = None
    item_1 = sacks[x]
    item_2 = sacks[x + 1]
    item_3 = sacks[x + 2]
    for letter_1 in item_1:
        for letter_2 in item_2:
            if (letter_2 == letter_1) & (letter_2 != '\n'):
                for letter_3 in item_3:
                    if (letter_3 == letter_2) & (letter_3 != '\n'):
                        badge = letter_3
    if badge.islower():
        total_sum += ord(badge) - 96
    else:
        total_sum += ord(badge) - 38

print(total_sum)
