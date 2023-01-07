# 引数の入力が正しいかどうかをチェックするバリデータを必ず記述
import sys


args = sys.argv[1:]
argc = len(args) - 1

def reverse_file_content(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        text = f.read()
    reverse_text = text[::-1]
    with open(outputpath, 'x') as f:
        f.write(reverse_text)

# 引数の数を確認するバリデータ
def validate_input_outputpath(argc):
    if argc != 2:
        print("Error: Invalid number of arguments.")
        print("Usage: python3 file_manipulator.py reverse arg1 arg2")
        sys.exit(1)


if (args[0] == 'reverse'):
    print(argc)
    validate_input_outputpath(argc)
    reverse_file_content(args[1], args[2])