lines = []
n = int(input())
year = int(input())

for i in range(n):
  holiday = input()
  lines.append(holiday)
  
start_month = input("")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_count = [52+n] * 7
holidays = [0] * 7

num = days.index(start_month)
day_count[num] += 1

def check_year(y):
  return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

flag = check_year(year)

if flag == True:
  if num == 6:
    day_count[0] += 1
  else:
    day_count[num + 1] += 1

# Подсчет праздников

month_num = [0] * 12 # номер дня недели перого числа месяца
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if flag == True:
  month_days[1] = 29

def update(num):
  if num > 6:
    return num % 7
  else:
    return num

month_num[0] = num

for i in range(1, 12):
  month_num[i] = update(month_num[i-1] + month_days[i-1])

for i in range(n):
  day, month = lines[i].split()
  day = int(day)
  n = months.index(month)
  d = update(month_num[n] + day - 1)
  holidays[d] += 1

for i in range(7):
  day_count[i] -= holidays[i]

max = 0 # Лучший
min = 0   # Худший

for i in range(7):
  if day_count[i] < day_count[min]:
    min = i
  if day_count[i] > day_count[max]:
    max = i

res = days[max] + " " + days[min]
print(res)