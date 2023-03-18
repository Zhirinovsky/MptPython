import pyodbc
import sys
import random

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-9R2S8EF\MYSERVERNAME;DATABASE=MiniBisnessDb;Trusted_Connection=yes;')
connection.autocommit = True
cursor=connection.cursor()
cursor.execute("SELECT Name_Role FROM [Role]")

def AmountChoose(storage):
    array = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, 11):
        if storage[i][2] > 0: array[i-3] = 1
    return array

def UserOrder(result, meatType, ingredientsArray, storage, meatArray, skidka, amount):
    if meatType != "Свинина" and meatType != "Говядина" and meatType != "Курица":
        meatType = ""
        if storage[0][2] > 0: meatType += "Свинина, "
        if storage[1][2] > 0: meatType += "Говядина, "
        if storage[2][2] > 0: meatType += "Курица "
        choose = input(f"Выберите тип мяса: {meatType}\n" + 
                    f"Цена за Свинину: {storage[0][3]}\n" + 
                    f"Цена за Говядину: {storage[1][3]}\n" + 
                    f"Цена за Курицу: {storage[2][3]}\n")
        if choose=="Свинина": 
            if storage[0][2] > 0: 
                meatType = "Свинина"
                meatArray[0] = 1
            else: 
                print("Свинины нет на складе")
        elif choose=="Говядина":
            if storage[1][2] > 0: 
                meatType = "Говядина"
                meatArray[1] = 1
            else: 
                print("Говядины нет на складе")
        elif choose=="Курица":
            if storage[2][2] > 0: 
                meatType = "Курица"
                meatArray[2] = 1
            else: 
                print("Курицы нет на складе")
        else: 
            print("Указан неверный тип мяса\n")
        UserOrder(result, meatType, ingredientsArray, storage, meatArray, skidka, amount)
    ingredients = ""
    if ingredientsArray[0] == 1: ingredients += "Картошка, "
    if ingredientsArray[1] == 1: ingredients += "Сыр, "    
    if ingredientsArray[2] == 1: ingredients += "Помидоры, "
    if ingredientsArray[3] == 1: ingredients += "Майонез, "
    if ingredientsArray[4] == 1: ingredients += "Грибы, "
    if ingredientsArray[5] == 1: ingredients += "Соль, "  
    if ingredientsArray[6] == 1: ingredients += "Перец, "  
    if ingredientsArray[7] == 1: ingredients += "Масло "
    print(f"На данный момент в состав блюда входит: {meatType}, {ingredients}\n" + 
          f"Цена за Свинину: {storage[0][3]}\n" + 
          f"Цена за Говядину: {storage[1][3]}\n" + 
          f"Цена за Курицу: {storage[2][3]}\n" + 
          f"Цена за Картошку: {storage[3][3]}\n" + 
          f"Цена за Сыр: {storage[4][3]}\n" + 
          f"Цена за Помидоры: {storage[5][3]}\n" +
          f"Цена за Майонез: {storage[6][3]}\n" +
          f"Цена за Грибы: {storage[7][3]}\n" +
          f"Цена за Соль: {storage[8][3]}\n" +
          f"Цена за Перец: {storage[9][3]}\n" +
          f"Цена за Масло: {storage[10][3]}")
    currentPrice = meatArray[0] * storage[0][3] + meatArray[1] * storage[1][3] + meatArray[2] * storage[2][3] + ingredientsArray[0] * storage[3][3] + ingredientsArray[1] * storage[4][3] + ingredientsArray[2] * storage[5][3] + ingredientsArray[3] * storage[6][3] + ingredientsArray[4] * storage[7][3] + ingredientsArray[5] * storage[8][3] + ingredientsArray[6] * storage[9][3] + ingredientsArray[7] * storage[10][3]
    print(f"Цена одного блюда на данный момент: {currentPrice}, цена с учётом скидок: {currentPrice - (currentPrice / 100 * skidka)}, цена за весь заказ: {(currentPrice - (currentPrice / 100 * skidka)) * amount}")
    choose = input("\nВведите название ингредиента для того, чтобы добавить/убрать его. Введите Далее для того, чтобы заказать. ")
    if choose == "Картошка": 
        if ingredientsArray[0]==1: ingredientsArray[0]=0
        else: 
            if storage[3][2] > 0: ingredientsArray[0]=1
            else: print("Картошки нет на складе ")
    elif choose == "Сыр": 
        if ingredientsArray[1]==1: ingredientsArray[1]=0
        else: 
            if storage[4][2] > 0: ingredientsArray[1]=1
            else: print("Сыра нет на складе ")
    elif choose == "Помидоры": 
        if ingredientsArray[2]==1: ingredientsArray[2]=0
        else: 
            if storage[5][2] > 0: ingredientsArray[2]=1
            else: print("Помидоров нет на складе ")
    elif choose == "Майонез": 
        if ingredientsArray[3]==1: ingredientsArray[3]=0
        else: 
            if storage[6][2] > 0: ingredientsArray[3]=1
            else: print("Майонеза нет на складе ")
    elif choose == "Грибы": 
        if ingredientsArray[4]==1: ingredientsArray[4]=0
        else: 
            if storage[7][2] > 0: ingredientsArray[4]=1
            else: print("Грибов нет на складе ")
    elif choose == "Соль": 
        if ingredientsArray[5]==1: ingredientsArray[5]=0
        else: 
            if storage[8][2] > 0: ingredientsArray[5]=1
            else: print("Соли нет на складе ")
    elif choose == "Перец": 
        if ingredientsArray[6]==1: ingredientsArray[6]=0
        else: 
            if storage[9][2] > 0: ingredientsArray[6]=1
            else: print("Перца нет на складе ")
    elif choose == "Масло": 
        if ingredientsArray[7]==1: ingredientsArray[7]=0
        else: 
            if storage[10][2] > 0: ingredientsArray[7]=1
            else: print("Масла нет на складе ")
    elif choose == "Далее": 
        if(random.randint(1,6) == 5):
            input("В заказ попала что-то инородное: лягушка ")
            if(random.randint(1,6) == 5):
                input("Клиент заметил инородное тело, предоставляется дополнительная скидка в 30% ")
                skidka += 30
            else:
                input("Клиент не заметил ничего инородного ")
        else:
            input("В заказ не попало ничего инородного ")
        finalPrice = meatArray[0] * storage[0][3] + meatArray[1] * storage[1][3] + meatArray[2] * storage[2][3] + ingredientsArray[0] * storage[3][3] + ingredientsArray[1] * storage[4][3] + ingredientsArray[2] * storage[5][3] + ingredientsArray[3] * storage[6][3] + ingredientsArray[4] * storage[7][3] + ingredientsArray[5] * storage[8][3] + ingredientsArray[6] * storage[9][3] + ingredientsArray[7] * storage[10][3]
        if result[0][3] < finalPrice: print("Недостаточно средств на балансе")
        else:
            cursor.execute(f"INSERT INTO Dish (Meat, Potato, Cheese, Tomato, Mayo, Mushroom, Salt, Pepper, Oil, Price, User_ID, Amount) values ('{meatType}', {ingredientsArray[0]}, {ingredientsArray[1]}, {ingredientsArray[2]}, {ingredientsArray[3]}, {ingredientsArray[4]}, {ingredientsArray[5]}, {ingredientsArray[6]}, {ingredientsArray[7]}, {(finalPrice  - (finalPrice / 100 * skidka)) * amount}, {result[0][0]}, {amount})")
            cursor.execute(f"UPDATE [User] SET Balance = Balance - {(finalPrice - (finalPrice / 100 * skidka)) * amount} where ID_User = {result[0][0]}")
            cursor.execute(f"UPDATE [User] SET WastedMoney = WastedMoney + {(finalPrice - (finalPrice / 100 * skidka)) * amount} where ID_User = {result[0][0]}")
            cursor.execute(f"UPDATE [User] SET Balance = Balance + {(finalPrice - (finalPrice / 100 * skidka)) * amount} where Role_ID = 2")
            cursor.execute(f"SELECT * FROM Dish WHERE User_ID = {result[0][0]} ORDER BY Date DESC")
            check = cursor.fetchall()
            info = ""
            if check[0][2] == 1: 
                info += "Картошка, "
            if check[0][3] == 1: 
                info += "Сыр, "
            if check[0][4] == 1: 
                info += "Помидоры, "
            if check[0][5] == 1: 
                info += "Майонез, "
            if check[0][6] == 1: 
                info += "Грибы, "
            if check[0][7] == 1: 
                info += "Соль, "
            if check[0][8] == 1: 
                info += "Перец, "
            if check[0][9] == 1: 
                info += "Масло."
            print(f"Заказ успешен\n\n" + 
                  f"Чек: \n" +
                  f"Заказ под номером: {check[0][0]}\n" + 
                  f"Состав заказываемого блюда: {check[0][1]}, {info}\n" + 
                  f"Цена заказа: {check[0][10]}\n" + 
                  f"Заказчик: {result[0][1]}\n" + 
                  f"Дата заказа: {check[0][12]}\n" + 
                  f"Количество блюд: {check[0][13]}")
            input("")
            User(result[0][1])
    else: print("Введённый ингредиент не найден")
    UserOrder(result, meatType, ingredientsArray, storage, meatArray, skidka, amount)

