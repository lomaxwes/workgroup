def adder(*nums):
    sum_ = 0
    for i in nums:
        sum_ += i
    return sum_

adder(1, 2, 3)