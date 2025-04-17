def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Enter a word: ")
    part = int(input("Enter the part of speech (0=noun, 1=verb, 2=adjective): "))
    make_sentence(word, part)

if __name__ == '__main__':
    main()
