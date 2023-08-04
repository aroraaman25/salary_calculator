import os 
os.system("cls")

try:
    hours_worked=float(input('How many hours did you work last month? '))
    hourly_rate=float(input('What is your hourly rate? '))
except EOFError as e:
    print(e)
last_month_earned=(hours_worked*hourly_rate)
print('Last month, you earned', last_month_earned, 'dollars')