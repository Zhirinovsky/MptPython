memory = float(input("Введите первое число: "))
i = 1
while (True):
    zero = bool(False)
    operation = input("Выберите операцию: +, -, *, /: ")
    now = float(input("Введите число: "))
    if operation == "+":
        memory = memory + now
    elif operation == "-":
        memory = memory - now
    elif operation == "*":
        memory = memory * now
    elif operation == "/":
        if now != 0: memory = memory / now
        else: zero = bool(True)
    if zero == False: 
        print(f"Результат {i}-ой операции: {memory}")
        i += 1
    else: print(f"Деление на ноль, результат не корректен. Результат {i-1}-ой операции: {memory}")