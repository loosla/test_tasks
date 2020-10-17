# abc - abc
# abbbab - abab
# aaabbac - abac
# [] - ''
# return: String

# to main.py:
# init_str = "abbbab"
# print(remove_duplicates.remove_duplicates(init_str))

# N - Linear Time Complexity
def remove_duplicates (init_str):
    res_arr = []
    init_arr = list(init_str)
    for n in range(len(list(init_str))-1):
        if init_arr[n] != init_arr[n+1]:
            if res_arr:
                res_arr.pop()
            res_arr.append(init_arr[n])
            res_arr.append(init_arr[n+1])
    return ''.join(res_arr)