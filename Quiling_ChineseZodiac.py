year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

if (year - 2004) % 12 == 0:
    zodiac_sign = "Year of the Monkey"
elif (year - 2004) % 12 == 1:
    zodiac_sign = "Year of the Rooster"
elif (year - 2004) % 12 == 2:
    zodiac_sign = "Year of the Dog"
elif (year - 2004) % 12 == 3:
    zodiac_sign = "Year of the Pig"
elif (year - 2004) % 12 == 4:
    zodiac_sign = "Year of the Rat"
elif (year - 2004) % 12  == 5:
    zodiac_sign = "Year of the Ox"
elif (year - 2004) % 12 == 6:
    zodiac_sign = "Year of the Tiger"
elif (year - 2004) % 12 == 7:
    zodiac_sign = "Year of the Rabbit"
elif (year - 2004) % 12 == 8:
    zodiac_sign = "Year of the Dragon"
elif (year - 2004) % 12 == 9:
    zodiac_sign = "Year of the Snake"
elif (year - 2004) % 12 == 10:
    zodiac_sign = "Year of the Horse"
else:
    zodiac_sign = "Year of the Sheep"

print(f"Your Chinese Zodiac sign is: {zodiac_sign}," , "Happy Birthday To You Bro!" , "Gong hei fat choy!")