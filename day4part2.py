with open('day4.txt', 'r') as file:
    sections = file.readlines()

pair_overlap = 0

for section in sections:
    a = int(section[:section.find('-')])  # a
    b = int(section[section.find('-') + 1:section.find(',')])  # b
    c = int(section[section.find(',') + 1:section.rfind('-')])  # c
    d = int(section[section.rfind('-') + 1:section.find('\n')])  # d
    if ((c >= a or d >= b) and (b >= d or a >= c)) or (a <= c <= b <= d):
        print(section)
        pair_overlap += 1
    elif ((a >= c or b >= d) and (d >= b or c >= a)) or (c <= a <= d <= b):
        print(section)
        pair_overlap += 1


print(pair_overlap)
