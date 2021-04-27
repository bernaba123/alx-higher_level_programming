#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number) % 10
    print("{}".format(num), end="")
    return num

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
