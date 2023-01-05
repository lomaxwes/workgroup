def main_func(name):
    def inner_func():
        print('Hello my friend', name)

    return inner_func