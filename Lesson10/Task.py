# import os
#
# while True:
#     current_dir = os.getcwd()
#     command = input(current_dir + "$ ").split()
#     match command[0]:
#         case "cd":
#             os.chdir(command[1])
#         case "cat":
#             with open(command[1]) as file:
#                 print(file.read())
#         case "mkdir":
#             os.mkdir(command[1])
#         case "touch":
#             open(command[1], "w").close()
import os
from pathlib import Path

print(Path("/home/shawn/PycharmProjects/Py_14/Lesson10").parent)
print(len(os.listdir()))
