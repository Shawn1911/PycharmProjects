import os

print(os.getcwd()) #terminal: pwd
#os.mkdir("test") #terminal: mkdir
print(os.listdir()) #terminal: ls or dir
os.chdir("../") #terminal: cd
print(os.getcwd())
os.chdir("Lesson10")
print((os.getcwd()))
# os.remove("temp.py") #terminal: rm
os.open("os_.py" , 2) #terminal: nano