n = int(input("введите км в день:"))
m = int(input("Введите маршрут в км:"))
days = m // n + (m%n > 0)
print (days)
