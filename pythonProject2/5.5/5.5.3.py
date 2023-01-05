# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

sorted_data = sorted(data, key=lambda x: x[0] / (x[1]*100)**2)
print(sorted_data)

print(sorted(data, key=lambda x: x[0] / x[1]**2))



