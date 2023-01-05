# 3.9. Количество гостей: в одной из программ из упражнений с 3.4 по 3.7
# используйте len() для вывода сообщения с количеством людей, приглашенных на обед.
# 3.10. Все функции: придумайте информацию, которую можно было бы хранить в списке.
# Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно.
# Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
#упоминавшуюся в этой главе, хотя бы один раз.

names = ['grisha', 'oleg', 'petya', 'dima', 'alesha']
dear_guest = ['Newton', 'Arnold', 'Enshtein']
print(f"Будет {len(names) + len(dear_guest)} гостей!" )

all_list = ['grisha', 'oleg', 'petya', 'dima', 'alesha', 'Newton', 'Arnold', 'Enshtein',
            'honda', 'yamaha', 'suzuki', 'ducati', 'greece', 'sochi', 'turkey', 'bombei',
            'astana', 'bmv', 'audi', 'toyota', 'subaru']
print(all_list)
print(len(all_list))
all_list.sort(reverse=True)
print(all_list)
print(sorted(all_list))
print(all_list)
all_list.remove('Arnold')
print(all_list)
too = 'Enshtein'
all_list.remove(too)
print(all_list)
too_pop = all_list.pop()
print(all_list)
print(too_pop)
all_list.extend(too)
print(all_list)
print(len(all_list))
del all_list[18:26]
print(all_list)
too_pop1 = all_list.pop(0)
print(all_list)
del all_list[-1]
print(all_list)
all_list.insert(0, 'yamaha')
print(all_list)
all_list.append('bugatti')
print(all_list[0].title())
print(all_list)

