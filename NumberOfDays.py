months = [0] * 12
min = 0; all = 0
odd = {0, 2, 4, 6, 7, 9, 11}
names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

for i in range(1, 29): min += i

for i in range(12):
    months[i] = min
    if i != 1: 
        months[i] += 29 + 30
        if i in odd: months[i] += 31
    print(f"{names[i]}: {months[i]} дней")
    all += months[i]

print(f"Общее кол-во дней в году: {all} дней")