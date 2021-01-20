# def most_wanted(text: str) -> str:
#     res_dict = {}
#     res_list = []
#     for i in text:
#         ch = i.lower()
#         if ch in 'abcdefghijklmnopqrstuvwxyz':
#             if res_dict.get(ch):
#                 val = res_dict.get(ch)
#                 res_dict[ch] = val + 1
#             else:
#                 res_dict[ch] = 1
                
            
                
#     print(res_dict)
#     max_key = max(res_dict, key=res_dict.get)
#     for i in res_dict:
#         if res_dict[i] == res_dict[max_key]:
#             res_list.append(i)
#     if len(res_list) > 1: 
#         res_list.sort()
#         return res_list
#     else: 
#         return res_list

def most_wanted(text: str) -> str:
    result_dict = {}
    result_list = []
    for i in text:
        char = i.lower()
        if char in 'abcdefghijklmnopqrstuvwxyz':
            result_dict[char] = text.lower().count(char)
            
            
    max_key = max(result_dict, key=result_dict.get)
    for i in result_dict:
        if result_dict[i] == result_dict[max_key]:
            result_list.append(i)
    result_list.sort()
    print(result_list)    
    return result_list


# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
#     assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
#     assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
#     assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
#     assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
#     assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
#     print("Start the long test")
#     assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
#     print("The local tests are done.")


#result = most_wanted("Hello World!")
# result = most_wanted("One")
# print(result)

