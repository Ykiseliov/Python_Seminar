# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

n = int(input("Введите число:"))
if n < 0:
    print('число отриц')
else:
    n_s = 1
    for i in range (1, n + 1):
        n_s *= i
    print(n_s)
