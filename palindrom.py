def palindrome(a):
    
    b = str(a[::-1])

    if b == a:
        print("Данная строка является палиндромом")
    else:
        print("Данная строка не является палиндромом")

c = input("Введите строку: ")
palindrome(c)