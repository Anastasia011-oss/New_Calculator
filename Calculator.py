print("Примитивный калькулятор")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Выход из программы.")
        break

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))


