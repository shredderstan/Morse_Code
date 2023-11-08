MORSE_CODE_DICT = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "  "
}


def string_to_morse(string_input):
    message = ""
    for letter in string_input.lower():
        if letter == " ":
            message += "  "
        else:
            message += MORSE_CODE_DICT[letter] + " "

    return message


def morse_to_string(morse_input):
    message = ""
    for morse in morse_input.split(" "):
        if morse == "":
            message += " "
        else:
            for key, value in MORSE_CODE_DICT.items():
                if morse == value:
                    message += key

    return message


print(string_to_morse("Hello World"))
print(morse_to_string(".... . .-.. .-.. ---  .-- --- .-. .-.. -.."))
