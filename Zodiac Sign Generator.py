import random
print("Hello! and Welcome to my Zodiac Sign / Horoscope generator!")
x, y = input("When were you born? Insert day then month (X Y): ").split()
x = int(x)
y = int(y)
zodiac = ""
print("Day of birth: ", x)
print("Month of birth: ", y)

if (y == 3 and x >= 21) or (y == 4 and x <=19):
    zodiac = "Aries"
elif (y == 4 and x >= 20) or (y == 5 and x <=20):
    zodiac = "Taurus"
elif (y == 5 and x >= 21) or (y == 6 and x <=21):
    zodiac = "Gemini"
elif (y == 6 and x >= 22) or (y == 7 and x <=22):
    zodiac = "Cancer"
elif (y == 7 and x >= 23) or (y == 8 and x <=22):
    zodiac = "Leo"
elif (y == 8 and x >= 23) or (y == 9 and x <=22):
    zodiac = "Virgo"
elif (y == 9 and x >= 23) or (y == 10 and x <=22):
    zodiac = "Libra"
elif (y == 10 and x >= 23) or (y == 11 and x <=21):
    zodiac = "Scorpio"
elif (y == 11 and x >= 22) or (y == 12 and x <=21):
    zodiac = "Sagittarius"
elif (y == 12 and x >= 22) or (y == 1 and x <=19):
    zodiac = "Capricorn"
elif (y == 1 and x >= 20) or (y == 2 and x <=18):
    zodiac = "Aquarius"
elif (y == 2 and x >= 19) or (y == 3 and x <=20):
    zodiac = "Pisces"
print("")
print("Your sign is:",zodiac)
print("")

signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]


print("Here are your Zodiac matches for today!")
print("Love: ", random.choice(signs))
print("Friendship: ", random.choice(signs))
print("Vibe: ", random.choice(signs))