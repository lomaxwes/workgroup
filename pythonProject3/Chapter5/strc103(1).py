current_users = ['olya', 'ema', 'petya', 'admin', 'tupic', 'Egor', 'sasha']
current_users_lower = list(map(str.lower,current_users))
new_users = ['lexa', 'vova', 'Ema', 'egor', 'lolita']
new_users_lower = list(map(str.lower,new_users))

for user in new_users_lower:
    if user in current_users_lower:
        print(f" Имя {user} уже занято!")
    else:
        print(f" Имя {user} доступно!")