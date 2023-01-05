def reverse_(s1):
    if len(s1) == 0:
       return s1
    return reverse_(s1[1:]) + s1[0]

print(reverse_("12345"))