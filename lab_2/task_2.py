money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Посчитайте количество  месяцев, которое можно протянуть без долгов
month_count = 0
while True:
    if month_count == 0:
        money_capital = money_capital + salary - spend
    else:
        spend += spend * increase
        money_capital = money_capital + salary - spend
        if money_capital < 0:
            break
    month_count += 1


print("Количество месяцев, которое можно протянуть без долгов:", month_count)
