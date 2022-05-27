s = input()
n = int(input())
new_s = []

for i in range(len(s)):
    if s[i].isupper() == True:
        temp = chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
        new_s.append(temp)
    elif s[i].islower() == True:
        temp = chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))
        new_s.append(temp)
    else:
        new_s.append(s[i])


answer = ''.join(new_s)
print(answer)