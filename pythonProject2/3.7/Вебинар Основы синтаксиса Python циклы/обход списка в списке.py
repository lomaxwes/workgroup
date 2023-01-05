countries_temp = [
                  ['Tai', [20, 22, 23, 21, 18, 35]],
                  ['Ger', [15, 13, 16, 19, 20]],
                  ['Rus', [10, 8, 15, 12, 11, 3, 9]],
                  ['Pol', [13, 12, 18, 17, 19]]
]



for country in countries_temp:
    avr_temp = sum(country[1])/len(country[1])
    print(f"Средняя температура в {country[0]} ---> {avr_temp :.2f} ")

# for dva in countries_temp:
#     # print(i[0])
#     # print(i[1])
#     # print(len(dva[0]))
#     # print(len(dva[1]))
#     for i in dva:
#         print(i)

