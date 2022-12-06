with open('day5.txt', 'r') as file:
    stacks = file.readlines()

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []

for stack in stacks:
    if stack[0] == '[':
        if stack[1] != ' ':
            stack_1.append(stack[1])
        if stack[5] != ' ':
            stack_2.append(stack[5])
        if stack[9] != ' ':
            stack_3.append(stack[9])
        if stack[13] != ' ':
            stack_4.append(stack[13])
        if stack[17] != ' ':
            stack_5.append(stack[17])
        if stack[21] != ' ':
            stack_6.append(stack[21])
        if stack[25] != ' ':
            stack_7.append(stack[25])
        if stack[29] != ' ':
            stack_8.append(stack[29])
        if stack[33] != ' ':
            stack_9.append(stack[33])

stack_1.reverse()
stack_2.reverse()
stack_3.reverse()
stack_4.reverse()
stack_5.reverse()
stack_6.reverse()
stack_7.reverse()
stack_8.reverse()
stack_9.reverse()

list_of_stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

for stack in stacks:
    if stack[0] == 'm':
        num_to_move = int(stack[stack.find('e') + 2:stack.find('f') - 1])
        start_stack = int(stack[stack.find('om') + 3:stack.find('to') - 1])
        end_stack = int(stack[stack.find('to') + 3:stack.find('\n')])
        for num in range(num_to_move):
            moved_stack = list_of_stacks[start_stack - 1].pop()
            list_of_stacks[end_stack - 1].append(moved_stack)

print(stack_1[len(stack_1) - 1] + stack_2[len(stack_2) - 1] + stack_3[len(stack_3) - 1]
      + stack_4[len(stack_4) - 1] + stack_5[len(stack_5) - 1] + stack_6[len(stack_6) - 1]
      + stack_7[len(stack_7) - 1] + stack_8[len(stack_8) - 1] + stack_9[len(stack_9) - 1])