def User(login):
    cursor.execute(f"SELECT * FROM [User] WHERE Login = '{login}'")
    result = cursor.fetchall()
    current_user = result[0][0]
    print("\nВы вошли как " + result[0][1])
    print("Ваш действующий баланс: " + str(result[0][3]))
    if result[0][5] <= 5000:
        print("Действующих скидок нет")
        skidka = 0
    elif result[0][5] <= 15000:
        print("Действует бронзовая карта лояльности, 5% скидка")
        skidka = 5
    elif result[0][5] <= 25000:
        print("Действует серебряная карта лояльности, 10% скидка")
        skidka = 10
    else:
        print("Действует золотая карта лояльности, 20% скидка")
        skidka = 20
    action2 = int(input("Выберите дальнейшее действие: 1 - Просмотр покупок, 2 - Сделать заказ, 3 - Выйти из учётной записи. "))
    if action2 == 1:
        print("\nИстория покупок: ")
        cursor.execute(f"SELECT * FROM [Dish] WHERE User_ID = '{current_user}'")
        history = cursor.fetchall()
        for i in range(0, len(history)):
            info = ""
            if history[i][2]: 
                info += "Картошка, "
            if history[i][3]: 
                info += "Сыр, "
            if history[i][4]: 
                info += "Помидоры, "
            if history[i][5]: 
                info += "Майонез, "
            if history[i][6]: 
                info += "Грибы, "
            if history[i][7]: 
                info += "Соль, "
            if history[i][8]: 
                info += "Перец, "
            if history[i][9]: 
                info += "Масло."
            print(f"{i+1}. Состав: {history[i][1]}, {info} Цена: {history[i][10]}, Дата и время заказа: {history[i][12]}, Количество блюд: {history[i][13]}")
        input("")
    elif action2==2:
        print("\nЗаказанное блюдо: Мясо по французски. ")
        cursor.execute(f"SELECT * FROM Storage")
        storage = cursor.fetchall()
        meatType = ""
        meatArray = [0, 0, 0]
        ingredientsArray = AmountChoose(storage)
        amount = int(input("Введите количество заказываемых блюд: "))
        while amount <= 0:
            print("Некоректное число блюд")
            amount = int(input("Введите количество заказываемых блюд: "))
        UserOrder(result, meatType, ingredientsArray, storage, meatArray, skidka, amount)
    elif action2==3:
        Main()
    else:
        input("Введено некоректное значение")
    User(login)

