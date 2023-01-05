first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print('Hello,', full_name.title(),'!')  #неправильный вариант, тк вставляются пробелы, лучше использовать f-строки
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)