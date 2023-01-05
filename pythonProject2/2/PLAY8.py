A = [1, 6, 3, 4, 5, 2, 7]

# мой вариант
second_min = A.index(min(A)+1)
third_min = A.index(min(A)+2)
print(A[second_min], A[third_min])

# второй вариант
first_min = A.pop(A.index(min(A)))
second_min = A.pop(A.index(min(A)))
third_min = A.pop(A.index(min(A)))
print(second_min, third_min)

# третий вариант
A1 = [1, 6, 3, 4, 5, 2, 7]
A1.sort()
print(A1[1], A1[2])