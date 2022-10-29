import sys


def println(x):
    print(x)


def print_words(file_name):
    word_counting = {}
    with open(file_name, 'r', encoding='utf8') as file:
        f = file.read()
        f = f.split()
        for word in f:
            if word.strip() not in word_counting:
                word_counting[word.strip()] = f.count(word)
    print(word_counting)
    return word_counting


def print_top(file_name):
    word_counting = print_words(file_name)
    sorted_counting = {k: v for k, v in sorted(word_counting.items(), key=lambda item: item[1])}
    for i in list(sorted_counting.items())[-20:]:
        print(i)


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    file_name = sys.argv[2]
    if option == '--count':
        print_words(file_name)
    elif option == '--topcount':
        print_top(file_name)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

    println("hello")


def pas():
    pass


if __name__ == '__main__':
    main()
