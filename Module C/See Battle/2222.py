


class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        self.__dict__.update(kwargs)

    def config(self, **kwargs):
        self.__dict__.update(kwargs)
        for key, val in kwargs.items():
            if key in self.__dict__:
                setattr(self, key, val)




label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

label.config(color='red', bd=100)

print(label.__dict__)