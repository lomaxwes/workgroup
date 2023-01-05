import os

with open('C:/Users/And/Desktop/wot/input.txt', 'r') as input_file:
   with open('C:/Users/And/Desktop/wot/output.txt', 'w') as output_file:
       for line in input_file:
           output_file.write(line)