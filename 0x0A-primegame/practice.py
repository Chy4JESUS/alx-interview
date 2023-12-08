#!/usr/bin/python3
""" Module for Prime Game """


def prime(n):
    prime_numbers = []
    for i in range(2, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers


def numbers_list(num):
    numbers = []
    for i in range(num + 1):
        numbers.append(i)
    return numbers


def multiple(selected, nums):
    multiple_list = []
    for i in range(nums + 1):
        mul = selected * i
        if mul <= nums:
            multiple_list.append(mul)
    return multiple_list


def removal(mul_list, num_list):
    new_numbers = []
    for i in num_list:
        if i not in mul_list:
            new_numbers.append(i)
    return new_numbers


def isWinner(x, nums, play_times=0):
    if not nums or x < 1:
        return None

    num = nums[0]

    num_list = numbers_list(num)
    prime_nums = prime(num)
    temp = prime_nums[0]
    mul_list = multiple(temp, num)

    if temp in prime_nums:
        prime_nums.remove(temp)

    result = removal(mul_list, num_list)

    x = x - 1
    play_times = play_times + 1

    if len(result) > 1 and x > 0:
        return isWinner(x, nums, play_times)
    else:
        if play_times % 2 == 0:
            return "Maria"
        else:
            return "Ben"
