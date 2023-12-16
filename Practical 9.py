def file_statistics(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # a. Print total number of characters, words, and lines
        total_characters = len(content)
        total_words = len(content.split())
        total_lines = content.count('\n') + 1
        print(f"Total Characters: {total_characters}")
        print(f"Total Words: {total_words}")
        print(f"Total Lines: {total_lines}")

        # b. Calculate frequency of each character
        character_frequency = {}
        for char in content:
            if char.isalnum():
                character_frequency[char] = character_frequency.get(char, 0) + 1
        print("Character Frequency:")
        for char, count in character_frequency.items():
            print(f"{char}: {count}")

        # c. Print words in reverse order
        words = content.split()
        reversed_words = ' '.join(reversed(words))
        print("Words in Reverse Order:")
        print(reversed_words)

        # d. Copy even lines to File1 and odd lines to File2
        lines = content.splitlines()
        even_lines = [line for i, line in enumerate(lines) if i % 2 == 0]
        odd_lines = [line for i, line in enumerate(lines) if i % 2 != 0]

        with open('File1.txt', 'w') as file1:
            file1.write('\n'.join(even_lines))

        with open('File2.txt', 'w') as file2:
            file2.write('\n'.join(odd_lines))


# Replace 'your_file.txt' with the actual path to your text file
file_path = 'your_file.txt'
file_statistics(file_path)

