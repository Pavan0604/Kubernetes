my_arr = [1,2,3]
# my_arr[0:1] = []
# print(my_arr)

# for i in range(0, len(my_arr), 1):
#     print(my_arr[i])

# with open("demo.txt", "w") as file:
#     file.write("My comment")

# with open("demo.txt", "r") as file:
#     lines = file.readlines()
#     print(lines[10])


# with open("demo.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
#     for line in reversed(lines):
#         print(line)


# import random

# with open("demo.txt", "r") as file:
#     lines = file.readlines()  # read all lines into a list
#     print(random.choice(lines).strip())

# with open("demo.txt", "r") as file:
#     text = file.read()
#     words = text.split()
#     print("Number of words:", len(words))

import os 
import re

# print(os.getcwd())
        

# import subprocess

# result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# print(result.stdout)
# print(result.stderr)

# text = "Hello World"
# pattern = r"Hello"

# if re.match(pattern, text):
#     print("Match found!")


def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        permute(rest, answer+ch)

permute("abc")

