# Balls are dropped from the opening of the board. Every time a ball hits a nail it has a 50% chance of falling to the left or to the right. The piles of balls
# are accumulated in the slots at the bottom of the board. 

# Write a program that simulates the bean machine. Your program should prompt the user to enter the number og balls and the number of slots in the machine. Simulate
# the falling of each ball by printing its path. 

# The output should look like this:   

# Enter the number of balls to drop: 5
# Enter the number of slots in the bean machine: 9
# LRLRLRR
# RRLLRLL

# Display the final buildup of the balls in the slots in a histogram. 
import random

number_of_balls = int(input("Enter the number of balls to drop: "))
number_of_slots = int(input("Enter the number of slots in the bean machine: "))
slots = [0] * number_of_slots
for i in range(number_of_balls):
    path = "" 
    for j in range(number_of_slots-1):
        if random.randint(0, 1) == 0:
            path += "L"
        else:
            path += "R"
    print(path)
    slots[path.count("R")] += 1 #

            

# def bean_machine():
#     balls = int(input("Enter the number of balls to drop: "))
#     slots = int(input("Enter the number of slots in the bean machine: "))
#     slots_list = [0] * slots
#     for i in range(balls):
#         path = ""
#         for j in range(slots-1):
#             if random.randint(0,1) == 0:
#                 path += "L"
#             else:
#                 path += "R"
#         print(path)
#         slots_list[path.count("R")] += 1
#     print(slots_list)
#     for i in range(max(slots_list), 0, -1):
#         for j in range(slots):
#             if slots_list[j] >= i:
#                 print("0", end = "")
#             else:
#                 print(" ", end = "")
#         print()
#     for i in range(slots):
#         print(i, end = "")
#     print()

# bean_machine()