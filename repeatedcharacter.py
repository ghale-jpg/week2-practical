text = input("Enter a string: ")

found = False

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            print("First repeated character:", text[i])
            found = True
            break

    if found:
        break

if not found:
    print("No repeated character found.")