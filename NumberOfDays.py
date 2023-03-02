months = [0] * 12
min = 0; all = 0
odd = {0, 2, 4, 6, 7, 9, 11}
names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

for i in range(1, 29): 

    min += int(i/10) + int(i%10)

for i in range(12):
    months[i] = min
    if i != 1: 
        months[i] += 2 + 9 + 3
        if i in odd: months[i] += 3 + 1
    print(f"{names[i]}: {months[i]} дней")
    all += months[i]

print(f"Общее сумма дней в году: {all} дней")