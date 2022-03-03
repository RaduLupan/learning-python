print("Today's date?")

date=input()

print("Breakfast calories?")
breakfast=int(input())

print("Lunch calories?")
lunch=int(input())

print("Dinner calories?")
dinner=int(input())

daily_calories=breakfast+lunch+dinner

print("Daily calories for " + date + ": " +str(daily_calories))
