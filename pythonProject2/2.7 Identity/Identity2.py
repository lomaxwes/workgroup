L = ['Hello', 'world']
M = L

print(M is L)

M.append('!')


print(L)
# ['Hello', 'world', '!']
print(M is L)
M = L.copy()

print(M is L)