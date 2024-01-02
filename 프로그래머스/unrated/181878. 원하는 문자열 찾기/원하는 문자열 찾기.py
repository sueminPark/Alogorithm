def solution(myString, pat):
    A = myString.upper()
    B = pat.upper()
    if B in A:
        return 1
    else:
        return 0