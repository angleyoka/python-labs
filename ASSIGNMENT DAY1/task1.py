def alphabet(text):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'U', 'I']
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
