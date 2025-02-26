import string

def frequency_analysis(filename):
    """
    Обчислює відносну частоту появи літер у файлі.
    Повертає словник {літера: відносна частота}.
    """
    try:
        with open(filename, "r", encoding="utf-8") as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None

    freq = {}
    total = 0
    # Розглядаємо лише англійські літери (перетворюємо в нижній регістр)
    for char in text.lower():
        if char in string.ascii_lowercase:
            freq[char] = freq.get(char, 0) + 1
            total += 1

    if total == 0:
        print("There are no alphabetical characters in the file for analysis.")
        return None

    relative_freq = {char: count / total for char, count in freq.items()}
    return relative_freq

def display_frequency(filename):
    """
    Виводить на екран відносну частоту появи літер.
    """
    relative_freq = frequency_analysis(filename)
    if relative_freq is None:
        return
    print("Relative frequency:") #
    for letter in sorted(relative_freq):
        print(f"{letter}: {relative_freq[letter]:.2%}")

def guess_key(filename, assumed_common_letter='e'):
    """
    Визначає ймовірний зсув шифру, спираючись на припущення,
    що найбільш часта літера у зашифрованому тексті відповідає assumed_common_letter.
    """
    try:
        with open(filename, "r", encoding="utf-8") as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None

    freq = {}
    total = 0
    for char in text.lower():
        if char in string.ascii_lowercase:
            freq[char] = freq.get(char, 0) + 1
            total += 1

    if total == 0:
        print("There are no alphabetical characters in the file for analysis.")
        return None

    most_common_letter = max(freq, key=freq.get)
    # Обчислення зсуву: різниця між позиціями найбільш частої літери та assumed_common_letter
    shift = (ord(most_common_letter) - ord(assumed_common_letter)) % 26

    print(f"\nThe most common letter in the encrypted text: '{most_common_letter}'")
    print(f"Assumption: this letter corresponds to letter '{assumed_common_letter}'")
    print(f"Possible shift (encryption key): {shift}")
    return shift

if __name__ == '__main__':
    filename = input("Enter the name of the encrypted file for analysis (for example, encrypted.txt): ")
    print("\n--- Frequency analysis ---")
    display_frequency(filename)
    guess_key(filename)