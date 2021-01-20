def get_day_input(day:int, cast:type=None, strip:bool=True, split_by:str=None) -> list:
    '''
    Returns list of input values from reading day specific text file
    '''
    out = []
    path = f"./inputs/day_{day}.txt"
    try:
        with open(path, 'r') as file:
            if not split_by:
                data = file.readlines()
            else:
                data = file.read().split(split_by)
            for raw in data:
                clean = raw
                if strip:
                    clean = clean.strip()
                if cast:
                    clean = cast(clean)
                out.append(clean)
    except:
        pass
    return out



# Day 1
day_1_test = [1721, 979, 366, 299, 675, 1456]
day_1_ans = 514579

def day_1_part1(test_example:list) -> int:
    
    for i in range(len(test_example)):
        cur_val = test_example[i]
        for j in range(i + 1, len(test_example)):
            next_val = test_example[j]
            if cur_val + next_val == 2020:
                return cur_val * next_val
                    
            
        

# test_res = day_1_part1(day_1_test)
# print(test_res, test_res == day_1_ans)
day_1_input = get_day_input(1, int)
# print(day_1_part1(day_1_input))



def day_1_part2(test_example:list) -> int:
    
    for i in range(len(test_example)):
        num_1 = test_example[i]
        for j in range(i + 1, len(test_example)):
            num_2 = test_example[j]
            if num_1 + num_2 < 2020:
                for x in range(j + 1, len(test_example)):
                    num_3 = test_example[x]
                    if num_1 + num_2 + num_3 == 2020:
                        return num_1 * num_2 * num_3

# print(day_1_part2(day_1_test))
# print(day_1_part2(day_1_input))

# Day 2
day_2_input = get_day_input(2)
day_2_test = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.split('\n')


def day_2_part1(test_example:str) -> int:
    cnt = 0
    res = []

    for policy in test_example:
        splt = policy.split()

        n_range = splt[0]
        char = splt[1][0]
        password = splt[2]

        # Tasks for the week
        'Clean up the n_range variable (maybe turn it into in? range?)'
        # Split the string
        n_range = list(map(int, n_range.split('-')))

        'Count the number of char in password'
        num = password.count(char)

        'Compare that count to range to see if theres enough'
        n_range = range(n_range[0], n_range[1] + 1)
        
        if num in n_range:
            # res.append(policy)
            cnt += 1
    
    return cnt


# print(day_2_part1(day_2_input))


def day_2_part2(test_example:str) -> int:
    cnt = 0

    for policy in test_example:
        splt = policy.split()

        position = list(map(int, splt[0].split('-')))
        char = splt[1][0]
        password = splt[2]

        n_char = int(password[position[0] - 1] == char) + int(password[position[1] - 1] == char)
        if n_char == 1:
            cnt += 1
        
        
    return cnt 

print(day_2_part2(day_2_input))