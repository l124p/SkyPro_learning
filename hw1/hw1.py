# exercise 1
t_f = int(input("Enter temperatur Faringeit: "))
t_c = (t_f - 32) * 5 / 9
print(f"Temperatura C: {t_c}")

# exercise 2
rate_exechange_usd_to_rub = 70.38
rate_exechange_rub_to_eur = 1.22 / 100

money = int(input("Enter summa money USD: "))
print(f"Summa EUR =: {money / rate_exechange_usd_to_rub / rate_exechange_rub_to_eur}")

# exercise 3
weather = input('What is the weather? ')
if weather == 'Good':
    print('Take glass')
else:
    print('Take umbrella')

# Exercise 4
summa = 0
for i in range(12):
    summa += int(input(f"How money in {i} mounth: "))
print("SAve money: ", summa)

# Exercise 5
normal_cycle = 90
express_cycle = 20
cotton_cycle = 90
otj = 10
pol = 10
time_cycle = 0
program, check_otj, check_pol= input("Enter programm: ") ,input("Otj - ON/OFF: "), input("pol - ON/OFF: ")

if program == 'normal_cycle':
    time_cycle += normal_cycle
elif program == 'express_cycle':
    time_cycle = express_cycle
elif program == 'cotton_cycle':
    time_cycle = cotton_cycle
if check_otj == 'OFF':
    time_cycle -= otj
if check_pol == 'OFF':
    time_cycle += pol
print("Time_total: ", time_cycle)