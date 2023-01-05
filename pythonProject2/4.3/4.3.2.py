def multiplication(*nums):
    mult = 1
    for n in nums:
        mult *= n

    return mult

print(multiplication(1, 12, 3, 1, 1))