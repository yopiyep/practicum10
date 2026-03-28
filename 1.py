sentence = input()


def count_letters(sentence: str) -> None:
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    consonants = set('бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ')

    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print(f"Количество гласных: {vowel_count}")
    print(f"Количество согласных: {consonant_count}")

count_letters(sentence)