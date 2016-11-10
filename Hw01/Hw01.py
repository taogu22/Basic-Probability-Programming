import random
import datetime
from datetime import date

favoNum = random.randint(1, 1001)
yourName = input('\nHello, I am Christian. What is your name? Please only give me one first name followed by your entire last name. ')
nameList = yourName.split()
givenName = nameList[0]
delimiter = ' '
surName = delimiter.join(nameList[1:])
#print(surName)

print('\nMy favourite number is ' + str(favoNum) +".")

birthIn = input('\nIt is a pleasure to meet you! What is your birthday? Input in YYYY/MM/DD format ')
birthYear, birthMon, birthDay = map(int, birthIn.split('/'))
#yourBirth  = datetime.date(birthYear, birthMon, birthDay) #Change to suit -1
#print(yourBirth)
today = date.today()
#print(today)
yourAge = abs(today.year - birthYear)
# We still need to compare the month and day in order to give the exact age
if today.month < birthMon: yourAge -= 1
elif today.month == birthMon and today.day < birthDay: yourAge -= 1
#print(yourAge)


smokeBool = input('\nDo you smoke? input yes/no')

print('\nIt was nice talking to you! Let me summarise what I learned abuot you.')
print('Your given name is ' + str(givenName) + '.')
print('Your surname is ' + surName + '.')
print('You are ' + str(yourAge) + ' years old.')
print('Smoker: ' +str(smokeBool).lower())