def AdminBuyIngredient(login):
    cursor.execute(f"SELECT * FROM [User] WHERE Login = '{login}'")
    result = cursor.fetchall()
    cursor.execute(f"SELECT * FROM Seller")
    seller = cursor.fetchall()
    print(f"\nЦена за Свинину: {seller[0][2]}\n" + 
        f"Цена за Говядину: {seller[1][2]}\n" + 
        f"Цена за Курицу: {seller[2][2]}\n" + 
        f"Цена за Картошку: {seller[3][2]}\n" + 
        f"Цена за Сыр: {seller[4][2]}\n" + 
        f"Цена за Помидоры: {seller[5][2]}\n" +
        f"Цена за Майонез: {seller[6][2]}\n" +
        f"Цена за Грибы: {seller[7][2]}\n" +
        f"Цена за Соль: {seller[8][2]}\n" +
        f"Цена за Перец: {seller[9][2]}\n" +
        f"Цена за Масло: {seller[10][2]}")
    ingredient = input(f"Имеющийся баланс: {str(result[0][3])}. Введите название ингредиента, который хотите купить. Для выхода введите Выход. ")
    if ingredient == "Выход": Admin(login)
    else: 
        check = 0
        for i in range (0, 11):
            if ingredient == seller[i][1]: check += 1
        if check == 0: print("Введённый ингредиент не найден")
        else: 
            amount = float(input("Введите количество покупаемого ингредиента. "))
            cursor.execute(f"SELECT Price FROM Seller WHERE Ingredient_Name = '{ingredient}'")
            price = float(cursor.fetchval())
            if amount*price < result[0][3]:
                cursor.execute(f"UPDATE [User] SET Balance = Balance - {amount*price} WHERE Role_ID = 2")
                cursor.execute(f"UPDATE Storage SET Amount = Amount + {amount} WHERE Ingredient_Name = '{ingredient}'")
                print("Ингредиент куплен. ")
    AdminBuyIngredient(login)

