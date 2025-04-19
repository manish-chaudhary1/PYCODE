#Prompt the user to enter their birth year, month, and day.
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))

#Import the datetime module to work with dates.
import datetime
#Get the current date and time.
now = datetime.datetime.now()
#Create a datetime object for the user's birth date.
birth_date = datetime.datetime(year, month, day)
#Calculate the difference between the current date and the birth date.
age = now - birth_date
#Calculate the number of years, months, and days from the age difference.
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30
#Print the user's age in years, months, and days.
print(f"You are {years} years, {months} months, and {days} days old.")

#Check the users age group.
if years >= 60:
    print("You are a senior citizen.")
elif years >= 18:
    print("You are an adult.")
elif years >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

#Countdown till the user's next birthday.
#Create a datetime object for the user's next birthday.
if month == now.month and day == now.day:
    next_birhtday = datetime.datetime(year + 1, month, day)
elif month < now.month or (month == now.month and day < now.day):
    next_birthday = datetime.datetime(year + 1, month, day)
elif month > now.month or (month == now.month and day > now.day):
    next_birthday = datetime.datetime(now.year, month, day)

#Calculate the difference between the next birthday and the current date.
countdown = next_birthday - now

#Print the countdown in days.
print(f"There are {countdown.days} days left until your next birthday.")

#print the user's next birthday.
print(f"Your next birthday: {next_birthday.strftime('%Y-%m-%d')}")