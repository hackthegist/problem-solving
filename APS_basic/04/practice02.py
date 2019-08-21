stack = [0] * 10
top = -1
word1 = "(())"
flag = True

for ch in word1:
    if ch == ")":
        if top == -1:
            print("There's a closing paren without opening")
            flag = False
            break
        else:
            if stack[top] != "(":
                print("not matched")
                flag = False
                break
            else:
                top -= 1

    if ch == "(":
        top += 1
        stack[top] = ch

if flag:
    print("well matched!")
