# Задача 1
name = "Надежда"
surname = "Кузнецова"
print(surname, name)
middle_name = input("Введите отчество: ")
age = int(input("Введите возраст: "))
print(name, surname, middle_name, age)

# Задача 2
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

#Задача 3
number = input("Введите любое число больше нуля: ")

while number < '0':
    print("Число должно быть больше нуля!")
    number = input("Введите любое число больше нуля: ")

print(f'{number} + {number + number} + {number + number + number} = {int(number) +int(number + number) + int(number + number + number)}')

#Задача 4
n = int(input("Введите целое положительное число: "))
max = 0

while n > 0:
    last = n % 10
    if last > max:
        max = last
    n = n // 10

print(f"Самая большая цифра в числе {n} - {max}")

#Задача 5
profit = float(input("Введите выручку фирмы: "))
loss = float(input("Введите издержки фирмы: "))
rescue = profit - loss
if profit > loss:
    print("Вы отлично поработали, покрыли все затраты и даже что-то сможете отложить :)")
    print(f"Выручка Вашей фиры составила {rescue}, а рентабельность {profit / rescue * 100: .1f} %")
    employee = int(input("Введите количество сотрудников: "))
    profit_per_employee = float(profit / employee)
    print(f"Если разделить выручку на всех сотрудников, то каждый получит по {profit_per_employee: .1f} y.e.")
elif profit < loss:
    print(f"Вам нужно больше продавать, чтобы покрыть все затраты! На данный момент убыток составляет {-rescue}")
else:
    print("Для стартапа выйти в ноль - неплохой исход событий, но вы же можете больше ;)")

#Задача 6
start = float(input("Введите стартовое значение в километрах: "))
finish = float(input("Введите желаемый результат в километрах: "))
days = 1
while start < finish:
    start = start * 1.1
    days = days + 1

print(f"Спортсмен добьется результата за {days} дн(я/ей)")