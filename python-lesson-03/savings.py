## Week 3 Assignment - Savings Calculator ##
import locale

locale.setlocale(locale.LC_ALL, '')

money_start = round(int(input("how much money do you have currently?")))
saving_years = round(int(input("how many years do you have to save?")))
interest_rate = input("what is the interest rate?")

if "%" in interest_rate:
    interest_rate = interest_rate.replace("%","")
    interest_rate_clean = float(interest_rate)
else:
    interest_rate_clean = float(interest_rate)

money_result = (money_start * (interest_rate_clean/100) * saving_years) + money_start

if money_result > 10000:
    print(f"""Your savings after {saving_years} years: {locale.currency(money_result,grouping=True)}..."
Yes, you will be able to afford your holiday!""")
else:
    print(f"""Your savings after {saving_years} years: {locale.currency(money_result,grouping=True)}..."
No, you will not be able to afford your holiday :(""")