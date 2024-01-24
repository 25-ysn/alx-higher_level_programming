#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [roman_numbers[x] for x in roman_string] + [0]
    rep = 0
    for j in range(len(numbers) - 1):
        if numbers[j] >= numbers[j+1]:
            rep += numbers[j]
        else:
            rep -= numbers[j]
    return rep
