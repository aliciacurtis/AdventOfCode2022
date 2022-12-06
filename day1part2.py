with open("adventofcodeday1.txt", "r") as my_file:
    running_sum = 0
    highest_sum_1 = 0
    highest_sum_2 = 0
    highest_sum_3 = 0
    for line in my_file:
        if line == '\n':
            if (running_sum > highest_sum_1) & (running_sum > highest_sum_2) \
                    & (running_sum > highest_sum_3):
                highest_sum_3 = highest_sum_2
                highest_sum_2 = highest_sum_1
                highest_sum_1 = running_sum
            elif (running_sum > highest_sum_2) & (running_sum > highest_sum_3):
                highest_sum_3 = highest_sum_2
                highest_sum_2 = running_sum
            elif running_sum > highest_sum_3:
                highest_sum_3 = running_sum
            running_sum = 0
        else:
            running_sum += int(line)
    print(highest_sum_1 + highest_sum_2 + highest_sum_3)
