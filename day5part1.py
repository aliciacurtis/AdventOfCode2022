with open('day5.txt', 'r') as file:
    stacks = file.readlines()

list_of_stacks = [[], [], [], [], [], [], [], [], []]

for stack in stacks:
    num = 0
    list_no = 0
    while stack[num] == '[':
        for x in range(1, len(stack), 4):
            if stack[x] != ' ':
                list_of_stacks[list_no].append(stack[x])
            list_no += 1
        list_no = 0
        num += 1

for num in range(len(list_of_stacks)):
    list_of_stacks[num].reverse()

for stack in stacks:
    if stack[0] == 'm':
        num_to_move = int(stack[stack.find('e') + 2:stack.find('f') - 1])
        start_stack = int(stack[stack.find('om') + 3:stack.find('to') - 1])
        end_stack = int(stack[stack.find('to') + 3:stack.find('\n')])
        for num in range(num_to_move):
            moved_stack = list_of_stacks[start_stack - 1].pop()
            list_of_stacks[end_stack - 1].append(moved_stack)

for x in range(len(list_of_stacks)):
    print(list_of_stacks[x][-1])
