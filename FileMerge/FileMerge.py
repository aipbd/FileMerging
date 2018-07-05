import fileinput
import glob

file_list = glob.glob("*.json")

with open('result.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)