from sys import argv

def main(filename):
    letters = []

    for i in range(26):
        letters.append(open(str(chr(97 + i)) + ".txt", "a+"))

    with open(filename, "r") as words:
        for i in range(84095):
            try:
                word = words.readline()
                print(word)
                with open(word[0].lower() + ".txt", "a+") as word_file:
                    word_file.write(word)
            except Exception:
                print(Exception)
                continue

    for letter_file in letters:
        letters_file.close()

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 {} [ word list filename ]".format(argv[0]))
        exit(0)
    filename = argv[1] 
    main(filename)
