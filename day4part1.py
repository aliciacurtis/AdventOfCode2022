with open('day4.txt', 'r') as file:
    sections = file.readlines()

pair_contain = 0

for section in sections:
    elf1_range_left = int(section[:section.find('-')])
    elf1_range_right = int(section[section.find('-') + 1:section.find(',')])
    elf2_range_left = int(section[section.find(',') + 1:section.rfind('-')])
    elf2_range_right = int(section[section.rfind('-') + 1:section.find('\n')])
    if (elf1_range_left <= elf2_range_left) & (elf1_range_right >= elf2_range_right):
        pair_contain += 1
    elif (elf2_range_left <= elf1_range_left) & (elf2_range_right >= elf1_range_right):
        pair_contain += 1

print(pair_contain)
