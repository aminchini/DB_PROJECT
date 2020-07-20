# f = open("test.txt", "w")
# for i in range (100):
#     f.write(str(i)+" kooon! I have deleted the content!\n")
# f.close()

# f = open("test.txt", "r")
# for i, line in enumerate(f):
#     if i == 25:
#         print(line[:len(line)-2:])
#     elif i == 29:
#         print(line[:len(line)-2:])
# f.close()
import json 

import fileinput
import sys
# for i, line in enumerate(fileinput.input("test.txt", inplace=1)):
#     if i == 50:
#         temp = line
#         line = line.replace("kooon", str(i)+' ')
#     sys.stdout.write(line)

# curr_film = open("test.txt", "r")
# current_line = 0
# for i in curr_film:
#     current_line += 1
# curr_film.close
# print(current_line)

# i = '0 1234'
# s_index = i.find(' ')
# e_index = i.find('/')
# print(i[s_index+1:e_index:])
# x = i.split('/')
# print(x)
# x = {}
# x[0] = "hdskjfhn"
# print(x[1])

# l = 'sdflsjk lfjsdlfj ,m dlfsldfjdl'
# b = l.split()[1]
# print(b)

# old_val = "123"
# value = "321"
# num = ''
# for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
#     if old_val in line:
#         s_in = line.find(" ")
#         num = line[:s_in:]
#         old_fields = line[s_in::]
#         ls = old_fields.split('/')
#         old_films = ls[3]
#         if(old_val in old_films):
#             temp = old_films
#             new_films = temp.replace(old_val, value)
#             ls[3] = new_films
#             line = num + '/'.join(ls)
# print(len(num))
#     sys.stdout.write(line)

# l = "123/Shahab Hosseini/46/The Salesman,A Separation,123"
# ls = l.find('/')
# r = l[ls::]
# print(r)
import ast 

f = open("temp_artist.txt", "r")

json_acceptable_string = f.readline().replace("'", "\"")
d = json.loads(json_acceptable_string)
print(type(d))

f.close()

