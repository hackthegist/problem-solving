'''
python string 뒤집기
'''

s = "Reverse this strings"
r_s = ""
for i in range(-1, -len(s)-1, -1):
    r_s += s[i]
print(r_s)
