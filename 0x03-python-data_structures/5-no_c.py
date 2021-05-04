#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            print("{}".format(my_string[i]), end="")
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
