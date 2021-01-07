def main():
    print("The amazing text-centerer program.")

    word = input("Enter a word that needs centering: ")

    while True:
        try:
            width = int(input("Enter the width of the terminal: "))
            break
        except ValueError:
            print("Invalid number.")

    centered_string = center_string(word, width)
    print("The final result is:")
    print(centered_string)


def center_string(word: str, width: int) -> str:
    left_spaces = (width - len(word)) // 2
    result = " " * left_spaces + word
    return result


def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    assert center_string("same_length", 1) == "same_length"
    assert center_string("too_big", 3) == "too_big"
    print("all passed!")


if __name__ == "__main__":
    tests()
    main()
