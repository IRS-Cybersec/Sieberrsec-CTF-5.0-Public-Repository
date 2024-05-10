interesting = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]


def reverser(text: str) -> str:
    output = ""

    curr = 0
    for i in interesting:
        output += text[curr : curr + i][::-1]
        curr += i

    return output


def main():
    text = input("Enter the reversed text: ")
    print(reverser(text))


if __name__ == "__main__":
    main()
