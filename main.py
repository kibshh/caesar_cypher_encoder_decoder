alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def coding(text_to_shift, shift_count, direction_to_code):
    new_text = ""
    for letter in text_to_shift:
        if letter not in alphabet:
            new_text += letter
            continue
        index = alphabet.index(letter)
        if direction_to_code == 'encode':
            index += shift_count
            index %= len(alphabet)
        else:
            index -= shift_count
            if index < 0:
                index += len(alphabet)
        new_text += alphabet[index]
    return new_text

answer_to_continue = 'yes'
while(answer_to_continue == 'yes'):
    direction = ""
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()

    while True:
        try:
            shift = int(input("Type the shift number: "))
            if shift < 0:
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    shift %= 26
    text = coding(text_to_shift=text, shift_count=shift, direction_to_code=direction)
    print(f"The {direction}d message is: {text}")

    answer_to_continue = ""
    while answer_to_continue not in ['yes', 'no']:
        answer_to_continue = input("\nDo you want to restart the program? Type yes/no: ").lower()
print("\nThank you for using our program! Kibshh")