import sys
import re


args = sys.argv[1:]
argc = len(args) - 1

def reverse_file_content(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        text = f.read()
    reverse_text = text[::-1]
    with open(outputpath, 'x') as f:
        f.write(reverse_text)

def copy_file(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        file = f.read()
    with open(outputpath, 'x') as f:
        f.write(file)

def duplicate_contents(inputpath, n):
    with open(inputpath, 'r') as f:
        file = f.read()
        temp = file
    for i in range(int(n)):
        with open(inputpath, 'w') as f:
            f.write(temp + file)
            temp += file

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r') as f:
        text = f.read()
    replaced_string = re.sub(needle, newstring, text)
    with open(inputpath, 'w') as f:
        f.write(replaced_string)
    


# 引数の数を確認するバリデータ
def validate_argc(option, argc):
    if option != 'replace-string' and argc != 2:
        print("Error: Invalid number of arguments.")
        sys.exit(1)
    if option == 'replace-string' and args != 3:
        print("Error: Invalid number of arguments.")
        sys.exit(1)

# 拡張子を確認するバリデータ
def validate_extension(inputfile, output=''):
    if (not inputfile.endswith('.txt') and output == ''):
        print('Error: The file extension is different.')
        print("Hint: Specify the .txt file as the argument.")
        sys.exit(1)
    if(not inputfile.endswith('.txt') or not output.endswith('.txt')):
        print('Error: The file extension is different.')
        print("Hint: Specify the .txt file as the argument.")
        sys.exit(1)

def validate_duplicate_contents(n):
    pattern = r"^[0-9]+$"
    match = re.match(pattern, n)
    if match == None:
        print("Error: Enter a number for the second argument.")
        sys.exit(1)



if (args[0] == 'reverse'):
    validate_argc(args[0], argc)
    validate_extension(args[1], args[2])
    reverse_file_content(args[1], args[2])
elif (args[0] == 'copy'):
    validate_argc(args[0], argc)
    validate_extension(args[1], args[2])
    copy_file(args[1], args[2])
elif (args[0] == 'duplicate-contents'):
    validate_argc(args[0], argc)
    validate_duplicate_contents(args[2])
    validate_extension(args[1])
    duplicate_contents(args[1], args[2])
elif (args[0] == 'replace-string'):
    validate_argc(args[0], argc)
    validate_extension(args[1])
    replace_string(args[1], args[2], args[3])  
else:
    print("Error: Please specify the correct option.")
    print("Hint: reverse | copy | duplicate-contents")
    sys.exit(1)
