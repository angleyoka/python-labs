def search(message,letter):
    output = []
    for indx , char in enumerate(message):
        if char == letter:
            output.append(indx)
    return output


# word = input("Enter word")
# letter = input("Enter the letter")
# x = search(word,letter)
# #print(x)


