class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        b = ''
        for i in value:
            if i == '@' or i == '.':
                b += i
        if b != '@.':
            print(f"ErrorMail:{value}")
        else:
            self.__email = value

    email = property(fget=get_email, fset=set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'

print(k.email)  # prince@still.wait