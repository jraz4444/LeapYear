#Calculate the leap year
print("Calculate a leap year")

#Ask the user for a leap year
year = int(input("What year is it?"))
leapyear = False

#Stating whether the leap year is true or false
if  year % 4 == 0:
    leapyear = True
if year % 400 == 0:
    leapyear = True
if year % 100 == 0:
    leapyear = False

# Past 
if year < 2022 and year >= 1600 and leapyear == True:
    print(str(year) + " was a leap year.")
if year < 2022 and year > 1600 and leapyear == False:
    print(str(year) + " was not a leap year")

#Present
if year == 2022:
    print(str(year) + " is not a leap year")

 # Future 
if year > 2022 and leapyear == True:
    print(str(year) + " will be a leap year.")
if year > 2022 and leapyear == False:
    print(str(year) + " will not be a leap year")

#Before the Gregorian Calendar
if year < 1600:
    print("Error: " + str(year) + " was before adoption of the Gregorian calendar.")
