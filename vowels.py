def count_vowels_and_consonants(input_string):
    input_string = input_string.lower()
    vowel_count = 0
    consonant_count = 0
    for char in input_string:
        if char.isalpha():
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)
input_string = "Machine learning!"
vowel_count, consonant_count = count_vowels_and_consonants(input_string)
print("The number of vowels: ", vowel_count)
print("The number of consonants: ", consonant_count)
