'''
Given a Roman Numeral string ('XI'), return the integer version of it

You may have to look up rules surrounding roman numerals and their expressions
'''


def roman_to_int(roman:str) -> int:
    '''Takes in a Roman numeral and returns the equivalent number/digit.'''
    roman_numerals_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
    res = 0
    if len(roman) == 0:
        return res
    # 'CIX'
    i = 0
    while i < len(roman):
        cur_char = roman[i]
        cur_val = roman_numerals_dict.get(cur_char, None)

        next_char = roman[i + 1]
        next_val = roman_numerals_dict.get(next_char, None)

        if cur_val > next_val:
            res += cur_val
            i += 1
        else:
            res += next_val - cur_val
            i += 2

    return res

result = roman_to_int('CM')
print(result)




    
