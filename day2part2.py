with open('day2.txt', 'r') as file:
    matches = file.readlines()

score = 0
for match in matches:
    if match[0] == 'A':  # rock
        if match[2] == 'Y':  # draw
            score += 4  # rock 1 + draw 3
        elif match[2] == 'X':  # lose
            score += 3  # scissors 3
        elif match[2] == 'Z':  # win
            score += 8  # paper 2 + win 6
    if match[0] == 'B':  # paper
        if match[2] == 'Y':  # draw
            score += 5  # paper 2 + draw 3
        if match[2] == 'X':  # lose
            score += 1  # rock 1
        if match[2] == 'Z':  # win
            score += 9  # scissors 3 + win 6
    if match[0] == 'C':  # scissors
        if match[2] == 'Y':  # draw
            score += 6  # scissors 3 + draw 3
        if match[2] == 'X':  # lose
            score += 2  # paper 2
        if match[2] == 'Z':  # win
            score += 7  # rock 1 + win 6

print(score)
