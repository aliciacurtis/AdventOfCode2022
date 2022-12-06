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

# stack_1 = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']
# stack_2 = ['M', 'Q', 'H']
# stack_3 = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']
# stack_4 = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G']
# stack_5 = ['M', 'T', 'H', 'P']
# stack_6 = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']
# stack_7 = ['M', 'N', 'B', 'F', 'V', 'R']
# stack_8 = ['P', 'L', 'H', 'M', 'R', 'G', 'S']
# stack_9 = ['P', 'D', 'B', 'C', 'N']
list_of_stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

for stack in stacks:
    if stack[0] == 'm':
        num_to_move = int(stack[stack.find('e') + 2:stack.find('f') - 1])
        start_stack = int(stack[stack.find('om') + 3:stack.find('to') - 1])
        end_stack = int(stack[stack.find('to') + 3:stack.find('\n')])
        current_list = list_of_stacks[start_stack - 1]
        temp_list = []
        for num in range(len(current_list), len(current_list) - num_to_move, -1):
            temp_list.append(current_list[num - 1])
        for num in range(num_to_move):
            list_of_stacks[start_stack - 1].pop()
        for num in range(len(temp_list), len(temp_list) - num_to_move, -1):
            list_of_stacks[end_stack - 1].append(temp_list[num - 1])

print(stack_1)
print(stack_2)
print(stack_3)
print(stack_4)
print(stack_5)
print(stack_6)
print(stack_7)
print(stack_8)
print(stack_9)