with open('day2.txt', 'r') as file:
    matches = file.readlines()

score = 0
for match in matches:
    if match[2] == 'X':  # rock
        score += 1
        if match[0] == 'A':  # rock
            score += 3  # draw
        elif match[0] == 'C':  # scissors
            score += 6  # win
    elif match[2] == 'Y':  # paper
        score += 2
        if match[0] == 'A':  # rock
            score += 6  # win
        elif match[0] == 'B':  # paper
            score += 3  # draw
    elif match[2] == 'Z':  # scissors
        score += 3
        if match[0] == 'B':  # paper
            score += 6  # win
        elif match[0] == 'C':  # scissors
            score += 3  # draw


print(score)
