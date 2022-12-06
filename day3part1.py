with open('day3.txt', 'r') as file:
    sacks = file.readlines()

total_sum = 0

for items in sacks:
    item_both = None
    half_size = int((len(items) - 1) / 2)
    first_half = items[:half_size]
    second_half = items[half_size:]
    for letter_1 in first_half:
        for letter_2 in second_half:
            if letter_2 == letter_1:
                item_both = letter_2
    if item_both.islower():
        total_sum += ord(item_both) - 96
    else:
        total_sum += ord(item_both) - 38

print(total_sum)
