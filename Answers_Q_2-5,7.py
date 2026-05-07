
############### Answer question 2 ####################

import os

def GetFileSize(filename):
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        return "File not found"
size = GetFileSize("file.txt")
print(f'The file size is: {size} KB')


############### Answer question 3 ####################

string = 'DDD1233as'

def ValidateStringFormat(string):
    if len(string) != 9:
        return False

    first = string[0:3]
    second = string[3:7]
    third = string[7:9]

    return first.isupper() and second.isdigit() and third.islower()

print(ValidateStringFormat(string))

############### Answer question 4 ####################

with open("file1.txt", "w") as f:
    f.write("Hey, my name is Elad")

with open("file2.txt", "w") as f:
    f.write("Hey, how are you my friend?")

with open("file3.txt", "w") as f:
    f.write("Hey, let's come with me")

import os

def GetSumSize(files):
    total = 0

    for f in files:
        size = os.path.getsize(f)
        total += size

    return total

files = ['file1.txt', 'file2.txt', 'file3.txt']

print(GetSumSize(files))

############### Answer question 5 ####################

def GetWordsFromFile(filename):
    with open(filename, 'r') as f:
        text = f.read()

    words = text.split()
    unique_words = set(words)

    return list(unique_words)
result = GetWordsFromFile("file3.txt")
print(result)

############### Answer question 7 ####################

import os

def WriteReverse(input_file, output_file):
    try:
        print("Current working directory:", os.getcwd())

        if not os.path.exists(input_file):
            print("Input file not found")
            return

        with open(input_file, 'r') as f:
            content = f.read()

        reversed_content = content[::-1]

        with open(output_file, 'w') as f:
            f.write(reversed_content)

        print("Done! Check the output file:", output_file)

    except Exception as e:
        print("Error:", e)

WriteReverse("input.txt", "output.txt")
