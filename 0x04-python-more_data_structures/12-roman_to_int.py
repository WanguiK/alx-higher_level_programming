#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    result = 0
    roman_num = 0
    for char in roman_string[::-1]:
        value = roman_value[char]
        if value < roman_num:
            result -= value
        else:
            result += value
        roman_num = value
    return (result)
