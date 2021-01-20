'''
Given two numbers, return their GCF. Default is 1

INPUT -> 100, 50
OUTPUT -> 50

INPUT -> 33, 7
OUTPUT -> 1

INPUT -> 32, 24
OUTPUT -> 8
'''
def find_GCF(num_1:int, num_2:int) -> int:
    """Takes in two numbers and returns the greatest common factor (GCF) of the two."""
    factors = []

    max_, min_ = max(num_1, num_2), min(num_1, num_2)

    for i in range(min_, 0, -1):
        fac_1 = min_ % i == 0
        fac_2 = max_ % i == 0
        if fac_1 and fac_2:
            print(i)
            break
    # set_factors1 = set(factors1)
    # set_factors2 = set(factors2)
    # print(max(set_factors1.intersection(set_factors2)))

#find_GCF(12, 9)


"""
Make an LCM Finder, feel free to use the methods you learned today for GCF, lastly use it on your homework so you'll never have to do math again. :P

"""

def lcm_finder(x:int, y:int) -> int:
    """Takes in two numbers and returns the LCM, or Least Common Multiple of the two."""
    if x == 0 or y == 0:
       return (0)
    if x == y:
       return(x)
    
    counter = 1
    
    greater = x
    smaller = y
    if y > x:
        greater = y
        smaller = x
    
    while True:
        if greater * counter % smaller == 0:
            return greater * counter
        counter += 1   

res = lcm_finder(0, 0)
print(res)
    

    




