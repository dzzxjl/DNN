import os
import re
import sys
# print(sys.path[0])
path = "/Users/dzzxjl/PycharmProjects/tianchi/script/input/"
files_name_list = os.listdir(path)


output = {}

for file_name in files_name_list:
    # print(file_name)
    file_index = re.match('cluster_(.*)',file_name.split(".")[0]).group(1)
    # print(file_index)

    list = []

    with open(path + file_name) as file:
        j = 0
        for line in file.readlines():
            if j < 4:
                pass
            else:
                str = line.split(" ")[0]
                match = re.match('ID=(.*)', str)
                # print(str)
                temp = match.group(1)
                # print(script)
                list.append(temp)
            j = j + 1
        # print(list)
    output[file_index] = list

print(output)


