print("Примитивный калькулятор")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Процент (a % b)")
    print("0. Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Выход из программы.")
        break

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if choice == "1":
        print("Результат:", a + b)
    elif choice == "2":
        print("Результат:", a - b)
    elif choice == "3":
        print("Результат:", a * b)
    elif choice == "4":
        if b == 0:
            print("Ошибка: деление на ноль!")
        else:
            print("Результат:", a / b)
    elif choice == "5":
        if b == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(f"{a} % {b} = {a % b}")
    else:
        print("Неверный выбор. Попробуйте снова.")



