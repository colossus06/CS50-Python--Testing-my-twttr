text = input('Enter text: ')

for char in text:
    if char in 'aeiou':

        char.replace(char, "")
    else:
        print(char, end ="")