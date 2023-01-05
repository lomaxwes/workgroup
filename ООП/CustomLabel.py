class CustomLabel:
    def __init__(self, text='', **kwargs):
        self.text = text
        self.__dict__.update(kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            self.key = value


