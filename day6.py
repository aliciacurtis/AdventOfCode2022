with open('day6.txt', 'r') as file:
    stream = file.readlines()

stream_list = []

for letter in stream[0]:
    stream_list.append(letter)

for num in range(3, len(stream_list) - 1):
    if (stream_list[num] != stream_list[num - 1]) & (stream_list[num] != stream_list[num - 2]) & \
            (stream_list[num] != stream_list[num - 3]) & (stream_list[num - 1] != stream_list[num - 2]) & \
            (stream_list[num - 1] != stream_list[num - 3]) & \
            (stream_list[num - 2] != stream_list[num - 3]):
        print('Part 1: ' + str(num + 1))
        break

match = False

for num in range(len(stream_list) - 15):
    for numb in range(14):
        for number in range(1, 14 - numb):
            if stream_list[num + numb] == stream_list[num + numb + number]:
                match = True
    if match:
        match = False
    else:
        print('Part 2: ' + str(num + 14))
