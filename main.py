def count_words(content: str) -> int:
    words = content.split()
    return len(words)


def count_letters(content: str) -> dict:
    content = content.lower()
    letters = {}

    for letter in content:
        if not letter.isalpha():
            continue
        elif letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters


def sort_by_occurrence(letters: dict):
    result = []
    for letter, occurrences in letters.items():
        result.append(
            {
                "letter": letter,
                "occurrences": occurrences
            })

    result.sort(key=lambda item: item["occurrences"],
                reverse=True)
    return result


def main():
    book = "books/frankenstein.txt"
    with open(book) as file:
        content = file.read()
        letters = count_letters(content)
        sorted_letters = sort_by_occurrence(letters)

        print(f"--- Begin report of {book} ---")
        print(f"{count_words(content)} words found in the document")
        print()
        for letter in sorted_letters:
            print(f"The '{letter["letter"]}' character was found {letter["occurrences"]} times")
        print("--- End report ---")


main()
