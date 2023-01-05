
def counter(func):
    def wrap(*args,**kwargs):
        wrap.num_calls += 1
        result = func(*args,**kwargs)
        return result
    wrap.num_calls = 0
    return wrap

@counter
def greet():
    print("Hello")

for i in range(10):
    greet()

print(greet.num_calls)