def AdminChangePrice(login):
    cursor.execute(f"SELECT * FROM Storage")
    storage = cursor.fetchall()
    print(f"\nЦена за Свинину: {storage[0][3]}\n" + 
          f"Цена за Говядину: {storage[1][3]}\n" + 
          f"Цена за Курицу: {storage[2][3]}\n" + 
          f"Цена за Картошку: {storage[3][3]}\n" + 
          f"Цена за Сыр: {storage[4][3]}\n" + 
          f"Цена за Помидоры: {storage[5][3]}\n" +
          f"Цена за Майонез: {storage[6][3]}\n" +
          f"Цена за Грибы: {storage[7][3]}\n" +
          f"Цена за Соль: {storage[8][3]}\n" +
          f"Цена за Перец: {storage[9][3]}\n" +
          f"Цена за Масло: {storage[10][3]}")
    ingredient = input("Введите название ингредиента, цену на который нужно изменить. Для выхода введите Выход. ")
    if ingredient == "Выход": Admin(login)
    else: 
        check = 0
        for i in range (0, 11):
            if ingredient == storage[i][1]: check += 1
        if check == 0: print("Введённый ингредиент не найден")
        else: 
            price = float(input("Введите новую цену для ингредиента. "))
            cursor.execute(f"UPDATE Storage SET Price = {price} WHERE Ingredient_Name = '{ingredient}'")
            print("Новая цена успешно установлена. ")
    AdminChangePrice(login)

def Admin(login):
    cursor.execute(f"SELECT * FROM [User] WHERE Login = '{login}'")
    result = cursor.fetchall()
    current_user = result[0][0]
    print("\nВы вошли как администратор " + result[0][1])
    print("Ваш действующий баланс: " + str(result[0][3]))
    action2 = int(input("Выберите дальнейшее действие: 1 - Просмотр историю покупок клиента, 2 - Изменение цен на ингредиенты, 3 - Закупка ингредиентов, 4 - Выйти из учётной записи. "))
    if action2 == 1:
        user = int(input("Введите номер клиента, чью историю покупок стоит вывести "))
        cursor.execute(f"SELECT * FROM [User] WHERE ID_User = '{user}'")
        if cursor.rowcount != 0:
            cursor.execute(f"SELECT * FROM [Dish] WHERE User_ID = '{user}'")
            if cursor.rowcount != 0:
                history = cursor.fetchall()
                print("\nИстория покупок: ")
                for i in range(0, len(history)):
                    info = ""
                    if history[i][2]: 
                        info += "Картошка, "
                    if history[i][3]: 
                        info += "Сыр, "
                    if history[i][4]: 
                        info += "Помидоры, "
                    if history[i][5]: 
                        info += "Майонез, "
                    if history[i][6]: 
                        info += "Грибы, "
                    if history[i][7]: 
                        info += "Соль, "
                    if history[i][8]: 
                        info += "Перец, "
                    if history[i][9]: 
                        info += "Масло."
                    print(f"{i+1}. Состав: {history[i][1]}, {info}. Цена: {history[i][10]}, Дата и время заказа: {history[i][12]}, Количество блюд: {history[i][13]}")
                input("")
            else:
                print("Данный пользователь не имеет истории покупок")
        else:
            print("Введённый пользователь не найден")
        Admin(login)
        
    elif action2==2:
        AdminChangePrice(login)
        
    elif action2==3:
        AdminBuyIngredient(login)

    elif action2==4:
        Main()

    else:
        input("Введено некоректное значение")
        Admin(login)

def Main():
    action = int(input("Вход в систему. Выберите действие: 1 - Авторизация, 2 - Регистрация, 3 - Выход. "))
    if action == 1: 
        print("Авторизация ")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        cursor.execute(f"SELECT Login FROM [User] WHERE Login = '{login}' and Password = '{password}' and Role_ID = 2")
        if cursor.rowcount != 0:
            Admin(login)
        else:
            cursor.execute(f"SELECT Login FROM [User] WHERE Login = '{login}' and Password = '{password}' and Role_ID = 1")
            if cursor.rowcount != 0:
                cursor.execute(f"UPDATE [User] SET Balance = Balance + {100 + random.randint(20, 40)} WHERE Login = '{login}'")
                User(login)
            else:
                input("Пользователь не найден" )
    elif action == 2:
        print("Регистрация ")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        cursor.execute(f"INSERT INTO [User] (Login, Password, Balance, Role_ID, WastedMoney) values ('{login}', '{password}', {100 * random.randint(20, 40)}, 1, 0)")
        cursor.commit()
        input("Регистрация успешна ")
    elif action == 3: 
        print("Выход... ")
        sys.exit()
    else: 
        print("Ошибка, введенно неверное значение ")
    Main()

Main()