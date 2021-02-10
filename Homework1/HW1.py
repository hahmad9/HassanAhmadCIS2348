from datetime import date


def calculateage(currentdate, birthdate):
    today = currentdate
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age


print("Birthday Calculator")
print('Current Day')

m = int(input('Month: '))
d = int(input('Day: '))
y = int(input('Year: '))

print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))

print("You are ", calculateage(date(y, m, d), date(birth_year, birth_month, birth_day)), "years old.")
if d == birth_day:
    print("Happy Birthday!")
