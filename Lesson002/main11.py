# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input('введите число: '))
f1 = 0
f2 = 1
fn = 0
x = 0
n = 3 # индекс от 1-5
while fn <= a:
    fn = f1+f2 
    x = f2
    f1 = x
    f2 = fn
    if fn == a:
        print(n)
        break
    n +=1
if a != fn:
    print(-1)