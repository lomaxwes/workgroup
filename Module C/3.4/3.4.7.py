with open('C:/Users/And/Desktop/wot/input2.txt', 'r', encoding='utf8') as input_file:
   with open('C:/Users/And/Desktop/wot/output.txt', 'w', encoding='utf8') as output_file:
       for line in input_file:
           output_file.write(line[::-1])
