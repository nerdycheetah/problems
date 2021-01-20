'''
Make a function that takes in a single number and prints things according to this rule-set:

If the number is divisible by both 3 and 5:
    - 'FizzBuzz'
If the number is divisible by 5 and not 3:
    - 'Fizz'
If the number is divisible by 3 and not 5:
    - 'Buzz'
If the number is not divisible by either:
    - The string version of the number
    It should return 'SIKE'

Once finished with this function, run this on numbers from 100 - 1 with any method of your choice
'''
# def fizzy(n:int) -> str:
#     '''oh ma gad'''
#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 5 == 0:
#         return 'Fizz'
#     elif n % 3 == 0:
#         return 'Buzz'
#     else:
#         return 'SIKE', str(n)

# for i in range(100,0,-1):
#     print(fizzy(i))

def fizzy(n:int) -> str:
    fiz_map = {
        (True, True) : lambda x: 'FizzBuzz',
        (True, False) : lambda x: 'Fizz',
        (False, True) : lambda x: 'Buzz',
        (False, False) : lambda x: str(x)
    }x
    div_5 = n % 5 == 0
    div_3 = n % 3 == 0
    key = (div_5, div_3)
    function = fiz_map[key]
    result = function(n)
    return result

# print(fizzy(100))

''''''
rand_func = lambda x: 'hello'
for i in range(10):
    print(rand_func(i))