alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  # ошибка, тк ключ отсутствует

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

people_data = {}
people_data['first name'] = 'andre'
people_data['second name'] = 'grigorev'
people_data['city'] = 'ekat'
people_data['years'] = 41
print(people_data)
print(people_data['years'])


