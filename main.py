# Case-study #3
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ().
# Program calculates compound interest with investment during each month and displays it in tables.
import local_1
lang = int(input(local_1.CHOOSE))
if lang == 1:
    import local_en as lc
elif lang == 2:
    import local_esp as lc
else:
    import local_ru as lc

years = float(input(lc.YRS))
while years <= 0 or years != int(years):
    print(lc.ERR_1)
    years = float(input(lc.YRS))
years = int(years)

initial_capital = float(input(lc.INIT_CAP))
while initial_capital <= 0:
    print(lc.ERR_2)
    initial_capital = float(input(lc.INIT_CAP))

interest_rate = float(input(lc.INT_RATE))
while interest_rate <= 0:
    print(lc.ERR_3)
    interest_rate = float(input(lc.INT_RATE))

investment_injection = float(input(lc.INV_INJ))
while investment_injection < 0:
    print(lc.ERR_4)
    investment_injection = float(input(lc.INV_INJ))
# TODO: Make formula for compound interest rate (Drachev N.)
for year in range(1, years+1):
    print(year, lc.YEAR)
    print("-------------------------------------------")
    print("|       |   {}   | {}  |         |".format(lc.BASE, lc.SUM))
    print("| {} | {} |{} | {} |".format(lc.MONTH, lc.INVESTMENTS, lc.F_MON, lc.CAP))
    print("-------------------------------------------")
    for counter in range(1, 13):
        if counter == 12 and year == years:
            main_money = initial_capital * (1 + interest_rate / 100)
            first_money = main_money - initial_capital
            main_money = initial_capital * (1 + interest_rate / 100)
            print("|  {}  |  {}  |  {}  |  {}  |".format(counter, '{:.2f}'.format(initial_capital),
                                                         '{:.2f}'.format(first_money), '{:.2f}'.format(main_money)))
            initial_capital = main_money
            print("-------------------------------------------")
        else:
            main_money = initial_capital * (1 + interest_rate / 100)
            first_money = main_money - initial_capital
            main_money = initial_capital * (1 + interest_rate / 100) + investment_injection
            print("|  {}  |  {}  |  {}  |  {}  |".format(counter, '{:.2f}'.format(initial_capital),
                                                     '{:.2f}'.format(first_money), '{:.2f}'.format(main_money)))
            initial_capital = main_money
            print("-------------------------------------------")
pass


