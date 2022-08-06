
def main():
    inp = input("Enter an name: ")
    print(shorten(inp))


def shorten(n):
    new_n = ""
    for char in n:
        if char not in "aeou":
            new_n += char
    return new_n


if __name__ == "__main__":
    main()
