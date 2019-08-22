'''
c의 itoa() 구현하기
'''


def my_str(number):
    string = ""
    while number != 0:
        num = number % 10
        string = chr(ord("0") + num) + string
        number //= 10

    return string


print(my_str(14000))
