import sys


def main():
    encryption = {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y', 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q', 'F': 'k', 'O': 'N', 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l',
    'g': 'S', 'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P', 'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i', 'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z',
    'G': 'F', 'A': 'W', 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 'Q': 'E', 'e': 'Y', 'r': 'R',
    'E': 'm'}

    encryption = {v: k for k, v in encryption.items()}
    file_name = sys.argv[1]

    with open(file_name, 'r') as encrypted:
        snake = encrypted.read()
        snake_txt = ''

        for i in snake:
            #print(i + " ", end='')
            if i.isdigit():
                snake_txt += " "
            else:
                snake_txt += i
        #BAxIUADYf
        #print()
        snake_txt = snake_txt.split()
        decoded = ''

        for word in snake_txt:
            for letter in word:
                if letter.isalpha():
                    decoded += encryption[letter]
            decoded += " "

        decoded = decoded.split()
        print(decoded)

        for word in range(len(decoded)):
            decoded[word] = decoded[word][::-1]
        print(decoded)

        #decoded = " ".join(decoded)

        #if len(sys.argv) < 2:
         #   print("file is missing")
        #elif len(sys.argv) > 2:
          #  print("remove unused parameter")
        #else:
         #   print(decoded)


if __name__ == "__main__":
    main()
