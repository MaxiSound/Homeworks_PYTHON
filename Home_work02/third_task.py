# 3. Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

n = int(input("Введите число: \n"))
s = 0
for i in range(1,n+1):
    s += (1+1/i)**i
print(f"Cумма последовательности (1+1/n)^n равна: \n{round(s,2)}")

# Можно так:

# lst = [(1+1/i)**i for i in range(1,n+1)]
# print(f"Cумма последовательности (1+1/n)^n равна: \n{round(sum(lst),2)}")