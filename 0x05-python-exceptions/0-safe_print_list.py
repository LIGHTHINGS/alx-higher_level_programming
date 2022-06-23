#!/usr/bin/python3
# def safe_print_list(my_list=[], x=0):
#     count = 0

#     for i in range(x):
#         try:
#             print("{}".format(my_list[i]), end='')
#         except:
#             break
#         else:
#             count += 1

#     print()
#     return (count)
# my_list = [1, 2, 3, 4, 5,1,2,4,5,7,8]
# safe_print_list(my_list, 6)
# list= [1,2,3,4,5,6,7,8,9,10]
# for a in range(10):
#     print("{}".format(list[a]))
# total = 0
# prices = [10,20,30]
# for item in prices:
#     total += item
numbers = [2, 2, 2, 2, 6]
for i in numbers:
    print(f"X" * i)