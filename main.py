# Case-study #2
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ().
# Program calculate compound interest rate with investment during the each month

import local as lc
years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))
for year in range(1, years + 1):
    print(year, "год")
    print("-------------------------------------------")
    print("|       |   основа   | сумма %  |         |")
    print("| месяц | инвестиций | за месяц | капитал |")
    print("-------------------------------------------")
# TODO: Make formula for compound interest rate (Drachev N.)
main_money = initial_capital * (1 + percent/100)
first_money = main_money - initial_capital
initial_capital = initial_capital * (1 + percent/100)
pass
# TODO: Make network for formula
pass
# TODO: Make loop for network
pass
