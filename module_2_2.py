first = int(input("Введите числа: "))
second = int(input("Введите числа: "))
third = int(input("Введите числа: "))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)