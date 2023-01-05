# def pow_func(base, n=2):
#    print(base ** n)
#    return None
#
# print(pow_func(3))
# 9
# None

def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result

print(pow_func(3))
outside_result = pow_func(3)
print(outside_result)