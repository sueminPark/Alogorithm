def solution(my_string, is_prefix):
    # 접두사 관련 함수 startswitch
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0