def solution(my_string, index_list):
    ans = ''
    for i in index_list:
        ans += my_string[i]
    return ans