str = input()
ans = ''
for i in range(len(str)):
    if str[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        ans += str[i].lower()
    elif str[i] in 'abcdefghijklmnopqrstuvwxyz':
        ans += str[i].upper()
        
print(ans)