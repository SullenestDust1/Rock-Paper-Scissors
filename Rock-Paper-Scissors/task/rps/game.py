# Write your code here
from random import choice
from collections import deque


def list_to_dic(lst):
    dic = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return dic


def check_half(lst, x):
    if x in lst[:len(lst)//2]:
        return 1
    else:
        return 0


def game(user_input, options):
    global score
    if user_input == "!rating":
        print(f"Your rating: {score}")
    elif user_input != "!exit":
        if user_input in options:
            pc_choice = choice(options)
            if user_input == pc_choice:
                score += 50
                print(f"There is a draw ({pc_choice})")
            else:
                user_index = options.index(user_input)
                middle = len(options)//2
                if user_index != middle:
                    if user_index > middle:
                        rotations = user_index - middle
                    else:
                        rotations = middle - user_index
                    options = deque(options)
                    options.rotate(rotations)
                    options = list(options)
                if check_half(options, pc_choice):
                    score += 100
                    print(f"Well done. Computer chose {pc_choice} and failed")
                else:
                    print(f"Sorry, but computer chose {pc_choice}")
        else:
            print("Invalid input")


user_in = input("Enter your name: ")
print(f"Hello, {user_in}")
score = 0
file = open("rating.txt", "r")
ratings = file.readlines()
names = []

for line in ratings:
    names.append(line.replace("\n", "").split(sep=" "))
file.close()
names = list_to_dic(sum(names, []))

if user_in in names:
    score = names[user_in]

user_in = input()
if not user_in:
    opt = ["scissors", "rock", "paper"]
else:
    opt = [user_in.split(sep=",")]
print("Okay, let's start")
user_in = input()
while user_in != "!exit":
    game(user_in, opt)
    user_in = input()

print("Bye!")
