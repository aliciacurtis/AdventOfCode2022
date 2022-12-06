with open("adventofcodeday1.txt", "r") as my_file:
    running_sum = 0
    highest_sum = 0
    for line in my_file:
        if line == '\n':
            if running_sum > highest_sum:
                highest_sum = running_sum
            running_sum = 0
        else:
            running_sum += int(line)
    print(highest_sum)
